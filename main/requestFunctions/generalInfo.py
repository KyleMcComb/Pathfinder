from database.models import *
from django.http import JsonResponse
from django.contrib.auth.models import User

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
        email = user.email.strip()  # Remove leading and trailing whitespace
        name = f"{user.first_name} {user.last_name}"  # Remove leading and trailing whitespace        
        studentNumber = ''
        pathwayName = ''
        currentSemester = ''
        currentStage = ''
        
        if not email:
            email = "This information could not be found on the database or the stored information is blank"
        
        if not name.strip():
            name = "This information could not be found on the database or the stored information is blank"
        
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