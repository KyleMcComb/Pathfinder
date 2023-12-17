from database.models import *

"""this data has already been entered into the database, to view the data run these commands:
py manage.py shell
>>>from database.models import *
>>>Student.objects.all()
>>>StudentInfo.objects.all()
>>>StudentInterest.objects.all()
>>>StudentModule.objects.all()
>>>StudentModuleAssessment.objects.all()        

to add this data to the database again run these commands:
py manage.py shell
>>>from database.models import *
>>>from database.populateData import students
to add students
>>>students.addSudents()
to add students info
>>>students.addSudentInfo()
to add students interest
>>>students.addSudentInterest()
to add student module linkers
>>>students.addStudentModules()
to add studentModels assessment linkers
>>>students.addStudentModuleAssessmentGrades()
"""

def addStudents():
    student1 = Student(studentID=40291577, pathwayID=Pathway.objects.get(pathwayID='G606'), studentCurrentLevel=2, studentCurrentSemester=1)
    student2 = Student(studentID=40191566, pathwayID=Pathway.objects.get(pathwayID='G400'), studentCurrentLevel=1, studentCurrentSemester=1, currentPathwayMark=7)
    student3 = Student(studentID=99999999, pathwayID=Pathway.objects.get(pathwayID='G400'), studentCurrentLevel=3, studentCurrentSemester=1)

    ##ADD ALL Students
    stu_list = [student1, student2, student3]
    for x in stu_list:
        x.save()

