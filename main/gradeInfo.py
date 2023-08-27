from database.models import *

import math

def stageInfo(student, stage):
    pass

def studentModuleInfo(student, module):
    pass

def assessmentInfo(student, assessment):
    pass

def moduleAvg(student, module):
    pass

def assessmentAvg(student, assessment):
    pass

def leftToEarn(student, stage):
    pass


def studentInfo(user):
    
    studentInfo = {
        'currentStage': currentStage,
        'currentPathway': currentPathway,
        'currentPathwayMark': str(math.trunc(round(currentPathwayMark, 0))),
    }

    return studentInfo

def gradeInfo(request):
    studentInDb = Student.objects.get(studentID=request.user.username)
    currentStage = studentInDb.currentStage
    currentPathway = Pathway.objects.get(pathwayID=studentInDb.pathwayID).pathwayName
    
    
    allGradeInfo = {
        'currentPathwayMark': str(math.trunc(round(currentPathwayMark, 0))),
        'moduleAvg': str(moduleAvg),
        'assesmentAvg': str(assessmentAvg),
        'leftToEarn': str(student, stage),
        'stages': stagesInfo
    }

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
