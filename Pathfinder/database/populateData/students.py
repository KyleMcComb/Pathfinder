from database.models import *

"""this data has already been entered into the database, to view the data run these commands:
py manage.py shell
>>>from database.models import *
>>>Student.objects.all()
>>>StudentInfo.objects.all()
>>>StudentInterest.objects.all()
>>>StudentModule.objects.all()

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
"""

def addStudents():
    student1 = Student(studentID=40291577, pathwayID=Pathway.objects.get(pathwayID='G606'))
    student2 = Student(studentID=40191566, pathwayID=Pathway.objects.get(pathwayID='G400'))
    student3 = Student(studentID=99999999, pathwayID=Pathway.objects.get(pathwayID='G400'))

    ##ADD ALL Students
    stu_list = [student1, student2, student3]
    for x in stu_list:
        x.save()

def addStudentInfo():
    studentInfo1 = StudentInfo(studentID=Student.objects.get(studentID=40291577), 
                                stuInfoPassword='password1',
                                stuInfoName='John Bell', stuInfoEmail='johnBell1@qub.ac.uk',
                                stuInfoCurrentLevel=2)
    studentInfo2 = StudentInfo(studentID=Student.objects.get(studentID=40191566),
                                stuInfoPassword='password2',
                                stuInfoName='Ellie Smith', stuInfoEmail='ellieSmith3@qub.ac.uk')
    studentInfo3 = StudentInfo(studentID=Student.objects.get(studentID=99999999), 
                                stuInfoPassword='ADMIN9999',
                                stuInfoName='ADMIN', stuInfoEmail='admin@qub.ac.uk')
    ##ADD ALL Students Info
    stuInfo_list = [studentInfo1, studentInfo2, studentInfo3]
    for x in stuInfo_list:
        x.save()

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
    stu1Mod10 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='C2065'), stuModMark=70)
    stu1Mod11 = StudentModule(studentID=student1ID, moduleID=Module.objects.get(moduleID='CSC2066'), stuModMark=74)

    stu2Mod1 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1023'), stuModMark=72)
    stu2Mod2 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1026'), stuModMark=71)
    stu2Mod3 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1033'), stuModMark=70)
    stu2Mod4 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1025'), stuModMark=67)
    stu2Mod5 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1029'), stuModMark=67)
    stu2Mod6 = StudentModule(studentID=student2ID, moduleID=Module.objects.get(moduleID='CSC1030'), stuModMark=76)

    ##ADD ALL Students Modules
    stuMod_list = [stu1Mod1, stu1Mod2, stu1Mod3,stu1Mod4, stu1Mod5, stu1Mod6, stu1Mod7, stu1Mod8,
                   stu1Mod9, stu1Mod10, stu1Mod11, stu2Mod1, stu2Mod2, stu2Mod3, stu2Mod4, stu2Mod5,
                   stu2Mod6]
    for x in stuMod_list:
        x.save()