from database.models import *

"""this data has already been entered into the database, to view the data run these commands:
py manage.py shell
>>>from database.models import *
>>>Assessment.objects.all()

to add this data to the database again run these commands:
py manage.py shell
>>>from database.models import *
>>>from database.populateData import cscAssessments
to add assessments
>>>cscAssessments.addAssessments()
"""

def addAssessments():
    mod1023 = Module.objects.get(moduleID='CSC1023')
    mod1023ass1 = Assessment(assessmentID=10231, moduleID = mod1023, assessmentType = 'Class Test', assessmentWeight=30)
    mod1023ass2 = Assessment(assessmentID=10232, moduleID = mod1023, assessmentType = 'Project', assessmentWeight=30)
    mod1023ass3 = Assessment(assessmentID=10233, moduleID = mod1023, assessmentType = 'Timed exam on Computer', assessmentWeight=40)

    mod1024 = Module.objects.get(moduleID='CSC1024')
    mod1024ass1 = Assessment(assessmentID=10241, moduleID=mod1024, assessmentType='Individual Contribution', assessmentWeight = 35)
    mod1024ass2 = Assessment(assessmentID=10242, moduleID=mod1024, assessmentType='Practical Exam', assessmentWeight = 10)
    mod1024ass3 = Assessment(assessmentID=10243, moduleID=mod1024, assessmentType='Project', assessmentWeight = 35)
    mod1024ass4 = Assessment(assessmentID=10244, moduleID=mod1024, assessmentType='Class Test', assessmentWeight = 20)

    mod1025 = Module.objects.get(moduleID='CSC1025')
    mod1025ass1 = Assessment(assessmentID=10251, moduleID=mod1025, assessmentType='Continual Assessment', assessmentWeight = 100)

    mod1026 = Module.objects.get(moduleID='CSC1026')
    mod1026ass1 = Assessment(assessmentID=10261, moduleID=mod1026, assessmentType='Continual Assessment', assessmentWeight = 60)
    mod1026ass2 = Assessment(assessmentID=10262, moduleID=mod1026, assessmentType='Timed exam on Computer', assessmentWeight = 40)

    mod1027 = Module.objects.get(moduleID='CSC1027')
    mod1027ass1 = Assessment(assessmentID=10271, moduleID=mod1027, assessmentType='Class Test', assessmentWeight = 20)
    mod1027ass2 = Assessment(assessmentID=10272, moduleID=mod1027, assessmentType='Continual Assessment', assessmentWeight = 50)
    mod1027ass3 = Assessment(assessmentID=10273, moduleID=mod1027, assessmentType='Timed exam on Computer', assessmentWeight = 30)

    mod1028 = Module.objects.get(moduleID='CSC1028')
    mod1028ass1 = Assessment(assessmentID=10281, moduleID=mod1028, assessmentType='Coursework', assessmentWeight = 100)

    mod1029 = Module.objects.get(moduleID='CSC1029')
    mod1029ass1 = Assessment(assessmentID=10291, moduleID=mod1029, assessmentType='Class Test', assessmentWeight = 20)
    mod1029ass2 = Assessment(assessmentID=10292, moduleID=mod1029, assessmentType='Project', assessmentWeight = 50)
    mod1029ass3 = Assessment(assessmentID=10293, moduleID=mod1029, assessmentType='Timed exam on Computer', assessmentWeight = 30)

    mod1030 = Module.objects.get(moduleID='CSC1030')
    mod1030ass1 = Assessment(assessmentID=10301, moduleID=mod1030, assessmentType='Project', assessmentWeight = 60)
    mod1030ass2 = Assessment(assessmentID=10302, moduleID=mod1030, assessmentType='Continual Assessment', assessmentWeight = 40)

    mod1031 = Module.objects.get(moduleID='CSC1031')
    mod1031ass1 = Assessment(assessmentID=10311, moduleID=mod1031, assessmentType='Continual Assessment', assessmentWeight = 100)

    mod1032 = Module.objects.get(moduleID='CSC1032')
    mod1032ass1 = Assessment(assessmentID=10321, moduleID=mod1032, assessmentType='Continual Assessment', assessmentWeight = 100)

    mod1033 = Module.objects.get(moduleID='CSC1033')
    mod1033ass1 = Assessment(assessmentID=10331, moduleID=mod1033, assessmentType='Continual Assessment', assessmentWeight = 100)

    ##ADD stage 1 assessments
    stage1Assess_list = [mod1023ass1, mod1023ass2, mod1023ass3, mod1024ass1, mod1024ass2, 
                        mod1024ass3, mod1024ass4, mod1025ass1, mod1026ass1, mod1026ass2, mod1027ass1, mod1027ass2, 
                        mod1027ass3, mod1028ass1, mod1029ass1, mod1029ass2, mod1029ass3, mod1030ass1,
                        mod1030ass2, mod1031ass1,mod1032ass1,mod1033ass1]
    for x in stage1Assess_list:
        x.save()

