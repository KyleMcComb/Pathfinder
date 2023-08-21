from database.models import *
from mysite.settings import *
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .chatbot_settings import get_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import os
import glob
import math

# below imports are used for sending an email
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

'''
    @Author: @DeanLogan123
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
    @Author: @DeanLogan123
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
    @Author: @DeanLogan123
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
    @Author: @DeanLogan123
    @Description: Gets the information needed for sign-up then sends an email containing this informatuion, or if email cannot be sent a fail message. 
    @param: request -  HttpRequest object that contains metadata about the request
    @return: moduleList - JSON object containing a list of all modules that meet the search term
'''
def searchModules(request):
    moduleName = request.GET.get('moduleName') # the search term for the module(s) to be searched for
    if(moduleName != ''): # if the search term is empty then return all modules within the database
        allModules = Module.objects.filter(moduleName__contains=moduleName) # returns a query set of all the module objects, that have module names that contain a sub string of moduleName
    else:
        allModules = Module.objects.all()

    moduleList = [];
    for i in range(len(allModules)):
        moduleList.append(getModuleInfofromObject(allModules[i])) # extracts the module information from the module objects then adds them to a list
    return JsonResponse({'moduleList':moduleList}, safe=False)


'''
    @Author: @DeanLogan123
    @Description: extracts the module information (name, code, lecturer(s), stage, semester, weighting, assesments and description) from the given module object, formating any 1-many relationships into a list.
    @param: request -  HttpRequest object that contains metadata about the request
    @return: infoNeeded - JSON object containing module information for the given module object
'''
def getModuleInfofromObject(moduleObject):
    name = moduleObject.moduleName
    code = moduleObject.moduleID
    stage = moduleObject.moduleLevel
    semester = moduleObject.moduleSemester
    weighting = moduleObject.moduleWeight
    description = moduleObject.moduleDescription

    pathwaysOn = ModulePathway.objects.filter(moduleID=code) # searches ModulePathway linking table to find all records of pathways that are linked to a module then adds the name of these to a list
    temp = []
    for j in range(len(pathwaysOn)):
        temp.append(Pathway.objects.get(pathwayID=pathwaysOn[j].pathwayID).pathwayName)
    pathways = ', '.join(temp);

    lecturers = ModuleLecturer.objects.filter(moduleID=code) # searches ModuleLecturer linking table to find all records of lecturers that are linked to a module then adds the name of these to a list
    temp = []
    for j in range(len(lecturers)):
        temp.append(Lecturer.objects.get(lecturerID=str(lecturers[j].lecturerID)).lecturerName)
    lecturer = ', '.join(temp);

    temp = []
    assesmentsIncluded = Assessment.objects.filter(moduleID=code) # searches Assessment table to find all records of assessments that are linked to a module then adds the name of these to a list
    for j in range(len(assesmentsIncluded)):
        temp.append(assesmentsIncluded[j].assessmentType+' ('+str(assesmentsIncluded[j].assessmentWeight)+'%)')
    assesments = ', '.join(temp);
    
    infoNeeded = {
        'name': name, #string
        'code': code, #string
        'lecturer': lecturer,
        'stage': stage, #string
        'semester': semester, #string
        'weighting': weighting, #string
        'pathways': pathways, #string comma seperated for each pathway
        'assesments': assesments, #string comma seperated for each assesment
        'description': description #string
    }
    
    return infoNeeded

'''
    @Author: @DeanLogan123
    @Description: Calculates the students module average and assesment average throughout their degree, also gets all the modules a student takes along with the assesments relating to those modules and the grades for all the modules and assesments. 
    @param: request -  HttpRequest object that contains metadata about the request
    @return: allGradeInfo - JSON object containing the grade information for the user
'''
def gradeInfo(request):
    currentUser = request.user.username
    studentInDb = Student.objects.get(studentID=currentUser) # gets record for the student who is currently logged in
    currentStage = studentInDb.studentCurrentLevel
    studentModuleInfo = StudentModule.objects.filter(studentID=currentUser) # query set of the module objects that student takes

    # below gets the modules, module marks, assessments and assessment marks that a student is on

    # Adds inner arrays to the stages array. Each inner array represents a stage the student has completed (or currently in)
    stages = []
    for i in range(currentStage):
        stages.append([]);

    for i in range(len(studentModuleInfo)):
        moduleId = studentModuleInfo[i].moduleID
        moduleInStage = Module.objects.get(moduleID=moduleId).moduleLevel
        moduleName = Module.objects.get(moduleID=moduleId).moduleName
        moduleWeighting = Module.objects.get(moduleID=moduleId).moduleWeight
        studentMark = studentModuleInfo[i].stuModMark
        assessmentsForModule = Assessment.objects.filter(moduleID=moduleId)

        assessments = []
        assessmentsStudentHasCompleted = StudentModuleAssesment.objects.filter(studentModuleID=studentModuleInfo[i])
        for j in range(len(assessmentsStudentHasCompleted)):
            assessmentName = assessmentsStudentHasCompleted[j].assessmentID.assessmentType
            assessmentMark = assessmentsStudentHasCompleted[j].assesmentMark

            studentAssessmentInfo = {
                'name': assessmentName,
                'mark': assessmentMark
            }
            assessments.append(studentAssessmentInfo)

        studentModuleInfoJSON = {
            'name': moduleName,
            'studentMark': studentMark,
            'weighting': moduleWeighting,
            'assessments': assessments
        }
        stages[moduleInStage-1].append(studentModuleInfoJSON) # adds the module in the correct array for the corresponding stage
    
    currentPathwayMark = studentInDb.currentPathwayMark
    
    avgs = moduleAndAssesmentAvg(stages)
    moduleAvg = avgs[0]
    assessmentAvg = avgs[1]
    
    allGradeInfo = {
        'currentPathwayMark': str(math.trunc(round(currentPathwayMark, 0))),
        'moduleAvg': str(math.trunc(round(moduleAvg,0))),
        'assesmentAvg': str(math.trunc(round(assessmentAvg,0))),
        'leftToEarn': str(math.trunc(round(calcLeftToEarn(currentStage, studentInDb),0))),
        'stages': stages
    }
    
    return JsonResponse(allGradeInfo, safe=False)

