from ..models import *

#def getCareersDataFromIndeed():


def addCareers(jobTitle, companyName, jobDescription):
    career = Career(jobTitle=jobTitle, companyName=companyName, jobDescription=jobDescription)
    career.save()

#def addCareerModuleLinks():
    #career = Career.objects.last
    #get modules with similar 