#stage 2
    #mod2034 = Module.objects.get(moduleID='CS2034')
    #mod1034ass1 = Assessment(assessmentID=20341, moduleID=mod2034, assessmentType='Blank??', assessmentWeight = 0)

    mod2051 = Module.objects.get(moduleID='CSC2051')
    mod2051ass1 = Assessment(assessmentID=20511, moduleID=mod2051, assessmentType='Class Test', assessmentWeight = 60)
    mod2051ass2 = Assessment(assessmentID=20512, moduleID=mod2051, assessmentType='Project', assessmentWeight = 40)

    mod2052 = Module.objects.get(moduleID='CSC2052')
    mod2052ass1 = Assessment(assessmentID=20521, moduleID=mod2052, assessmentType='Project', assessmentWeight = 100)

    mod2053 = Module.objects.get(moduleID='CSC2053')
    mod2053ass1 = Assessment(assessmentID=20531, moduleID=mod2053, assessmentType='Project', assessmentWeight = 50)
    mod2053ass2 = Assessment(assessmentID=20532, moduleID=mod2053, assessmentType='Timed exam on Computer', assessmentWeight = 50)

    mod2054 = Module.objects.get(moduleID='CSC2054')
    mod2054ass1 = Assessment(assessmentID=20541, moduleID=mod2054, assessmentType='Project', assessmentWeight = 100)

    mod2056 = Module.objects.get(moduleID='CSC2056')
    mod2056ass1 = Assessment(assessmentID=20561, moduleID=mod2056, assessmentType='Class Test 1', assessmentWeight = 50)
    mod2056ass2 = Assessment(assessmentID=20562, moduleID=mod2056, assessmentType='Class Test 2', assessmentWeight = 50)

    mod2057 = Module.objects.get(moduleID='CSC2057')
    mod2057ass1 = Assessment(assessmentID=20571, moduleID=mod2057, assessmentType='Continual Assessment', assessmentWeight = 30)
    mod2057ass2 = Assessment(assessmentID=20572, moduleID=mod2057, assessmentType='Project', assessmentWeight = 70)

    mod2058 = Module.objects.get(moduleID='CSC2058')
    mod2058ass1 = Assessment(assessmentID=20581, moduleID=mod2058, assessmentType='Project', assessmentWeight = 100)

    mod2059 = Module.objects.get(moduleID='CSC2059')
    mod2059ass1 = Assessment(assessmentID=20591, moduleID=mod2059, assessmentType='Continual Assessment', assessmentWeight = 50)
    mod2059ass2 = Assessment(assessmentID=20592, moduleID=mod2059, assessmentType='Timed exam on Computer', assessmentWeight = 50)

    mod2060 = Module.objects.get(moduleID='CSC2060')
    mod2060ass1 = Assessment(assessmentID=20601, moduleID=mod2060, assessmentType='Continual Assessment', assessmentWeight = 40)
    mod2060ass2 = Assessment(assessmentID=20602, moduleID=mod2060, assessmentType='Paper', assessmentWeight = 60)

    mod2062 = Module.objects.get(moduleID='CSC2062')
    mod2062ass1 = Assessment(assessmentID=20621, moduleID=mod2062, assessmentType='Assignment 1', assessmentWeight = 30)
    mod2062ass2 = Assessment(assessmentID=20622, moduleID=mod2062, assessmentType='Assignment 2', assessmentWeight = 30)
    mod2062ass3 = Assessment(assessmentID=20623, moduleID=mod2062, assessmentType='Paper', assessmentWeight = 40)

    mod2063 = Module.objects.get(moduleID='CSC2063')
    mod2063ass1 = Assessment(assessmentID=20631, moduleID=mod2063, assessmentType='Project', assessmentWeight = 70)
    mod2063ass2 = Assessment(assessmentID=20632, moduleID=mod2063, assessmentType='Timed exam on Computer', assessmentWeight = 30)

    mod2065 = Module.objects.get(moduleID='CSC2065')
    mod2065ass1 = Assessment(assessmentID=20651, moduleID=mod2065, assessmentType='Continual Assessment', assessmentWeight = 100)

    mod2066 = Module.objects.get(moduleID='CSC2066')
    mod2066ass1 = Assessment(assessmentID=20661, moduleID=mod2066, assessmentType='Continual Assessment', assessmentWeight =100)

    ##ADD stage 2 assessments
    stage2Assess_list = [mod2051ass1, mod2051ass2, mod2052ass1,mod2053ass1, mod2053ass2, mod2054ass1, 
                        mod2056ass1, mod2056ass2,mod2057ass1, mod2057ass2, mod2058ass1, mod2059ass1, 
                        mod2059ass2, mod2060ass1, mod2060ass2, mod2062ass1, mod2062ass2, mod2062ass3,
                        mod2063ass1, mod2063ass2,mod2065ass1,mod2066ass1]
    for x in stage2Assess_list:
        x.save()

