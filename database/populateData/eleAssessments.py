from database.models import *

"""this data has already been entered into the database, to view the data run these commands:
py manage.py shell
>>>from database.models import *
>>>Assessment.objects.all()

to add this data to the database again run these commands:
py manage.py shell
>>>from database.models import *
>>>from database.populateData import eleAssessments
to add assessments
>>>eleAssessments.addAssessments()
"""

def addAssessments():
    #stage 1
    mod1001= Module.objects.get(moduleID='ECS1001')
    mod1001ass1 = Assessment(assessmentID='ecs10011', moduleID=mod1001, assessmentType='Laboratory Coursework', assessmentWeight = 100)

    mod1005= Module.objects.get(moduleID='ECS1005')
    mod1005ass1 = Assessment(assessmentID='ecs10051', moduleID=mod1005, assessmentType='Class Test', assessmentWeight = 40)
    mod1005ass2 = Assessment(assessmentID='ecs10052', moduleID=mod1005, assessmentType='Coursework', assessmentWeight = 40)
    mod1005ass3 = Assessment(assessmentID='ecs10053', moduleID=mod1005, assessmentType='Coursework', assessmentWeight = 20)

    mod1006= Module.objects.get(moduleID='ECS1006')
    mod1006ass1 = Assessment(assessmentID='ecs10061', moduleID=mod1006, assessmentType='Class Test', assessmentWeight = 5)
    mod1006ass2 = Assessment(assessmentID='ecs10062', moduleID=mod1006, assessmentType='Coursework', assessmentWeight = 10)
    mod1006ass3 = Assessment(assessmentID='ecs10063', moduleID=mod1006, assessmentType='Examination', assessmentWeight = 60)
    mod1006ass4 = Assessment(assessmentID='ecs10064', moduleID=mod1006, assessmentType='Practical', assessmentWeight = 15)
    mod1006ass5 = Assessment(assessmentID='ecs10065', moduleID=mod1006, assessmentType='Project', assessmentWeight = 10)

    mod1012= Module.objects.get(moduleID='ELE1012')
    mod1012ass1 = Assessment(assessmentID='ele10121', moduleID=mod1012, assessmentType='Continual Assessment', assessmentWeight = 50)
    mod1012ass2 = Assessment(assessmentID='ele10122', moduleID=mod1012, assessmentType='Paper', assessmentWeight = 50)

    mod1056= Module.objects.get(moduleID='ELE1056')
    mod1056ass1 = Assessment(assessmentID='ele10561', moduleID=mod1056, assessmentType='Coursework', assessmentWeight = 40)
    mod1056ass2 = Assessment(assessmentID='ele10562', moduleID=mod1056, assessmentType='Paper', assessmentWeight = 60)

    mod1057= Module.objects.get(moduleID='ELE1057')
    mod1057ass1 = Assessment(assessmentID='ele10571', moduleID=mod1057, assessmentType='Coursework', assessmentWeight = 60)
    mod1057ass2 = Assessment(assessmentID='ele10572', moduleID=mod1057, assessmentType='Class Test', assessmentWeight = 20)
    mod1057ass3 = Assessment(assessmentID='ele10573', moduleID=mod1057, assessmentType='Practical', assessmentWeight = 20)

    ##ADD stage 1 assessments
    stage1Assess_list = [mod1001ass1, mod1005ass1, mod1005ass2, mod1005ass3, mod1006ass1, mod1006ass2, mod1006ass3, mod1006ass4,
                        mod1006ass5, mod1012ass1, mod1012ass2, mod1056ass1, mod1056ass2, mod1057ass1, mod1057ass2, mod1057ass3]
    for x in stage1Assess_list:
        x.save()