def addStudent40191566Info():
    stu = Student.objects.get(studentID="40191566")
    stu.save()
    stuModCSC1023 = StudentModule(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1023'), stuModMark=72)
    stuModCSC1023.save()
    savedStuMod1023 = StudentModule.objects.filter(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1023'))[0]
    stuMod1023Ass1 = StudentModuleAssessment(studentModuleID = savedStuMod1023, assessmentID = Assessment.objects.get(assessmentID='csc10231'), assessmentMark=86)
    stuMod1023Ass2 = StudentModuleAssessment(studentModuleID = savedStuMod1023, assessmentID = Assessment.objects.get(assessmentID='csc10232'), assessmentMark=60)
    stuMod1023Ass3 = StudentModuleAssessment(studentModuleID = savedStuMod1023, assessmentID = Assessment.objects.get(assessmentID='csc10233'), assessmentMark=70)
    stuMod1023Ass1.save()
    stuMod1023Ass2.save()
    stuMod1023Ass3.save()

    stuModCSC1026 = StudentModule(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1026'), stuModMark=56)
    stuModCSC1026.save()
    savedStuMod1026 = StudentModule.objects.filter(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1026'))[0]
    stuMod1026Ass1 = StudentModuleAssessment(studentModuleID = savedStuMod1026, assessmentID = Assessment.objects.get(assessmentID='csc10261'), assessmentMark=56)
    stuMod1026Ass2 = StudentModuleAssessment(studentModuleID = savedStuMod1026, assessmentID = Assessment.objects.get(assessmentID='csc10262'), assessmentMark=56)
    stuMod1026Ass1.save()
    stuMod1026Ass2.save()

    stuModCSC1033 = StudentModule(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1033'), stuModMark=76)
    stuModCSC1033.save()
    savedStuMod1033 = StudentModule.objects.filter(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1033'))[0]
    stuMod1033Ass1 = StudentModuleAssessment(studentModuleID = savedStuMod1033, assessmentID = Assessment.objects.get(assessmentID='csc10331'), assessmentMark=76)
    stuMod1033Ass1.save()

    stuModCSC1027 = StudentModule(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1027'), stuModMark=86)
    stuModCSC1027.save()
    savedStuMod1027 = StudentModule.objects.filter(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1027'))[0]
    stuMod1027Ass1 = StudentModuleAssessment(studentModuleID = savedStuMod1027, assessmentID = Assessment.objects.get(assessmentID='csc10271'), assessmentMark=86)
    stuMod1027Ass2 = StudentModuleAssessment(studentModuleID = savedStuMod1027, assessmentID = Assessment.objects.get(assessmentID='csc10272'), assessmentMark=83)
    stuMod1027Ass3 = StudentModuleAssessment(studentModuleID = savedStuMod1027, assessmentID = Assessment.objects.get(assessmentID='csc10273'), assessmentMark=89)
    stuMod1027Ass1.save()
    stuMod1027Ass2.save()
    stuMod1027Ass3.save()

    stuModCSC1028 = StudentModule(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1028'), stuModMark=67)
    stuModCSC1028.save()
    savedStuMod1028 = StudentModule.objects.filter(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1028'))[0]
    stuMod1028Ass1 = StudentModuleAssessment(studentModuleID = savedStuMod1028, assessmentID = Assessment.objects.get(assessmentID='csc10281'), assessmentMark=67)
    stuMod1028Ass1.save()
    
    stuModCSC1030 = StudentModule(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1030'), stuModMark=76)
    stuModCSC1030.save()
    savedStuMod1030 = StudentModule.objects.filter(studentID=stu, moduleID=Module.objects.get(moduleID='CSC1030'))[0]
    stuMod1030Ass1 = StudentModuleAssessment(studentModuleID = savedStuMod1030, assessmentID = Assessment.objects.get(assessmentID='csc10301'), assessmentMark=78)
    stuMod1030Ass2 = StudentModuleAssessment(studentModuleID = savedStuMod1030, assessmentID = Assessment.objects.get(assessmentID='csc10302'), assessmentMark=74)
    stuMod1030Ass1.save()
    stuMod1030Ass2.save()   


def addExtraStudent():
    student1 = Student(studentID=40294254, pathwayID=Pathway.objects.get(pathwayID='G606'), studentCurrentLevel=2, studentCurrentSemester=2, currentPathwayMark=31)

    stu_list = [student1]
    for x in stu_list:
        x.save()

    studentInterest1 = StudentInterest(studentID=Student.objects.get(studentID=40294254),interestName='Artificial Intelligence', interestImportance=1)

    studentInterest1.save()

    print("starting")

    student1ID=Student.objects.get(studentID=40294254)
    

    stu1Mod1 = StudentModule(studentModuleID=18, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1023'), stuModMark=72)
    stu1Mod2 = StudentModule(studentModuleID=19, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1026'), stuModMark=70)
    stu1Mod3 = StudentModule(studentModuleID=20, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1033'), stuModMark=70)
    stu1Mod4 = StudentModule(studentModuleID=21, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1025'), stuModMark=67)
    stu1Mod5 = StudentModule(studentModuleID=22, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1029'), stuModMark=67)
    stu1Mod6 = StudentModule(studentModuleID=23, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1030'), stuModMark=75)

    stu1Mod7 = StudentModule(studentModuleID=24, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2056'), stuModMark=94)
    stu1Mod8 = StudentModule(studentModuleID=25, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2057'), stuModMark=90)
    stu1Mod9 = StudentModule(studentModuleID=26, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2066'), stuModMark=78)
    stu1Mod10 = StudentModule(studentModuleID=27, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2054'), stuModMark=72)
    stu1Mod11 = StudentModule(studentModuleID=28, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2053'), stuModMark=56)
    stu1Mod12 = StudentModule(studentModuleID=29, studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2052'), stuModMark=84)

    stuMod_list = [stu1Mod1, stu1Mod2, stu1Mod3,stu1Mod4, stu1Mod5, stu1Mod6, stu1Mod7, stu1Mod8,
                    stu1Mod9, stu1Mod10, stu1Mod11, stu1Mod12]
    for x in stuMod_list:
        x.save()

    stu2Mod1 = StudentModule.objects.get(studentModuleID=18)
    stu2Mod2 = StudentModule.objects.get(studentModuleID=19)
    stu2Mod3 = StudentModule.objects.get(studentModuleID=20)
    stu2Mod4 = StudentModule.objects.get(studentModuleID=21)
    stu2Mod5 = StudentModule.objects.get(studentModuleID=22)
    stu2Mod6 = StudentModule.objects.get(studentModuleID=23)
    stu2Mod7 = StudentModule.objects.get(studentModuleID=24)
    stu2Mod8 = StudentModule.objects.get(studentModuleID=25)
    stu2Mod9 = StudentModule.objects.get(studentModuleID=26)
    stu2Mod10 = StudentModule.objects.get(studentModuleID=27)
    stu2Mod11 = StudentModule.objects.get(studentModuleID=28)
    stu2Mod12 = StudentModule.objects.get(studentModuleID=29)

    mod1023ass1 = Assessment.objects.get(assessmentID='csc10231')
    mod1023ass2 = Assessment.objects.get(assessmentID='csc10232')
    mod1023ass3 = Assessment.objects.get(assessmentID='csc10233')
    mod1026ass1 = Assessment.objects.get(assessmentID='csc10261')
    mod1026ass2 = Assessment.objects.get(assessmentID='csc10262')
    mod1033ass1 = Assessment.objects.get(assessmentID='csc10331')
    mod1025ass1 = Assessment.objects.get(assessmentID='csc10251')
    mod1029ass1 = Assessment.objects.get(assessmentID='csc10291')
    mod1029ass2 = Assessment.objects.get(assessmentID='csc10292')
    mod1029ass3 = Assessment.objects.get(assessmentID='csc10293')
    mod1030ass1 = Assessment.objects.get(assessmentID='csc10301')
    mod1030ass2 = Assessment.objects.get(assessmentID='csc10302')

    mod2056ass1 = Assessment.objects.get(assessmentID='csc20561')
    mod2056ass2 = Assessment.objects.get(assessmentID='csc20562')
    mod2057ass1 = Assessment.objects.get(assessmentID='csc20571')
    mod2057ass2 = Assessment.objects.get(assessmentID='csc20572')
    mod2065ass1 = Assessment.objects.get(assessmentID='csc20661')
    mod2054ass1 = Assessment.objects.get(assessmentID='csc20541')
    mod2053ass1 = Assessment.objects.get(assessmentID='csc20531')
    mod2053ass2 = Assessment.objects.get(assessmentID='csc20532')
    mod2052ass1 = Assessment.objects.get(assessmentID='csc20521')

    mod2056ass1g = StudentModuleAssessment(studentModuleID = stu2Mod7, assessmentID = mod2056ass1, assessmentMark=98)
    mod2056ass2g = StudentModuleAssessment(studentModuleID = stu2Mod7, assessmentID = mod2056ass2, assessmentMark=90)

    mod2057ass1g = StudentModuleAssessment(studentModuleID = stu2Mod8, assessmentID = mod2057ass1, assessmentMark=70)
    mod2057ass2g = StudentModuleAssessment(studentModuleID = stu2Mod8, assessmentID = mod2057ass2, assessmentMark=93)

    mod2065ass1g = StudentModuleAssessment(studentModuleID = stu2Mod9, assessmentID = mod2065ass1, assessmentMark=78)

    mod2054ass1g = StudentModuleAssessment(studentModuleID = stu2Mod10, assessmentID = mod2054ass1, assessmentMark=72)

    mod2053ass1g = StudentModuleAssessment(studentModuleID = stu2Mod11, assessmentID = mod2053ass1, assessmentMark=56)
    mod2053ass2g = StudentModuleAssessment(studentModuleID = stu2Mod11, assessmentID = mod2053ass2, assessmentMark=56)

    mod2052ass1g = StudentModuleAssessment(studentModuleID = stu2Mod12, assessmentID = mod2052ass1, assessmentMark=84)

    mod1023ass1g = StudentModuleAssessment(studentModuleID = stu2Mod1, assessmentID = mod1023ass1, assessmentMark=70)
    mod1023ass2g = StudentModuleAssessment(studentModuleID = stu2Mod1, assessmentID = mod1023ass2, assessmentMark=70)
    mod1023ass3g = StudentModuleAssessment(studentModuleID = stu2Mod1, assessmentID = mod1023ass3, assessmentMark=75)

    mod1026ass1g = StudentModuleAssessment(studentModuleID = stu2Mod2, assessmentID = mod1026ass1, assessmentMark=70)
    mod1026ass2g = StudentModuleAssessment(studentModuleID = stu2Mod2, assessmentID = mod1026ass2, assessmentMark=70)

    mod1033ass1g = StudentModuleAssessment(studentModuleID = stu2Mod3, assessmentID = mod1033ass1, assessmentMark=70)

    mod1025ass1g = StudentModuleAssessment(studentModuleID = stu2Mod4, assessmentID = mod1025ass1, assessmentMark=67)

    mod1029ass1g = StudentModuleAssessment(studentModuleID = stu2Mod5, assessmentID = mod1029ass1, assessmentMark=67)
    mod1029ass2g = StudentModuleAssessment(studentModuleID = stu2Mod5, assessmentID = mod1029ass2, assessmentMark=67)
    mod1029ass3g = StudentModuleAssessment(studentModuleID = stu2Mod5, assessmentID = mod1029ass3, assessmentMark=67)

    mod1030ass1g = StudentModuleAssessment(studentModuleID = stu2Mod6, assessmentID = mod1030ass1, assessmentMark=75)
    mod1030ass2g = StudentModuleAssessment(studentModuleID = stu2Mod6, assessmentID = mod1030ass2, assessmentMark=75)

    assessmentStudent_list = [mod2056ass1g, mod2056ass2g, mod2057ass1g,mod2057ass2g,mod2065ass1g ,mod2054ass1g ,mod2053ass1g ,mod2053ass2g ,mod2052ass1g]
    for x in assessmentStudent_list:
        x.save()

    assessmentStudent_list = [mod1023ass1g, mod1023ass2g, mod1023ass3g,mod1026ass1g,mod1026ass2g ,mod1033ass1g ,mod1025ass1g ,mod1029ass1g, mod1029ass2g, mod1029ass3g ,mod1030ass1g, mod1030ass2g]
    for x in assessmentStudent_list:
        x.save()

    print("done")
    

def addStudentInterest():
    studentInterest1 = StudentInterest(studentID=Student.objects.get(studentID=40291577), 
                                        interestName='Artificial Intelligence', interestImportance=1)
    studentInterest2 = StudentInterest(studentID=Student.objects.get(studentID=40291577), 
                                        interestName='Coding with Java', interestImportance=2)
    studentInterest3 = StudentInterest(studentID=Student.objects.get(studentID=40191566), 
                                        interestName='Artificial Intelligence & Machine Learning', 
                                        interestImportance=2)
    studentInterest4 = StudentInterest(studentID=Student.objects.get(studentID=40191566), 
                                        interestName='Sql Databases', interestImportance=1)

    ##ADD ALL Students Info
    stuInter_list = [studentInterest1, studentInterest2, studentInterest3,studentInterest4]
    for x in stuInter_list:
        x.save()

def addStudentModules():
    student1ID=Student.objects.get(studentID=40291577)
    student2ID=Student.objects.get(studentID=40191566)
    stu1Mod1 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1023'), 
                            stuModMark=77)
    stu1Mod2 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1026'), stuModMark=75)
    stu1Mod3 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1033'), stuModMark=78)
    stu1Mod4 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1027'), stuModMark=67)
    stu1Mod5 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1031'), stuModMark=81)
    stu1Mod6 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC1028'), stuModMark=76)

    stu1Mod7 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2058'), stuModMark=81)
    stu1Mod8 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2059'), stuModMark=61)
    stu1Mod9 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2063'), stuModMark=80)
    stu1Mod10 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2065'), stuModMark=70)
    stu1Mod11 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2066'), stuModMark=74)

    stu2Mod1 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1023'), stuModMark=72)
    stu2Mod2 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1026'), stuModMark=70)
    stu2Mod3 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1033'), stuModMark=70)
    stu2Mod4 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1025'), stuModMark=67)
    stu2Mod5 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1029'), stuModMark=67)
    stu2Mod6 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1030'), stuModMark=75)

    ##ADD ALL Students Modules
    stuMod_list = [stu1Mod1, stu1Mod2, stu1Mod3,stu1Mod4, stu1Mod5, stu1Mod6, stu1Mod7, stu1Mod8,
                   stu1Mod9, stu1Mod10, stu1Mod11, stu2Mod1, stu2Mod2, stu2Mod3, stu2Mod4, stu2Mod5,
                   stu2Mod6]
    for x in stuMod_list:
        x.save()

def addStudentModuleAssessmentGrades():
    stu2Mod1 = StudentModule.objects.get(studentModuleID=12)
    stu2Mod2 = StudentModule.objects.get(studentModuleID=13)
    stu2Mod3 = StudentModule.objects.get(studentModuleID=14)
    stu2Mod4 = StudentModule.objects.get(studentModuleID=15)
    stu2Mod5 = StudentModule.objects.get(studentModuleID=16)
    stu2Mod6 = StudentModule.objects.get(studentModuleID=17)

    mod1023ass1 = Assessment.objects.get(assessmentID='10231')
    mod1023ass2 = Assessment.objects.get(assessmentID='10232')
    mod1023ass3 = Assessment.objects.get(assessmentID='10233')

    mod1026ass1 = Assessment.objects.get(assessmentID='10261')
    mod1026ass2 = Assessment.objects.get(assessmentID='10262')

    mod1033ass1 = Assessment.objects.get(assessmentID='10331')
    mod1025ass1 = Assessment.objects.get(assessmentID='10251')
    mod1029ass1 = Assessment.objects.get(assessmentID='10291')
    mod1030ass1 = Assessment.objects.get(assessmentID='10301')
    mod1030ass2 = Assessment.objects.get(assessmentID='10302')

    mod1023ass1g = StudentModuleAssessment(studentModuleID = stu2Mod1, assessmentID = mod1023ass1, assesmentMark=70)
    mod1023ass2g = StudentModuleAssessment(studentModuleID = stu2Mod1, assessmentID = mod1023ass2, assesmentMark=70)
    mod1023ass3g = StudentModuleAssessment(studentModuleID = stu2Mod1, assessmentID = mod1023ass3, assesmentMark=75)

    mod1026ass1g = StudentModuleAssessment(studentModuleID = stu2Mod2, assessmentID = mod1026ass1, assesmentMark=70)
    mod1026ass2g = StudentModuleAssessment(studentModuleID = stu2Mod2, assessmentID = mod1026ass2, assesmentMark=70)

    mod1033ass1g = StudentModuleAssessment(studentModuleID = stu2Mod3, assessmentID = mod1033ass1, assesmentMark=70)

    mod1025ass1g = StudentModuleAssessment(studentModuleID = stu2Mod4, assessmentID = mod1025ass1, assesmentMark=67)

    mod1029ass1g = StudentModuleAssessment(studentModuleID = stu2Mod5, assessmentID = mod1029ass1, assesmentMark=67)

    mod1030ass1g = StudentModuleAssessment(studentModuleID = stu2Mod6, assessmentID = mod1030ass1, assesmentMark=75)
    mod1030ass2g = StudentModuleAssessment(studentModuleID = stu2Mod6, assessmentID = mod1030ass2, assesmentMark=75)

    ##ADD ALL Assessments for Student 
    assessmentStudent_list = [mod1023ass1g, mod1023ass2g, mod1023ass3g,mod1026ass1g,mod1026ass2g ,mod1033ass1g ,mod1025ass1g ,mod1029ass1g ,mod1030ass1g, mod1030ass2g]
    for x in assessmentStudent_list:
        x.save()

if __name__ == "__main__":
    addStudents()
    addStudentInterest()
    addStudentModules()
    addStudentModuleAssessmentGrades()
    addExtraStudent()
    addStudent40191566Info()