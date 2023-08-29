import re
import os
import glob
import math
import platform
import subprocess
from datetime import datetime

# below imports are used for sending an email
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from database.models import *
from mysite.settings import *
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .chatbot_settings import get_response
from django.contrib.auth.models import User
from backups.azureBlobStorage import listBlobs
from django.core.management import call_command
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from backups.azureBlobStorage import downloadBlob, deleteBlob


'''
    @Author: @DeanLogan
    @Description: Gets the account information (name, email, admins email, then if student: student number, pathway, current stage and semester) for the user currently logged into the system then formats this to be returned as a JSON object.
    @param: request -  HttpRequest object that contains metadata about the request
    @return: accountInfo - JSON object containing the necassary information for the user currently logged into the system. If a user is not logged into the system returns None
'''
def accountInfo(request):
    try:
        currentUser = request.user.username
        user = User.objects.get(username=currentUser) # gets the information about the current user from the database
        email = user.email
        name = user.first_name+' '+user.last_name
        studentNumber = ''
        pathwayName = ''
        currentSemester = ''
        currentStage = ''
        # tries to get information from the student table, if this fails it is safe to assume that the current user is not a student
        try:
            studentInDb = Student.objects.get(studentID=currentUser)
            studentNumber = str(currentUser)
            pathway = studentInDb.pathwayID
            pathwayName = Pathway.objects.get(pathwayID=pathway).pathwayName
            currentSemester = studentInDb.studentCurrentSemester
            currentStage = studentInDb.studentCurrentLevel
        except:
            pass
        
        admin = User.objects.get(username='admin') # gets the admin object from the database
        adminEmail = admin.email
        accountInfo = {
            'name': name,
            'email': email,
            'studentNumber': studentNumber,
            'pathway': pathwayName,
            'currentSemester': currentSemester,
            'currentStage': currentStage,
            'adminEmail': adminEmail
        }
    except:
        accountInfo = None # if a user is not logged into the system
    return JsonResponse(accountInfo, safe=False)

'''
    @Author: @DeanLogan
    @Description: Gets the information needed for sign-up then sends an email containing this informatuion, or if email cannot be sent a fail message. 
    @param: request -  HttpRequest object that contains metadata about the request
    @return: success - JSON object containing true or false (stored as string as in Django a response can only have a JSON object with strings), depending if a successful email was sent to the admin
'''
def signUp(request):
    # get required info
    success = {'success':'true'}
    try:
        studentNumber = request.GET.get('studentNumber')
        name = request.GET.get('name')
        email = request.GET.get('email')
        selectedPathway = request.GET.get('selectedPathway')
        currentStage = request.GET.get('currentStage')
        currentSemester = request.GET.get('currentSemester')

        admin = User.objects.get(username='admin')
        adminEmail = admin.email

        # below formats the information into an email
        msg = MIMEMultipart()
        msg['From'] = 'pathfinder3068@gmail.com'
        msg['To'] = "{0}".format(adminEmail)
        msg['Subject'] = 'Sign-Up User'

        messageContentInHtml = '<h1>Request has been made to sign up user</h1><br/><p><b>Student Number: </b>'+studentNumber+'</p><p><b>Name: </b>'+name+'</p><p><b>Email: </b>'+email+'</p><p><b>Pathway: </b>'+selectedPathway+'</p><p><b>Stage: </b>'+currentStage+'</p><p><b>Semester: </b>'+currentSemester+'</p><br/><p>From Pathfinder.'

        body = MIMEText(messageContentInHtml, 'html')
        msg.attach(body)

        server = smtplib.SMTP('smtp.gmail.com', 587) # connect to email server
        server.starttls() #encrypts login
        server.login('pathfinder3068@gmail.com', 'eglrgyaxlnyrvixi') # email account and 3rd party app password for the account which the email will be sent from
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        success = {'success':'false'}

    return JsonResponse(success, safe=False)

