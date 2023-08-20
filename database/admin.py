from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import *

# Register your models here.
from .models import *

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("moduleID", "moduleName", "moduleSemester", "moduleDescription", "moduleLevel", "moduleWeight")
    search_fields = ("moduleID", "moduleName")
    list_filter = ("moduleLevel", "moduleSemester")

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID}/change/'>{obj.moduleID}</a>")

    list_display = ("assessmentID", "module", "assessmentType", "assessmentWeight")
    search_fields = ("assessmentID", "assessmentType")
    list_filter = ("moduleID", )

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ("lecturerID", "lecturerName", "lecturerEmail")
    search_fields = ("lecturerID", "lecturerName")

@admin.register(ModuleLecturer)
class ModuleLecturerAdmin(admin.ModelAdmin):
    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID}/change/'>{obj.moduleID}</a>")
    def lecturer(self, obj):
        return mark_safe(f"<a href='/admin/database/lecturer/{obj.lecturerID}/change/'>{obj.lecturerID}</a>")

    list_display = ("moduleLecturerID", "lecturer", "module")
    search_fields = ("moduleLecturerID", "lecturerID", "moduleID")
    list_filter = ("moduleID", )

@admin.register(Pathway)
class PathwayAdmin(admin.ModelAdmin):
    list_display = ("pathwayID", "pathwayName", "pathwayLevels")
    search_fields = ("pathwayID", "pathwayName")
    list_filter = ("pathwayLevels", )

@admin.register(ModulePathway)
class ModulePathwayAdmin(admin.ModelAdmin):
    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID}/change/'>{obj.moduleID}</a>")
    def pathway(self, obj):
        return mark_safe(f"<a href='/admin/database/pathway/{obj.pathwayID}/change/'>{obj.pathwayID}</a>")
    
    list_display = ("modulePathwayID", "module", "pathway", "mpCore")
    search_fields = ("modulePathwayID", "moduleID", "pathwayID")
    list_filter = ("mpCore", "pathwayID", "moduleID")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def pathway(self, obj):
        return mark_safe(f"<a href='/admin/database/pathway/{obj.pathwayID}/change/'>{obj.pathwayID}</a>")

    list_display = ("studentID", "pathway", "studentCurrentLevel", "studentCurrentSemester", "currentPathwayMark")
    search_fields =  ('studentID', )

@admin.register(StudentModule)
class StudentModuleAdmin(admin.ModelAdmin):
    def student(self, obj):
        return mark_safe(f"<a href='/admin/database/student/{obj.studentID}/change/'>{obj.studentID}</a>")
    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID}/change/'>{obj.moduleID}</a>")
    
    list_display = ("studentModuleID", "student", "module", "stuModMark")
    search_fields =  ('studentModuleID', "studentID", "moduleID")
    list_filter = ("studentID", "moduleID")

@admin.register(StudentInterest)
class StudentInterestAdmin(admin.ModelAdmin):
    def student(self, obj):
        return mark_safe(f"<a href='/admin/database/student/{obj.studentID}/change/'>{obj.studentID}</a>")
    
    list_display = ("studentInterestID", "student", "interestName", "interestImportance")
    search_fields =  ('studentInterestID', "studentID", "interestName")
    list_filter = ("studentID", )

@admin.register(StudentModuleAssesment)
class StudentModuleAssesmentAdmin(admin.ModelAdmin):
    def studentModule(self, obj):
        return mark_safe(f"<a href='/admin/database/studentmodule/{obj.studentModuleID}/change/'>{obj.studentModuleID}</a>")
    
    def assessment(self, obj):
        return mark_safe(f"<a href='/admin/database/assessment/{obj.assessmentID}/change/'>{obj.assessmentID}</a>")

    list_display = ("studentModuleAssesmentID", "studentModule", "assessment", "assesmentMark")
    search_fields =  ('studentModuleAssesmentID', )
    list_filter = ("studentModuleID", "assessmentID")

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("careerID", "jobTitle", "companyName", "jobDescription")
    search_fields = ("careerID", "jobTitle", "companyName")
    list_display_links = ("jobTitle",)
    list_filter = ("companyName",)

@admin.register(CareerModule)
class CareerModuleAdmin(admin.ModelAdmin):
    def career(self, obj):
        return mark_safe(f"<a href='/admin/database/career/{obj.careerID.pk}/change/'>{obj.careerID.jobTitle} at {obj.careerID.companyName}</a>")

    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID.pk}/change/'>{obj.moduleID.moduleName}</a>")

    list_display = ("careerModuleID", "career", "module")
    search_fields = ("careerModuleID", "jobTitle", "moduleID")
    list_filter = ("careerID", "moduleID")