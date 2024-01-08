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
import random

def addLecturers():
    lecturer1 = Lecturer(lecturerName='Thomas Mckinstry', lecturerEmail='thomasMckinstry@qub.ac.uk')
    lecturer2 = Lecturer(lecturerName='Frank Alan', lecturerEmail='FrankAlan@qub.ac.uk')
    lecturer3 = Lecturer(lecturerName='Caroline Moore', lecturerEmail='carolinemoore1@qub.ac.uk')

    ##ADD ALL Lecturers
    lec_list = [lecturer1, lecturer2, lecturer3]
    for x in lec_list:
        x.save()

def addLecturesToModules():
    print(Lecturer.objects.all())
    for module in Module.objects.all():
        random_lecturer = random.randint(1, 3)
        lecturer = Lecturer.objects.get(lecturerID=random_lecturer)
        lecturer.lecturerModules.add(module)

if __name__ == '__main__':
    addLecturers()
    addLecturesToModules()