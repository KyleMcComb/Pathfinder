import json
import math
from collections import defaultdict

from database.models import *
from django.http import JsonResponse


"""
@Author: DeanLogan
@Description: Generates and returns information about modules for a given student up to a specified stage.
@param: student - Student object representing the student for whom module information is generated.
@param: currentStage - The current stage up to which module information is generated.
@return: A list of dictionaries containing module information organized by stages.
"""
def moduleInfoForStudent(student, currentStage):
    # Retrieve student's enrolled modules along with module levels
    studentModules = StudentModule.objects.filter(studentID=student.studentID).select_related('moduleID')
    moduleLevels = studentModules.values_list('moduleID', 'moduleID__moduleLevel')
    moduleIds = [moduleId for moduleId, _ in moduleLevels]
    
    assessmentInfos = {moduleId: assessmentInfoForStudentsModule(student, moduleId) for moduleId in moduleIds} # Retrieve assessment information for each module
    # Retrieve module names and weights
    moduleNamesAndWeights = Module.objects.filter(moduleID__in=moduleIds).values('moduleID', 'moduleName', 'moduleWeight')
    studentModuleInfoAsStages = defaultdict(list)
    
    # Organize module information by stages
    for moduleId, moduleLevel in moduleLevels:
        moduleInfo = next((info for info in moduleNamesAndWeights if info['moduleID'] == moduleId), None)
        if moduleInfo:
            studentModuleInfoAsStages[moduleLevel - 1].append({
                'name': moduleInfo['moduleName'],
                'mark': studentModules.get(moduleID=moduleId).stuModMark,
                'weighting': moduleInfo['moduleWeight'],
                'assessments': assessmentInfos[moduleId]
            })
    
    return [studentModuleInfoAsStages[i] for i in range(currentStage)] # Return module information up to the specified current stage

"""
@Author: DeanLogan
@Description: Retrieves and returns assessment information for a student's specific module.
@param: studentID - ID of the student for whom assessment information is retrieved.
@param: moduleID - ID of the module for which assessment information is retrieved.
@return: A list of dictionaries containing assessment information for the student's module.
"""
def assessmentInfoForStudentsModule(studentID, moduleID):
    # Retrieve the student's module and related assessment records
    studentModule = StudentModule.objects.prefetch_related('moduleID').get(studentID_id=studentID, moduleID_id=moduleID)
    studentAssessments = StudentModuleAssessment.objects.filter(studentModuleID=studentModule).select_related('assessmentID__moduleID')
    
    assessmentInfo = []
    
    # Create a list of dictionaries containing assessment information
    for studentAssessment in studentAssessments:
        assessmentInfo.append({
            'name': studentAssessment.assessmentID.assessmentType,
            'mark': studentAssessment.assessmentMark,
            'id': studentAssessment.studentModuleAssessmentID
        })
    
    return assessmentInfo

"""
@Author: @DeanLogan
@Description: Calculates the average module mark across all stages.
@param: stages - A list of stages, each containing a list of modules with assessments.
@return: The calculated average module mark or 0 if no modules are present.
"""
def moduleAvgAllStages(stages):
    avgForStage = 0
    for stage in stages:
        avgForStage += calcAvgMark(stage)
    
    return avgForStage / len(stages)

"""
@Author: @DeanLogan
@Description: Calculates the average assessment mark across all stages and modules.
@param: stages - A list of stages, each containing a list of modules with assessments.
@return: The calculated average assessment mark or 0 if no assessments are present.
"""
def assessmentAvgAllStages(stages):
    avgForModules = 0
    numOfModules = 0
    for stage in stages:
        numOfModules += len(stage)
        for module in stage:
            avgForModules += calcAvgMark(module['assessments'])
    
    return avgForModules / numOfModules if numOfModules != 0 else 0

"""
@Author: @DeanLogan
@Description: Calculates the average mark from a list of grade dictionaries.
@param: arr - List of dictionaries containing 'mark' values.
@return: The calculated average mark or 0 if the list is empty.
"""
def calcAvgMark(arr):
    return sum(grade['mark'] for grade in arr) / len(arr) if len(arr) != 0 else 0


"""
@Author: @DeanLogan
@Description: Calculates the number of credits left to earn in a student's pathway.
@param: currentStage - The current stage of the student's progress.
@param: studentInDb - The student's database object containing information such as the pathway.
@return: The number of credits left to earn in the student's pathway.
"""
def calcLeftToEarn(currentStage, studentInDb):
    # Lookup table for credits left to earn at different stages based on pathway stages
    leftTOEarnLookUp = {
        3: [90, 60, 0],
        4: [90, 40, 20, 0]
    }
    
    # Get the total stages in the student's pathway
    pathwayStages = Pathway.objects.get(pathwayID=studentInDb.pathwayID).pathwayLevels
    
    if pathwayStages in leftTOEarnLookUp:
        leftToEarnValues = leftTOEarnLookUp[pathwayStages]
        leftToEarn = leftToEarnValues[currentStage - 1] if currentStage <= pathwayStages else 0
    else:
        leftToEarn = 0

    return leftToEarn

"""
@Author: @DeanLogan
@Description: Retrieves and returns various grade-related information for a student.
@param: request - The HttpRequest object containing user information.
@return: JsonResponse with grade-related information or an error message.
"""
def gradeInfoRequest(request):
    try:
        studentInDb = Student.objects.get(studentID=request.user.username)
        currentStage = studentInDb.studentCurrentLevel
        stagesInfo = moduleInfoForStudent(studentInDb, currentStage)
        
        return JsonResponse(
            {
                'error': 'False',
                'currentPathwayMark': str(math.trunc(round(studentInDb.currentPathwayMark, 0))),
                'moduleAvg': str(math.trunc(round(moduleAvgAllStages(stagesInfo), 0))),
                'assessmentAvg': str(math.trunc(round(assessmentAvgAllStages(stagesInfo), 0))),
                'leftToEarn': str(math.trunc(round(calcLeftToEarn(currentStage, studentInDb), 0))),
                'stages': stagesInfo
            }, 
            safe=False
        )
    except:
        return JsonResponse({'error': 'True'}, safe=False)


"""
@Author: @DeanLogan
@Description: Update assessment marks for students.
@param: request - The HttpRequest object containing assessment grades.
@return: JsonResponse with a status message indicating the result of the updates.
"""
def updateMarks(request):
    # Extract assessment grades from the request
    assessmentGrades = json.loads(request.GET.get('assessmentMark'))
    
    # Initialize a variable to store failed updates
    failedUpdates = ''

    # Iterate through the provided assessment grades
    for assessmentInfo in assessmentGrades:
        # Get the corresponding assessment from the database
        assessment = StudentModuleAssessment.objects.get(studentModuleAssessmentID=assessmentInfo['id'])
        try:
            # Attempt to update the assessment mark with the provided value
            assessment.assessmentMark = int(assessmentInfo['mark'].replace(" ", ""))
        except:
            # Handle the case where the mark cannot be updated and record the failed update
            assessmentName = str(assessment.assessmentID.assessmentType) + " - " + str(Module.objects.get(moduleID=assessment.assessmentID.moduleID).moduleName)
            failedUpdates += assessmentName + '\n'
        assessment.save()

    if failedUpdates != '':
        return JsonResponse({'message': f'Error: The following assessments (they have not been updated): \n{failedUpdates}\n', 'status': 'fail'}, safe=False)
    else:
        return JsonResponse({'message': 'Grades have been successfully updated', 'status': 'success'}, safe=False)