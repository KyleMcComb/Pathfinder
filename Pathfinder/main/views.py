from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_settings import get_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from database.models import *
from django.contrib.auth.models import User
import math

# below imports are used for sending an email
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def accountInfo(request):
    try:
        currentUser = request.user.username
        print(currentUser)
        user = User.objects.get(username=currentUser)
        email = user.email
        name = user.first_name+' '+user.last_name
        studentNumber = ''
        pathwayName = ''
        currentSemester = ''
        currentStage = ''
        try:
            studentInDb = Student.objects.get(studentID=currentUser)
            studentNumber = str(currentUser)
            pathway = studentInDb.pathwayID
            pathwayName = Pathway.objects.get(pathwayID=pathway).pathwayName
            currentSemester = studentInDb.studentCurrentSemester
            currentStage = studentInDb.studentCurrentLevel
        except:
            pass
        
        admin = User.objects.get(username='admin')
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
        accountInfo = None
    return JsonResponse(accountInfo, safe=False)


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

        # send email
        msg = MIMEMultipart()
        msg['From'] = 'pathfinder3068@gmail.com'
        msg['To'] = "{0}".format(adminEmail)
        msg['Subject'] = 'Sign-Up User'

        messageContentInHtml = '<h1>Request has been made to sign up user</h1><br/><p><b>Student Number: </b>'+studentNumber+'</p><p><b>Name: </b>'+name+'</p><p><b>Email: </b>'+email+'</p><p><b>Pathway: </b>'+selectedPathway+'</p><p><b>Stage: </b>'+currentStage+'</p><p><b>Semester: </b>'+currentSemester+'</p><br/><p>From Pathfinder.'

        body = MIMEText(messageContentInHtml, 'html')
        msg.attach(body)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() #encrypts login
        server.login('pathfinder3068@gmail.com', 'eglrgyaxlnyrvixi') # email account and 3rd party app password for the account which the email will be sent from
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        success = {'success':'false'}

    return JsonResponse(success, safe=False)

def listOfPathways(request):
    pathwayList = []
    allPathwayObjects = Pathway.objects.all()
    for i in range(len(allPathwayObjects)):
        name = allPathwayObjects[i].pathwayName
        stages = allPathwayObjects[i].pathwayLevels
        pathwayInfo = {'name':name,'stages':stages}
        pathwayList.append(pathwayInfo)

    return JsonResponse({'pathwayList':pathwayList}, safe=False)

def searchModules(request):
    moduleName = request.GET.get('moduleName')
    if(moduleName != ''):
        allModules = Module.objects.filter(moduleName__contains=moduleName)
    else:
        allModules = Module.objects.all()

    moduleList = [];
    for i in range(len(allModules)):
        moduleList.append(getModuleInfofromObject(allModules[i]))
    return JsonResponse({'moduleList':moduleList}, safe=False)

def getModuleInfofromObject(moduleObject):
    name = moduleObject.moduleName
    code = moduleObject.moduleID
    stage = moduleObject.moduleLevel
    semester = moduleObject.moduleSemester
    weighting = moduleObject.moduleWeight
    description = moduleObject.moduleDescription

    pathwaysOn = ModulePathway.objects.filter(moduleID=code) # searches ModulePathway linking table to find all records of pathways that are linked to a module
    temp = []
    for j in range(len(pathwaysOn)):
        temp.append(Pathway.objects.get(pathwayID=pathwaysOn[j].pathwayID).pathwayName)
    pathways = ', '.join(temp);

    lecturers = ModuleLecturer.objects.filter(moduleID=code)
    temp = []
    for j in range(len(lecturers)):
        temp.append(Lecturer.objects.get(lecturerID=str(lecturers[j].lecturerID)).lecturerName)
    lecturer = ', '.join(temp);

    temp = []
    assesmentsIncluded = Assessment.objects.filter(moduleID=code)
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

def gradeInfo(request):
    currentUser = request.user.username
    studentInDb = Student.objects.get(studentID=currentUser)
    currentStage = studentInDb.studentCurrentLevel
    studentModuleInfo = StudentModule.objects.filter(studentID=currentUser) # array of the modules the student takes

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

        #allAssessmentsStudentHasTaken = StudentModuleAssesment.objects.get(studentModuleID=studentModuleInfo[i])

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

    # works out moduleAvg
    studentsTotalMark = 0
    assessmentsTotalMark = 0
    assessmentsTotalMarksAvailable = 0
    totalMarksAvailable = 0
    stageMarks = []
    for i in range(len(stages)):
        stageMark = 0
        for j in range(len(stages[i])):
            moduleWeighting = stages[i][j]['weighting']
            markForModule = stages[i][j]['studentMark']
            assessmentsInModule = stages[i][j]['assessments']
            
            studentsTotalMark += markForModule
            totalMarksAvailable += 100

            for x in range(len(assessmentsInModule)):
                assessmentsTotalMark += assessmentsInModule[x]['mark']
                assessmentsTotalMarksAvailable += 100

            stageMark += moduleWeighting * (markForModule/100) # calculates how much of the available CAT points you have earnt
        stageMarks.append(stageMark)

    moduleAvg = (studentsTotalMark / totalMarksAvailable)*100
    assessmentAvg = (assessmentsTotalMark / assessmentsTotalMarksAvailable) * 100

    leftToEarn = 0
    totalNumOfStages = Pathway.objects.get(pathwayID=studentInDb.pathwayID).pathwayLevels
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

    allGradeInfo = {
        'currentPathwayMark': str(math.trunc(round(currentPathwayMark, 0))),
        'moduleAvg': str(math.trunc(round(moduleAvg,0))),
        'assesmentAvg': str(math.trunc(round(assessmentAvg,0))),
        'leftToEarn': str(math.trunc(round(leftToEarn,0))),
        'stages': stages
    }

    return JsonResponse(allGradeInfo, safe=False)

# for login 
def verify(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'loggedIn': 'true'})
    else:
        return JsonResponse({'loggedIn': 'false'})

def index(request):
    return render(request, 'index.html')

def receive_message(request):
    message = request.GET.get('message')
    response = get_response(message)
    return JsonResponse({'message': response})

def settings(request):
    return render(request, 'settings.html')

def gradeDashboard(request):
    return render(request, 'gradeDashboard.html')

def moduleInformation(request):
    return render(request, 'moduleInformation.html')