'''
    @Author: @DeanLogan
    @Description: Returns a JSON object with all the pathway names and the stage the pathway is on formatted into a JSON object. 
    @param: request -  HttpRequest object that contains metadata about the request
    @return: pathwayList - JSON object containing the pathway information
'''
def listOfPathways(request):
    pathwayList = []
    allPathwayObjects = Pathway.objects.all()
    for i in range(len(allPathwayObjects)):
        name = allPathwayObjects[i].pathwayName
        stages = allPathwayObjects[i].pathwayLevels
        pathwayInfo = {'name':name,'stages':stages}
        pathwayList.append(pathwayInfo)

    return JsonResponse({'pathwayList':pathwayList}, safe=False)

'''
    @Author: @DeanLogan
    @Description: Gets the username and password from the request then checks if these credentials are on the system, returns true or false based on authentication result.
    @param: request -  HttpRequest object that contains metadata about the request
    @return: loggedIn - JSON object containing whether or not a the log in attempt was successful
'''
@csrf_exempt
def verify(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'loggedIn': 'true'})
        else:
            return JsonResponse({'loggedIn': 'false'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

"""
    @Author: @DeanLogan
    @Description: Lists the names of local backup files in descending order of modification time (newest first).
    @param: request - HttpRequest object that contains metadata about the request (unused in this function).
    @return: JsonResponse with a dictionary containing 'fileNames' as keys and the list of file names as values.
"""
def listLocalBackupFiles(request):
    try:
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump')) # Check the number of existing backup files
        
        fileNames = [os.path.basename(file) for file in backupFiles]  # Extract only the filenames

        fileNames = sorted(fileNames, key=lambda filename: extractedDate(filename), reverse=True) # Sort the array based on the extracted dates from file name (newest first)
        
        return JsonResponse({'fileNames': fileNames}, safe=False)
    except:
        return JsonResponse({'fileNames': []}, safe=False)

"""
    @Author: @DeanLogan
    @Description: Extracts the date and hash information from a backup filename.
    @param: filename - The filename to extract information from.
    @return: A tuple containing the extracted datetime object and hash part (if any).
"""
def extractedDate(filename):
    match = re.search(r'(\d{4}-\d{2}-\d{2}-\d{6})(?:_(.*))?\.dump', filename)
    
    if match:
        date_part = match.group(1)  # Extract the date part from the filename
        hash_part = match.group(2) or ""  # Extract the hash part or use an empty string if not present
        
        # Convert the date part to a datetime object using the specified format
        extracted_datetime = datetime.strptime(date_part, '%Y-%m-%d-%H%M%S')
        
        return extracted_datetime, hash_part
    else:
        return None, None  # Return None if no match is found in the filename

# TODO: Refactor the restore and rollback functions to reduce code repetition  

"""
@Author: @DeanLogan
@Description: Restores the database from a local backup file if the user is authenticated as 'admin'.
@param: request - HttpRequest object that contains metadata about the request.
@return: JsonResponse indicating the status of the restore operation.
"""
def restoreBackup(request):
    try:
        # Check if the user is authenticated as 'admin'
        if request.user.is_authenticated and request.user.username == 'admin':
            if request.GET.get('cloud') == 'true':
                backupFile = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], 'temp', request.GET.get('fileName'))
                if not downloadBlob(request.GET.get('fileName'), backupFile):
                    return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if blob download fails
            else:
                backupFile = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], request.GET.get('fileName'))
            restoreFromBackup(backupFile)  # Restore the database from the specified backup file
            restoreFromBackup(backupFile)  # Restore again to ensure all data is added (dependency issues)
            
            if request.GET.get('cloud') == 'true':
                os.remove(backupFile)  # Remove the downloaded backup file if it was downloaded from cloud storage
    except:
        return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if an exception occurs
    return JsonResponse({'Status': 'true'}, safe=False)  # Return status 'true' if the operation is successful