'''
    @Author: @DeanLogan123
    @Description: Calculates the students module average and assesment average based on the information that is stored in their stages dictionary
    @param: stages - dictionary that contains a students information for each one of their stages, the module information for each given stage 
    @return: avgs - array containing the module average and assessment average based on the information within stages
'''
def moduleAndAssesmentAvg(stages):
    # works out moduleAvg and assessmentAvg
    studentsTotalMark = 0
    assessmentsTotalMark = 0
    assessmentsTotalMarksAvailable = 0
    totalMarksAvailable = 0
    stageMarks = []
    # this loop is for the stages that the student has completed
    for i in range(len(stages)):
        stageMark = 0
        # this loops is for the modules that are witin a stage
        for j in range(len(stages[i])):
            moduleWeighting = stages[i][j]['weighting']
            markForModule = stages[i][j]['studentMark']
            assessmentsInModule = stages[i][j]['assessments']
            
            studentsTotalMark += markForModule
            totalMarksAvailable += 100 # assumes all modules are marked out of 100
            
            # this loop is for the assessments that are within a module
            for x in range(len(assessmentsInModule)):
                assessmentsTotalMark += assessmentsInModule[x]['mark']
                assessmentsTotalMarksAvailable += 100
            
            stageMark += moduleWeighting * (markForModule/100) # calculates how much of the available CAT points the student has earned based on the weighting of the module
        stageMarks.append(stageMark)
    
    moduleAvg = (studentsTotalMark / totalMarksAvailable)*100
    assessmentAvg = (assessmentsTotalMark / assessmentsTotalMarksAvailable) * 100

    avgs = [moduleAvg, assessmentAvg]

    return avgs

'''
    @Author: @DeanLogan123
    @Description: Calculates how much of the degree is left to earn for a given student.
    @param: currentStage - the stage the student is currently on
    @param: studentInDb - student object for the student the calculation is for
    @return: leftToEarn - the percentage amount the student has left to earn of their degrees
'''
def calcLeftToEarn(currentStage, studentInDb):
    # works out how much is left to earn in the degree based on their current stage, note these numbers are currently place holders may not be accurate with the actual weighting for stages
    leftToEarn = 0
    totalNumOfStages = Pathway.objects.get(pathwayID=studentInDb.pathwayID).pathwayLevels # gets the total number of stages for the pathway that the student is on
    if (totalNumOfStages == 3):
        if (currentStage == 1):
            leftToEarn = 90
        elif (currentStage == 2):
            leftToEarn = 60
        elif (currentStage == 3):
            leftToEarn = 0
    elif (totalNumOfStages == 4):
        if (currentStage == 1):
            leftToEarn = 90
        elif (currentStage == 2):
            leftToEarn = 40
        elif (currentStage == 3):
            leftToEarn = 20
        elif (currentStage == 4):
            leftToEarn = 0

    return leftToEarn

'''
    @Author: @DeanLogan123
    @Description: Gets the username and password from the request then checks if these credentials are on the system, returns true or false based on authentication result.
    @param: request -  HttpRequest object that contains metadata about the request
    @return: loggedIn - JSON object containing whether or not a the log in attempt was successful
'''
def verify(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'loggedIn': 'true'})
    else:
        return JsonResponse({'loggedIn': 'false'})

"""
    @Author: DeanLogan123
    @Description: Lists the names of local backup files in descending order of modification time (newest first).
    @param: request - HttpRequest object that contains metadata about the request (unused in this function).
    @return: JsonResponse with a dictionary containing 'fileNames' as keys and the list of file names as values.
"""
def listLocalBackupFiles(request):
    try:
        backupFiles = glob.glob(os.path.join(DBBACKUP_STORAGE_OPTIONS['location'], '*.dump')) # Check the number of existing backup files
        backupFiles.sort(key=os.path.getmtime, reverse=True) # Sort backup files by modification time (newest first)
        
        fileNames = [os.path.basename(file) for file in backupFiles]  # Extract only the filenames
        
        return JsonResponse({'fileNames': fileNames}, safe=False)
    except:
        return JsonResponse({'fileNames': []}, safe=False)

"""
    @Author: DeanLogan123
    @Description: Retrieves and returns a list of cloud backup file names from a Blob Storage container.
    @param: request - HttpRequest object that contains metadata about the request (unused in this function).
    @return: JsonResponse with a dictionary containing 'fileNames' as keys and the list of cloud backup file names as values.
"""
from backups.azureBlobStorage import listBlobs
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
    @Author: @DeanLogan123
    @Description: Renders the settings.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def settings(request):
    return render(request, 'settings.html')

'''
    @Author: @DeanLogan123
    @Description: Renders the gradeDashboard.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def gradeDashboard(request):
    return render(request, 'gradeDashboard.html')

'''
    @Author: @DeanLogan123
    @Description: Renders the moduleInformation.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def moduleInformation(request):
    return render(request, 'moduleInformation.html')
