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

def addLecturersToModules():
    lec1 = Lecturer.objects.get(lecturerID=1)
    lec1.lecturerModules.add(Module.objects.get(moduleID='CSC1023')),
    lec1.lecturerModules.add(Module.objects.get(moduleID='CSC1026')),
    lec1.lecturerModules.add(Module.objects.get(moduleID='CSC1033')),
    lec1.lecturerModules.add(Module.objects.get(moduleID='CSC1027')),
    lec1.lecturerModules.add(Module.objects.get(moduleID='CSC1031')),
    
    lec2 =  Lecturer.objects.get(lecturerID=2)
    lec2.lecturerModules.add(Module.objects.get(moduleID='CSC2051')),

if __name__ == '__main__':
    addLecturers()
    addLecturersToModules()