#stage 3
    mod3001 = Module.objects.get(moduleID='CSC3001')
    mod3001ass1 = Assessment(assessmentID=30011, moduleID=mod3001, assessmentType='Assignment', assessmentWeight = 30)
    mod3001ass2 = Assessment(assessmentID=30012, moduleID=mod3001, assessmentType='Paper', assessmentWeight = 70)

    mod3002 = Module.objects.get(moduleID='CSC3002')
    mod3002ass1 = Assessment(assessmentID=30021, moduleID=mod3002, assessmentType='Project', assessmentWeight = 100)

    mod3021 = Module.objects.get(moduleID='CSC3021')
    mod3021ass1 = Assessment(assessmentID=30211, moduleID=mod3021, assessmentType='Coursework', assessmentWeight = 100)

    mod3023 = Module.objects.get(moduleID='CSC3023')
    mod3023ass1 = Assessment(assessmentID=30231, moduleID=mod3023, assessmentType='Project', assessmentWeight = 100)

    mod3031 = Module.objects.get(moduleID='CSC3031')
    mod3031ass1 = Assessment(assessmentID=30311, moduleID=mod3031, assessmentType='Coursework', assessmentWeight = 100)

    mod3032 = Module.objects.get(moduleID='CSC3032')
    mod3032ass1 = Assessment(assessmentID=30321, moduleID=mod3032, assessmentType='Project', assessmentWeight = 100)

    mod3045 = Module.objects.get(moduleID='CSC3045')
    mod3045ass1 = Assessment(assessmentID=30451, moduleID=mod3045, assessmentType='Project', assessmentWeight = 100)

    mod3047 = Module.objects.get(moduleID='CSC3047')
    mod3047ass1 = Assessment(assessmentID=30471, moduleID=mod3047, assessmentType='Project', assessmentWeight = 100)

    mod3056 = Module.objects.get(moduleID='CSC3056')
    mod3056ass1 = Assessment(assessmentID=30561, moduleID=mod3056, assessmentType='Continual Assessment', assessmentWeight = 60)
    mod3056ass2 = Assessment(assessmentID=30562, moduleID=mod3056, assessmentType='Timed Exam on Computer', assessmentWeight = 40)

    mod3058 = Module.objects.get(moduleID='CSC3058')
    mod3058ass1 = Assessment(assessmentID=30581, moduleID=mod3058, assessmentType='Continual Assessment', assessmentWeight = 60)
    mod3058ass2 = Assessment(assessmentID=30582, moduleID=mod3058, assessmentType='Practical', assessmentWeight = 40)

    mod3059 = Module.objects.get(moduleID='CSC3059')
    mod3059ass1 = Assessment(assessmentID=30591, moduleID=mod3059, assessmentType='Paper', assessmentWeight = 40)
    mod3059ass2 = Assessment(assessmentID=30592, moduleID=mod3059, assessmentType='Practical', assessmentWeight = 60)

    mod3062 = Module.objects.get(moduleID='CSC3062')
    mod3062ass1 = Assessment(assessmentID=30621, moduleID=mod3062, assessmentType='Coursework', assessmentWeight = 100)

    mod3063 = Module.objects.get(moduleID='CSC3063')
    mod3063ass1 = Assessment(assessmentID=30631, moduleID=mod3063, assessmentType='Assignment', assessmentWeight = 40)
    mod3063ass2 = Assessment(assessmentID=30632, moduleID=mod3063, assessmentType='Practical 1', assessmentWeight = 30)
    mod3063ass3 = Assessment(assessmentID=30633, moduleID=mod3063, assessmentType='Practical 2', assessmentWeight = 30)

    mod3064 = Module.objects.get(moduleID='CSC3064')
    mod3064ass1 = Assessment(assessmentID=30641, moduleID=mod3064, assessmentType='Coursework', assessmentWeight = 100)

    mod3065 = Module.objects.get(moduleID='CSC3065')
    mod3065ass1 = Assessment(assessmentID=30651, moduleID=mod3065, assessmentType='Continual Assessment', assessmentWeight = 100)

    mod3066 = Module.objects.get(moduleID='CSC3066')
    mod3066ass1 = Assessment(assessmentID=30661, moduleID=mod3066, assessmentType='Assignment 1', assessmentWeight = 30)
    mod3066ass2 = Assessment(assessmentID=30662, moduleID=mod3066, assessmentType='Assignment 2', assessmentWeight = 30)
    mod3066ass3 = Assessment(assessmentID=30663, moduleID=mod3066, assessmentType='Paper', assessmentWeight = 40)

    mod3067 = Module.objects.get(moduleID='CSC3067')
    mod3067ass1 = Assessment(assessmentID=30671, moduleID=mod3067, assessmentType='Class Test 1', assessmentWeight = 20)
    mod3067ass2 = Assessment(assessmentID=30672, moduleID=mod3067, assessmentType='Class Test 2', assessmentWeight = 40)
    mod3067ass3 = Assessment(assessmentID=30673, moduleID=mod3067, assessmentType='Project', assessmentWeight = 40)

    mod3068 = Module.objects.get(moduleID='CSC3068')
    mod3068ass1 = Assessment(assessmentID=30681, moduleID=mod3068, assessmentType='Project', assessmentWeight = 100)

    mod3069 = Module.objects.get(moduleID='CSC3069')
    mod3069ass1 = Assessment(assessmentID=30691, moduleID=mod3069, assessmentType='Project ', assessmentWeight = 100)

    ##ADD stage 3 assessments
    stage3Assess_list = [mod3001ass1, mod3001ass2, mod3002ass1, mod3021ass1, mod3023ass1, mod3031ass1,
                         mod3032ass1, mod3045ass1, mod3047ass1, mod3056ass1, mod3056ass2, mod3058ass1,
                         mod3058ass2, mod3059ass1, mod3059ass2, mod3062ass1, mod3063ass1, mod3063ass2,
                         mod3063ass3, mod3064ass1, mod3065ass1, mod3066ass1, mod3066ass2, mod3066ass3,
                         mod3067ass1, mod3067ass2, mod3067ass3, mod3068ass1, mod3069ass1]
    for x in stage3Assess_list:
        x.save()

if __name__ == '__main__':
    addAssessments()