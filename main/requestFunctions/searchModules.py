from database.models import *
from django.http import JsonResponse

'''
    @Author: @DeanLogan
    @Description: Gets the information needed for sign-up then sends an email containing this informatuion, or if email cannot be sent a fail message. 
    @param: request -  HttpRequest object that contains metadata about the request
    @return: moduleList - JSON object containing a list of all modules that meet the search term
'''
def searchModulesRequest(request):
    moduleName = request.GET.get('moduleName') # the search term for the module(s) to be searched for
    if(moduleName != ''): # if the search term is empty then return all modules within the database
        allModules = Module.objects.filter(moduleName__contains=moduleName) # returns a query set of all the module objects, that have module names that contain a sub string of moduleName
    else:
        allModules = Module.objects.all()

    moduleList = [getModuleInfofromObject(module) for module in allModules]

    return JsonResponse({'moduleList':moduleList}, safe=False)

'''
@Author: @DeanLogan
@Description: extracts the module information (name, code, lecturer(s), stage, semester, weighting, assessments and description) from the given module object, formatting any 1-many relationships into a list.
@param: moduleObject - Module object containing metadata about the module
@return: infoNeeded - Dictionary containing module information for the given module object
'''
def getModuleInfofromObject(moduleObject):
    moduleCode = moduleObject.moduleID

    pathways = Pathway.objects.filter(modulepathway__moduleID=moduleCode).values_list('pathwayName', flat=True)
    pathwaysStr = ', '.join(pathways)

    lecturers = Lecturer.objects.filter(modulelecturer__moduleID=moduleCode).values_list('lecturerName', flat=True)
    lecturersStr = ', '.join(lecturers)

    assessmentsInfo = Assessment.objects.filter(moduleID=moduleCode).values_list('assessmentType', 'assessmentWeight')
    assessmentsStr = ', '.join([f'{atype} ({aweight}%)' for atype, aweight in assessmentsInfo])

    infoNeeded = {
        'name': moduleObject.moduleName,
        'code': moduleCode,
        'lecturer': lecturersStr,
        'stage': moduleObject.moduleLevel,
        'semester': moduleObject.moduleSemester,
        'weighting': moduleObject.moduleWeight,
        'pathways': pathwaysStr,
        'assesments': assessmentsStr,
        'description': moduleObject.moduleDescription
    }

    return infoNeeded