#stage 2
    mod2039 = Module.objects.get(moduleID='ECS2039')
    mod2039ass1 = Assessment(assessmentID='ecs20391', moduleID=mod2039, assessmentType='Coursework', assessmentWeight = 25)
    mod2039ass2 = Assessment(assessmentID='ecs20392', moduleID=mod2039, assessmentType='Exam', assessmentWeight = 40)
    mod2039ass3 = Assessment(assessmentID='ecs20393', moduleID=mod2039, assessmentType='Laboratory', assessmentWeight = 25)
    mod2039ass4 = Assessment(assessmentID='ecs20394', moduleID=mod2039, assessmentType='Class Test', assessmentWeight = 10)

    mod2019 = Module.objects.get(moduleID='ELE2019')
    mod2019ass1 = Assessment(assessmentID='ele20191', moduleID=mod2019, assessmentType='Coursework', assessmentWeight = 10)
    mod2019ass2 = Assessment(assessmentID='ele20192', moduleID=mod2019, assessmentType='Paper', assessmentWeight = 70)
    mod2019ass3 = Assessment(assessmentID='ele20193', moduleID=mod2019, assessmentType='Practical', assessmentWeight = 20)

    mod2025= Module.objects.get(moduleID='ELE2025')
    mod2025ass1 = Assessment(assessmentID='ele20251', moduleID=mod2025, assessmentType='Laboratory Coursework', assessmentWeight = 50)
    mod2025ass2 = Assessment(assessmentID='ele20252', moduleID=mod2025, assessmentType='Design Project', assessmentWeight = 60)

    #mod2034= Module.objects.get(moduleID='ELE2034')
    #mod2034ass1 = Assessment(assessmentID='ele20341', moduleID=mod2034, assessmentType='Coursework', assessmentWeight = 100)

    mod2035= Module.objects.get(moduleID='ELE2035')
    mod2035ass1 = Assessment(assessmentID='ele20351', moduleID=mod2035, assessmentType='Class Test', assessmentWeight = 20)
    mod2035ass2 = Assessment(assessmentID='ele20352', moduleID=mod2035, assessmentType='Coursework', assessmentWeight = 20)
    mod2035ass3 = Assessment(assessmentID='ele20353', moduleID=mod2035, assessmentType='Paper', assessmentWeight = 60)

    mod2037= Module.objects.get(moduleID='ELE2037')
    mod2037ass1 = Assessment(assessmentID='ele20371', moduleID=mod2037, assessmentType='Coursework', assessmentWeight = 100)

    mod2038= Module.objects.get(moduleID='ELE2038')
    mod2038ass1 = Assessment(assessmentID='ele20381', moduleID=mod2038, assessmentType='Coursework', assessmentWeight = 40)
    mod2038ass2 = Assessment(assessmentID='ele20382', moduleID=mod2038, assessmentType='Paper', assessmentWeight = 50)
    mod2038ass3 = Assessment(assessmentID='ele20383', moduleID=mod2038, assessmentType='Project', assessmentWeight = 10)

    mod2040= Module.objects.get(moduleID='ELE2040')
    mod2040ass1 = Assessment(assessmentID='ele20401', moduleID=mod2040, assessmentType='Coursework', assessmentWeight = 10)
    mod2040ass2 = Assessment(assessmentID='ele20402', moduleID=mod2040, assessmentType='Exam', assessmentWeight = 75)
    mod2040ass3 = Assessment(assessmentID='ele20403', moduleID=mod2040, assessmentType='Laboratory Project', assessmentWeight = 15)

    mod2041= Module.objects.get(moduleID='ELE2041')
    mod2041ass1 = Assessment(assessmentID='ele20401', moduleID=mod2041, assessmentType='Coursework', assessmentWeight = 10)
    mod2041ass2 = Assessment(assessmentID='ele20402', moduleID=mod2041, assessmentType='Exam', assessmentWeight = 70)
    mod2041ass3 = Assessment(assessmentID='ele20403', moduleID=mod2041, assessmentType='Laboratory Project', assessmentWeight = 15)

    ##ADD stage 2 assessments
    stage2Assess_list = [mod2039ass1, mod2039ass2, mod2039ass3, mod2039ass4, mod2019ass1, mod2019ass2, mod2019ass3, mod2025ass1,
                         mod2025ass2, mod2035ass1, mod2035ass2, mod2035ass3, mod2037ass1, mod2038ass1, mod2038ass2,
                         mod2038ass3, mod2040ass1, mod2040ass2, mod2040ass3, mod2041ass1, mod2041ass2, mod2041ass3]
    for x in stage2Assess_list:
        x.save()

