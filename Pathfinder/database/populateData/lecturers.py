from database.models import *

"""this data has already been entered into the database, to view the data run these commands:
py manage.py shell
>>>from database.models import *
>>>Lecturer.objects.all()
>>>ModuleLecturer.objects.all()

to add this data to the database again run these commands:
py manage.py shell
>>>from database.models import *
>>>from database.populateData import lecturers
to add lecturers
>>>lecturers.addLecturers()
to add lecturers to modules linkers
>>>lecturers.addLecturerModuleLinks()
"""

def addLecturers():
    lecturer1 = Lecturer(lecturerName='Thomas Mckinstry', lecturerEmail='thomasMckinstry@qub.ac.uk')
    lecturer2 = Lecturer(lecturerName='Frank Alan', lecturerEmail='FrankAlan@qub.ac.uk')
    lecturer3 = Lecturer(lecturerName='Caroline Moore', lecturerEmail='carolinemoore1@qub.ac.uk')

    ##ADD ALL Lecturers
    lec_list = [lecturer1, lecturer2, lecturer3]
    for x in lec_list:
        x.save()

def addLecturerModuleLinks():
    lec1 = Lecturer.objects.get(lecturerID=1)
    lec1Mod1023 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1023'),
                                lecturerID=lec1)
    lec1Mod1026 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1026'),
                                lecturerID=lec1)
    lec1Mod1033 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1033'),
                                lecturerID=lec1)
    lec1Mod1027 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1027'),
                                lecturerID=lec1)
    lec1Mod1031 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1031'),
                                lecturerID=lec1)
    
    lec2 =  Lecturer.objects.get(lecturerID=2)
    lec2Mod1028 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1028'),
                                lecturerID=lec2)
    lec2Mod1023 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1023'),
                                lecturerID=lec2)
    lec2Mod1025 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1025'),
                                lecturerID=lec2)
    lec2Mod1029 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1029'),
                                lecturerID=lec2)
    lec2Mod1030 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1030'),
                                lecturerID=lec2)
    
    lec3 = Lecturer.objects.get(lecturerID=3)
    lec3Mod2058 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC2058'),
                                lecturerID=lec3)
    lec3Mod2059 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC2059'),
                                lecturerID=lec3)
    lec3Mod2063 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC2063'),
                                lecturerID=lec3)
    lec3Mod2065 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC2065'),
                                lecturerID=lec3)
    lec3Mod2066 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC2066'),
                                lecturerID=lec3)
    lec3Mod1023 = ModuleLecturer(moduleID=Module.objects.get(moduleID='CSC1023'),
                                lecturerID=lec3)
    
    ##ADD ALL modules and lecturer links
    modLec_list = [lec1Mod1023, lec1Mod1026, lec1Mod1033, lec1Mod1027, lec1Mod1031,
                   lec2Mod1028, lec2Mod1023, lec2Mod1025, lec2Mod1029,lec2Mod1030,
                   lec3Mod2058, lec3Mod2059, lec3Mod2063, lec3Mod2065, lec3Mod2066,
                   lec3Mod1023]
    for x in modLec_list:
        x.save()