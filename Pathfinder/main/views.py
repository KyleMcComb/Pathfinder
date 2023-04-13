from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_settings import get_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from database.models import *
from django.core import serializers
import math

def moduleInfo(request):
    moduleList = [];
    allModules = Module.objects.all()
    for i in range(len(allModules)):
        name = allModules[i].moduleName
        code = allModules[i].moduleID
        stage = allModules[i].moduleLevel
        semester = allModules[i].moduleSemester
        weighting = allModules[i].moduleWeight
        description = allModules[i].moduleDescription

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
        moduleList.append(infoNeeded)
    #moduleName = Pathway.objects.filter(pathwayID__contains="G4")
    #qs_json = serializers.serialize('json', moduleName)
    qs_json = [{'name':'dean'},{'name':'john'}]
    #print(qs_json)
    #return HttpResponse(qs_json, content_type='application/json')
    return JsonResponse({'moduleList':moduleList}, safe=False)

def gradeInfo(request):
    currentUser = request.user.username
    studentInDb = Student.objects.get(studentID=currentUser)
    studentInfoInDb = StudentInfo.objects.get(studentID=currentUser)
    currentStage = studentInfoInDb.stuInfoCurrentLevel
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
