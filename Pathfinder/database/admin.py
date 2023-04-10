from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Module);
admin.site.register(Assessment);
admin.site.register(Lecturer);
admin.site.register(ModuleLecturer);
admin.site.register(Pathway);
admin.site.register(ModulePathway);
admin.site.register(Student);
admin.site.register(StudentInfo);
admin.site.register(StudentModule);
admin.site.register(StudentInterest);