#stage 3
    mod3003= Module.objects.get(moduleID='ECS3003')
    mod3003ass1 = Assessment(assessmentID='ecs30031', moduleID=mod3003, assessmentType='Coursework', assessmentWeight = 70)
    mod3003ass2 = Assessment(assessmentID='ecs30032', moduleID=mod3003, assessmentType='Paper', assessmentWeight = 30)

    mod3001= Module.objects.get(moduleID='ELE3001')
    mod3001ass1 = Assessment(assessmentID='ele30011', moduleID=mod3001, assessmentType='Continual Assessment', assessmentWeight = 50)
    mod3001ass2 = Assessment(assessmentID='ele30012', moduleID=mod3001, assessmentType='Report', assessmentWeight = 50)

    mod3037= Module.objects.get(moduleID='ELE3037')
    mod3037ass1 = Assessment(assessmentID='ele30371', moduleID=mod3037, assessmentType='Coursework', assessmentWeight = 30)
    mod3037ass2 = Assessment(assessmentID='ele30372', moduleID=mod3037, assessmentType='Paper', assessmentWeight = 70)

    mod3039= Module.objects.get(moduleID='ELE3039')
    mod3039ass1 = Assessment(assessmentID='ele30391', moduleID=mod3039, assessmentType='Coursework', assessmentWeight = 30)
    mod3039ass2 = Assessment(assessmentID='ele30392', moduleID=mod3039, assessmentType='Paper', assessmentWeight = 70)

    mod3040= Module.objects.get(moduleID='ELE3040')
    mod3040ass1 = Assessment(assessmentID='ele30401', moduleID=mod3040, assessmentType='Class Test', assessmentWeight = 20)
    mod3040ass2 = Assessment(assessmentID='ele30402', moduleID=mod3040, assessmentType='Coursework', assessmentWeight = 20)
    mod3040ass3 = Assessment(assessmentID='ele30403', moduleID=mod3040, assessmentType='Paper', assessmentWeight = 60)

    mod3041= Module.objects.get(moduleID='ELE3041')
    mod3041ass1 = Assessment(assessmentID='ele30411', moduleID=mod3041, assessmentType='Class Test', assessmentWeight = 15)
    mod3041ass2 = Assessment(assessmentID='ele30412', moduleID=mod3041, assessmentType='Coursework', assessmentWeight = 15)
    mod3041ass3 = Assessment(assessmentID='ele30413', moduleID=mod3041, assessmentType='Paper', assessmentWeight = 70)

    mod3042= Module.objects.get(moduleID='ELE3042')
    mod3042ass1 = Assessment(assessmentID='ele30421', moduleID=mod3042, assessmentType='Coursework', assessmentWeight = 15)
    mod3042ass2 = Assessment(assessmentID='ele30422', moduleID=mod3042, assessmentType='Paper', assessmentWeight = 70)
    mod3042ass3 = Assessment(assessmentID='ele30423', moduleID=mod3042, assessmentType='Project', assessmentWeight = 15)

    mod3043= Module.objects.get(moduleID='ELE3043')
    mod3043ass1 = Assessment(assessmentID='ele30431', moduleID=mod3043, assessmentType='Critcal Review', assessmentWeight = 20)
    mod3043ass2 = Assessment(assessmentID='ele30432', moduleID=mod3043, assessmentType='Presentation', assessmentWeight = 30)
    mod3043ass3 = Assessment(assessmentID='ele30433', moduleID=mod3043, assessmentType='Report', assessmentWeight = 50)

    mod3044= Module.objects.get(moduleID='ELE3044')
    mod3044ass1 = Assessment(assessmentID='ele30441', moduleID=mod3044, assessmentType='Critical Review', assessmentWeight = 15)
    mod3044ass2 = Assessment(assessmentID='ele30442', moduleID=mod3044, assessmentType='Peer Assessment', assessmentWeight = 15)
    mod3044ass3 = Assessment(assessmentID='ele30443', moduleID=mod3044, assessmentType='Presentation', assessmentWeight = 15)
    mod3044ass4 = Assessment(assessmentID='ele30444', moduleID=mod3044, assessmentType='Report', assessmentWeight = 55)

    mod3045 = Module.objects.get(moduleID='ELE3045')
    mod3045ass1 = Assessment(assessmentID='ele30451', moduleID=mod3045, assessmentType='Coursework', assessmentWeight = 30)
    mod3045ass2 = Assessment(assessmentID='ele30452', moduleID=mod3045, assessmentType='Paper', assessmentWeight = 50)
    mod3045ass3 = Assessment(assessmentID='ele30453', moduleID=mod3045, assessmentType='Project', assessmentWeight = 20)

    mod3046 = Module.objects.get(moduleID='ELE3046')
    mod3046ass1 = Assessment(assessmentID='ele30461', moduleID=mod3046, assessmentType='Coursework', assessmentWeight = 20)
    mod3046ass2 = Assessment(assessmentID='ele30462', moduleID=mod3046, assessmentType='Laboratory Project', assessmentWeight = 15)
    mod3046ass3 = Assessment(assessmentID='ele30463', moduleID=mod3046, assessmentType='Paper', assessmentWeight = 50)
    mod3046ass4 = Assessment(assessmentID='ele30464', moduleID=mod3046, assessmentType='Project', assessmentWeight = 15)

    ##ADD stage 3 assessments
    stage3Assess_list = [mod3003ass1, mod3003ass2, mod3001ass1, mod3001ass2, mod3037ass1, mod3037ass2, mod3039ass1, mod3039ass2, mod3040ass1, mod3040ass2, mod3040ass3,
                          mod3041ass1, mod3041ass2, mod3041ass3, mod3042ass1, mod3042ass2, mod3042ass3, mod3043ass1, mod3043ass2, mod3043ass3, mod3044ass1, mod3044ass2,
                          mod3044ass3, mod3044ass4, mod3045ass1, mod3045ass2, mod3045ass3, mod3046ass1, mod3046ass2, mod3046ass3, mod3046ass4]
    for x in stage3Assess_list:
        x.save()

