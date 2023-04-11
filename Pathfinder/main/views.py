from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_settings import get_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from database.models import *
from django.core import serializers

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
            temp.append(Lecturer.objects.get(lecturerID=lecturers[j].lectureID).lecturerName)
        lecturer = ', '.join(temp);

        temp = []
        assesmentsIncluded = Assessment.objects.filter(moduleID=code)
        for j in range(len(assesmentsIncluded)):
            temp.append(assesmentsIncluded[i].assessmentType+' ('+assesmentsIncluded[i].assessmentWeight+'%)')
        assesments = ', '.join(temp);
        assesments = 'name1 (20%), name2 (80%)'
        
        infoNeeded = {
            'name': name, #string
            'code': code,
            'lecturer': lecturer,
            'stage': stage, #string
            'semester': semester, #string
            'weighting': weighting, #string
            'pathways': pathways, #string comma seperated
            'assesments': assesments, #json
            'description': description #string
        }
        moduleList.append(infoNeeded)
    #moduleName = Pathway.objects.filter(pathwayID__contains="G4")
    #qs_json = serializers.serialize('json', moduleName)
    qs_json = [{'name':'dean'},{'name':'john'}]
    #print(qs_json)
    #return HttpResponse(qs_json, content_type='application/json')
    return JsonResponse({'moduleList':moduleList}, safe=False)

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
