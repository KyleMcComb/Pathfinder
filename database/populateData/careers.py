from ..models import *


def addCareers(jobTitle, companyName, jobDescription):
    career = Career(jobTitle=jobTitle, companyName=companyName, jobDescription=jobDescription)
    try:
        career.save()
    except Exception as e:
        print(f"Error saving career: {e}")
    addCareerModuleRelationship(career)

### Could use chatgpt to search through and create reasoning of how the module and career link together
### Look at partial name or full name as link

def addCareerModuleRelationship(career):
    # Fetch all the Module instances from the database
    all_modules = Module.objects.all()

    for module in all_modules:
        module_name_words = module.moduleName.split()
        
        for word in module_name_words:
            if word.lower() in career.jobDescription.lower().split():
                module.careers.add(career)
                break