#stage 4
    mod4002= Module.objects.get(moduleID='ECS4002')
    mod4002ass1 = Assessment(assessmentID='ecs40021', moduleID=mod4002, assessmentType='Coursework', assessmentWeight = 15)
    mod4002ass2 = Assessment(assessmentID='ecs40022', moduleID=mod4002, assessmentType='Laboratory Project', assessmentWeight = 25)
    mod4002ass3 = Assessment(assessmentID='ecs40023', moduleID=mod4002, assessmentType='Paper', assessmentWeight = 60)

    mod4003= Module.objects.get(moduleID='ECS4003')
    mod4003ass1 = Assessment(assessmentID='ecs40031', moduleID=mod4003, assessmentType='Coursework', assessmentWeight = 100)

    mod4001= Module.objects.get(moduleID='ELE4001')
    mod4001ass1 = Assessment(assessmentID='ele40011', moduleID=mod4001, assessmentType='Coursework', assessmentWeight = 100)

    mod4009= Module.objects.get(moduleID='ELE4009')
    mod4009ass1 = Assessment(assessmentID='ele40091', moduleID=mod4009, assessmentType='Class Test', assessmentWeight = 20)
    mod4009ass2 = Assessment(assessmentID='ele40092', moduleID=mod4009, assessmentType='Paper', assessmentWeight = 60)
    mod4009ass3 = Assessment(assessmentID='ele40093', moduleID=mod4009, assessmentType='Project', assessmentWeight = 20)

    mod4023= Module.objects.get(moduleID='ELE4023')
    mod4023ass1 = Assessment(assessmentID='ele40231', moduleID=mod4023, assessmentType='Coursework', assessmentWeight = 75)
    mod4023ass2 = Assessment(assessmentID='ele40232', moduleID=mod4023, assessmentType='Class Tests', assessmentWeight = 25)

    mod4024= Module.objects.get(moduleID='ELE4024')
    mod4024ass1 = Assessment(assessmentID='ele40241', moduleID=mod4024, assessmentType='Coursework', assessmentWeight = 20)
    mod4024ass2 = Assessment(assessmentID='ele40242', moduleID=mod4024, assessmentType='Coursework', assessmentWeight = 20)
    mod4024ass3 = Assessment(assessmentID='ele40243', moduleID=mod4024, assessmentType='Exam', assessmentWeight = 60)

    mod4025= Module.objects.get(moduleID='ELE4025')
    mod4025ass1 = Assessment(assessmentID='ele40251', moduleID=mod4025, assessmentType='Coursework', assessmentWeight = 40)
    mod4025ass2 = Assessment(assessmentID='ele40252', moduleID=mod4025, assessmentType='Exam', assessmentWeight = 60)

    

    ##ADD stage 4 assessments
    stage4Assess_list = [mod4002ass1, mod4002ass2, mod4002ass3, mod4003ass1, mod4001ass1, mod4009ass1, mod4009ass2, mod4009ass3, 
                         mod4023ass1, mod4023ass2, mod4024ass1, mod4024ass2, mod4024ass3, mod4025ass1, mod4025ass2]
    for x in stage4Assess_list:
        x.save()

if __name__ == '__main__':
    addAssessments()