"""
@Author: @DeanLogan
@Description: Rolls back the database to a previous state by restoring a backup file.
@param: request - HttpRequest object that contains metadata about the request.
@return: JsonResponse indicating the status of the rollback operation.
"""
def rollbackBackup(request):
    try:
        # Check if the user is authenticated as 'admin'
        if request.user.is_authenticated and request.user.username == 'admin':
            if request.GET.get('cloud') == 'true':
                backupFile = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], 'temp', request.GET.get('fileName'))
                if not downloadBlob(request.GET.get('fileName'), backupFile):
                    return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if blob download fails
            else:
                backupFile = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], request.GET.get('fileName'))
            
            # Delete database data and restore from the backup file
            call_command('flush', '--noinput', '--database=default', '--skip-checks')  # Delete all data from the default database
            restoreFromBackup(backupFile)  # Restore the database from the specified backup file
            restoreFromBackup(backupFile)  # Restore again to ensure all data is added (dependency issues)
            
            if request.GET.get('cloud') == 'true':
                os.remove(backupFile)  # Remove the downloaded backup file if it was downloaded from cloud storage
    except:
        return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if an exception occurs
    
    return JsonResponse({'Status': 'true'}, safe=False)  # Return status 'true' if the operation is successful


"""
@Author: @DeanLogan
@Description: Deletes a backup file if the user is authenticated as 'admin'.
@param: request - HttpRequest object that contains metadata about the request.
@return: JsonResponse indicating the status of the delete operation.
"""
def deleteBackup(request):
    try:
        # Check if the user is authenticated as 'admin'
        if request.user.is_authenticated and request.user.username == 'admin':
            if request.GET.get('cloud') == 'true':
                deleteBlob(request.GET.get('fileName'))
            else:
                file_path = os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], request.GET.get('fileName'))
                os.remove(file_path)  # Delete the specified backup file
    except:
        return JsonResponse({'Status': 'false'}, safe=False)  # Return status 'false' if an exception occurs
    
    return JsonResponse({'Status': 'true'}, safe=False)  # Return status 'true' if the operation is successful

"""
@Author: @DeanLogan
@Description: Restores a database backup from the specified file using Django's 'dbrestore' management command.
@param: filePath - The path to the backup file to restore from.
"""
def restoreFromBackup(filePath):
# Determine the platform (OS) and adjust the command accordingly
    if platform.system() == "Windows":
        print("windows")
        subprocess.run(" ".join([
            "python", "manage.py", "dbrestore",
            "-I",
            f'"{filePath}"',
            "--noinput",
            "--skip-checks"
        ]), shell=True)  # Run the command as a single string using shell (Windows)
    else:
        print("unix")
        subprocess.run([
            "python", "manage.py", "dbrestore",
            "-I",
            f"{filePath}",
            "--noinput",
            "--skip-checks"
        ])  # Run the command as a list (Linux, macOS)
    with connection.cursor() as cursor:
        cursor.execute("VACUUM;")
    print("complete vacum (hopefully)")

"""
    @Author: @DeanLogan
    @Description: Retrieves and returns a list of cloud backup file names from a Blob Storage container.
    @param: request - HttpRequest object that contains metadata about the request (unused in this function).
    @return: JsonResponse with a dictionary containing 'fileNames' as keys and the list of cloud backup file names as values.
"""
def listCloudBackupFiles(request):
    try:
        return JsonResponse({'fileNames': listBlobs()}, safe=False)
    except:
        return JsonResponse({'fileNames': []}, safe=False)

'''
    @Author: @KyleMcComb
'''
def receive_message(request):
    message = request.GET.get('message')
    response = get_response(message)
    return JsonResponse({'message': response})

'''
    @Author: @KyleMcComb
    @Description: Renders the index.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def index(request):
    return render(request, 'index.html')

'''
    @Author: @DeanLogan
    @Description: Renders the settings.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def settings(request):
    return render(request, 'settings.html')

'''
    @Author: @DeanLogan
    @Description: Renders the gradeDashboard.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def gradeDashboard(request):
    return render(request, 'gradeDashboard.html')

'''
    @Author: @DeanLogan
    @Description: Renders the moduleInformation.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def moduleInformation(request):
    return render(request, 'moduleInformation.html')
