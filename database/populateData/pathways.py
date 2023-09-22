from database.models import *

def addPathways():
    Pathway(pathwayID="G402", pathwayName="MEng Computer Science", pathwayLevels=4).save()
    Pathway(pathwayID="CS", pathwayName="BENG-I (International) Computer Science", pathwayLevels=3).save() # unknown pathwayID as it is not on Queens website therefore I have made it CS
    Pathway(pathwayID="G602", pathwayName="MEng Software Engineering", pathwayLevels=4).save() 
    Pathway(pathwayID="G604", pathwayName="BEng Software Engineering", pathwayLevels=3).save() 
    Pathway(pathwayID="G606", pathwayName="BEng Software Engineering with Digital Technology Partnership", pathwayLevels=3).save() 
    Pathway(pathwayID="GG45", pathwayName="BSc Computing and Information Technology", pathwayLevels=3).save() 
    Pathway(pathwayID="GN51", pathwayName="BSc Business Information Technology", pathwayLevels=3).save() 
    Pathway(pathwayID="H602", pathwayName="MEng Electrical and Electronic Engineering", pathwayLevels=4).save() 
    Pathway(pathwayID="H600", pathwayName="BEng Electrical and Electronic Engineering", pathwayLevels=3).save() 
    Pathway(pathwayID="EEE", pathwayName="BEng-I (International) Electrical & Electronic Engineering", pathwayLevels=3).save() # unknown pathwayID as it is not on Queens website therefore I have made it EEE
    Pathway(pathwayID="GH6Q", pathwayName="MEng Computer Engineering", pathwayLevels=4).save()
    Pathway(pathwayID="GH6P", pathwayName="BEng Computer Engineering", pathwayLevels=3).save()

if __name__ == '__main__':
    addPathways()
