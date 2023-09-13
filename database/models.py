from django.db import models


class Pathway(models.Model):
    pathwayID = models.CharField(primary_key=True,max_length=4, auto_created=False)
    pathwayName = models.CharField(max_length=100)
    pathwayLevels = models.IntegerField(default=3)
    def __str__(self):
        return self.pathwayID
    
class Lecturer(models.Model):
    lecturerID = models.IntegerField(primary_key=True, auto_created=True)
    lecturerName = models.CharField(max_length=100)
    lecturerEmail = models.EmailField()
    def __str__(self):
        return str(self.lecturerID)

class Module(models.Model):
    moduleID = models.CharField(primary_key=True ,max_length=7, auto_created=False)
    moduleName = models.CharField(max_length=100)
    moduleSemester = models.IntegerField(default=3)
    moduleDescription = models.CharField(max_length=250)
    moduleLevel = models.IntegerField(default=1)
    moduleWeight = models.IntegerField(default=20)
    def __str__(self):
        return self.moduleID
    
class Assessment(models.Model):
    assessmentID = models.IntegerField(primary_key=True, auto_created=True)
    moduleID = models.ForeignKey(Module, on_delete=models.CASCADE)
    assessmentType = models.CharField(max_length=20)
    assessmentWeight = models.FloatField(default=20)
    def __str__(self):
        return str(self.assessmentID)

class ModuleLecturer(models.Model):
    moduleLecturerID = models.IntegerField(primary_key=True, auto_created=True)
    lecturerID = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    moduleID = models.ForeignKey(Module, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.moduleLecturerID)

class ModulePathway(models.Model):
    modulePathwayID = models.IntegerField(primary_key=True, auto_created=True)
    moduleID = models.ForeignKey(Module, on_delete=models.CASCADE)
    pathwayID = models.ForeignKey(Pathway, on_delete=models.CASCADE)
    mpCore = models.BooleanField(default=True) # either optional or core
    def __str__(self):
        return str(self.modulePathwayID)
    
class Student(models.Model):
    studentID = models.IntegerField(primary_key=True, auto_created=False)
    pathwayID = models.ForeignKey(Pathway, on_delete=models.SET_NULL, null=True)
    studentCurrentLevel = models.IntegerField(default=1)
    studentCurrentSemester = models.IntegerField(default=1)
    currentPathwayMark = models.FloatField(default=100, editable=False)
    def __str__(self):
        return str(self.studentID)

class StudentModule(models.Model):
    studentModuleID = models.IntegerField(primary_key=True, auto_created=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    moduleID = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    stuModMark = models.FloatField(default=100, editable=False)
    def __str__(self):
        return str(self.studentModuleID)

class StudentInterest(models.Model):
    studentInterestID = models.IntegerField(primary_key=True, auto_created=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    interestName = models.CharField(max_length=100)
    interestImportance = models.IntegerField(default=0)
    def __str__(self):
        return str(self.studentInterestID)
    
class StudentModuleAssesment(models.Model):
    studentModuleAssesmentID =  models.IntegerField(primary_key=True, auto_created=True)
    studentModuleID = models.ForeignKey(StudentModule, on_delete=models.CASCADE)
    assessmentID = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    assesmentMark = models.FloatField(default=100)
