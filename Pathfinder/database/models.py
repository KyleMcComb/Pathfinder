from django.db import models

# Create your models here.
class Modules(models.Model):
    moduleID = models.CharField(max_length=7)
    moduleName = models.CharField(max_length=200)
    duration = models.IntegerField(default=3)
    def __str__(self):
        return self.moduleID

class Courses(models.Model):
    #id - auto gen
    courseName = models.CharField(max_length=200)
    duration = models.IntegerField(default=3)

class ModuleCourse(models.Model):
    #id - auto gen
    moduleRef = models.ForeignKey(Modules, on_delete=models.DO_NOTHING)
    courseRef = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    level = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)

