from .models import *
from django.contrib import admin
from django.utils.safestring import *

@admin.register(Pathway)
class PathwayAdmin(admin.ModelAdmin):
    list_display = ("pathwayID", "pathwayName", "pathwayLevels")
    search_fields = ("pathwayName", )
    list_filter = ("pathwayLevels", )

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ("lecturerID", "lecturerName", "lecturerEmail")
    search_fields = ("lecturerName", )

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("moduleID", "moduleName", "moduleSemester", "moduleDescription", "moduleLevel", "moduleWeight")
    search_fields = ("moduleName", )
    list_filter = ("moduleLevel", "moduleSemester")

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID}/change/'>{obj.moduleID}</a>")

    list_display = ("assessmentID", "module", "assessmentType", "assessmentWeight")
    search_fields = ("assessmentID", )
    list_filter = ("moduleID", )

@admin.register(ModuleLecturer)
class ModuleLecturerAdmin(admin.ModelAdmin):
    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID}/change/'>{obj.moduleID}</a>")
    def lecturer(self, obj):
        return mark_safe(f"<a href='/admin/database/lecturer/{obj.lecturerID}/change/'>{obj.lecturerID}</a>")

    list_display = ("moduleLecturerID", "lecturer", "module")
    search_fields = ("lecturer", )
    list_filter = ("moduleID", )

@admin.register(ModulePathway)
class ModulePathwayAdmin(admin.ModelAdmin):
    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID}/change/'>{obj.moduleID}</a>")
    def pathway(self, obj):
        return mark_safe(f"<a href='/admin/database/pathway/{obj.pathwayID}/change/'>{obj.pathwayID}</a>")
    
    list_display = ("modulePathwayID", "module", "pathway", "mpCore")
    search_fields = ("modulePathwayID", )
    list_filter = ("mpCore", "pathwayID", "moduleID")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def pathway(self, obj):
        return mark_safe(f"<a href='/admin/database/pathway/{obj.pathwayID}/change/'>{obj.pathwayID}</a>")

    list_display = ("studentID", "pathway", "studentCurrentLevel", "studentCurrentSemester", "currentPathwayMark")
    search_fields =  ('studentID', )

    readonly_fields=('currentPathwayMark',)

@admin.register(StudentModule)
class StudentModuleAdmin(admin.ModelAdmin):
    def student(self, obj):
        return mark_safe(f"<a href='/admin/database/student/{obj.studentID}/change/'>{obj.studentID}</a>")
    def module(self, obj):
        return mark_safe(f"<a href='/admin/database/module/{obj.moduleID}/change/'>{obj.moduleID}</a>")
    
    list_display = ("studentModuleID", "student", "module", "stuModMark")
    search_fields =  ('studentModuleID', )
    list_filter = ("studentID", "moduleID")

    readonly_fields=('stuModMark',)

@admin.register(StudentInterest)
class StudentInterestAdmin(admin.ModelAdmin):
    def student(self, obj):
        return mark_safe(f"<a href='/admin/database/student/{obj.studentID}/change/'>{obj.studentID}</a>")
    
    list_display = ("studentInterestID", "student", "interestName", "interestImportance")
    search_fields =  ('studentInterestID', )
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

admin.site.index_template = 'admin/extendedAdminPage.html'  # Path to custom template for admin index page