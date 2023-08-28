from database.models import *
from collections import defaultdict

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
                'studentMark': studentModules.get(moduleID=moduleId).stuModMark,
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
    studentAssessments = StudentModuleAssesment.objects.filter(studentModuleID=studentModule).select_related('assessmentID__moduleID')
    
    assessmentInfo = []
    
    # Create a list of dictionaries containing assessment information
    for student_assessment in studentAssessments:
        assessmentInfo.append({
            'name': student_assessment.assessmentID.assessmentType,
            'mark': student_assessment.assesmentMark
        })
    
    return assessmentInfo

def moduleAvg(moduleInfo):
    stageAverages = []
    
    for stageInfo in moduleInfo:
        totalWeightedMarks = 0
        totalWeighting = 0
        
        for module in stageInfo:
            totalWeightedMarks += module['studentMark'] * module['weighting']
            totalWeighting += module['weighting']
        
        stageAverage = totalWeightedMarks / totalWeighting if totalWeighting != 0 else 0
        stageAverages.append(stageAverage)
    
    return stageAverages


def assessmentAvg(student, assessment):
    pass

def leftToEarn(student, stage):
    pass


def studentInfo(user):
    moduleInfoForStudent(user, 1)
    moduleInfoForStudent(user, 1)

def gradeInfoTest(request):
    studentInDb = Student.objects.get(studentID=request.user.username)
    currentStage = studentInDb.studentCurrentLevel
    stagesInfo = moduleInfoForStudent(studentInDb, currentStage)
    
    return {
        'currentPathwayMark': 'test',
        'moduleAvg': moduleAvg(stagesInfo),
        'assesmentAvg': 'test',
        'leftToEarn': 'test',
        'stages': stagesInfo
    }

'''
    @Author: @DeanLogan
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
