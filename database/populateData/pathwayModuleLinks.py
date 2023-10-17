from database.models import *
############################ Module to Pathway links #########################

def addPathwayModuleLinks():
    #### PathwayG402 Link tables
    #level 1
    pathwayG402 = Pathway.objects.get(pathwayID='G402')
    module1023PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1023'))
    module1026PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1026'))
    module1033PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1033'))
    module1027PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1027')) #with SSD
    module1025PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1025')) #without SSD
    module1029PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1029')) #without SSD

    module1028PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1028'), mpCore=False)
    module1030PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1030'), mpCore=False)
    module1031PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1031'), mpCore=False)
    module1032PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC1032'), mpCore=False)

    #level 2
    module2058PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC2058'))
    module2059PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC2059'))
    module2060PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC2060'))
    module2065PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC2065'))

    module2056PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)
    module2066PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC2066'), mpCore=False)

    #level 3
    module3001PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3001'))

    module3021PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3021'), mpCore=False)
    module3056PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3056'), mpCore=False)
    module3058PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3058'), mpCore=False)
    module3059PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3059'), mpCore=False)
    module3064PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3064'), mpCore=False)
    module3065PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3065'), mpCore=False)
    module3066PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3066'), mpCore=False)
    module3067PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC3067'), mpCore=False)

    #level 4
    module4006PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC4006'))
    module4008PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC4008'))

    moduleECS4003PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='ECS4003'), mpCore=False)
    module4003PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC4003'), mpCore=False)
    module4009PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC4009'), mpCore=False)
    module4010PathwayG402 = ModulePathway(pathwayID = pathwayG402, moduleID=Module.objects.get(moduleID='CSC4010'), mpCore=False)

    #### PathwayCS Link tables
    #level 1 - undefined in the given doc, therefore these modules are assumed for now
    pathwayICS = Pathway.objects.get(pathwayID='ICS')
    module1023PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1023'))
    module1026PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1026'))
    module1033PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1033'))
    module1027PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1027')) #with SSD
    module1025PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1025')) #without SSD
    module1029PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1029')) #without SSD
    module1028PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1028'), mpCore=False)
    module1030PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1030'), mpCore=False)
    module1031PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1031'), mpCore=False)
    module1032PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC1032'), mpCore=False)
    
    #level 2
    module2058PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC2058'))
    module2059PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC2059'))
    module2060PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC2060'))
    module2065PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC2065'))
    module2056PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)
    module2066PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC2066'), mpCore=False)

    #level 3
    module3002PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3002'))
    module3001PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3001'), mpCore=False)
    module3021PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3021'), mpCore=False)
    module3056PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3056'), mpCore=False)
    module3058PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3058'), mpCore=False)
    module3059PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3059'), mpCore=False)
    module3064PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3064'), mpCore=False)
    module3065PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3065'), mpCore=False)
    module3066PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3066'), mpCore=False)
    module3067PathwayICS = ModulePathway(pathwayID = pathwayICS, moduleID=Module.objects.get(moduleID='CSC3067'), mpCore=False)


    #PathwayG400 Link tables
    pathwayG400 = Pathway.objects.get(pathwayID='G400')
    #level 1
    module1023PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1023'))
    module1026PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1026'))
    module1033PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1033'))
    module1027PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1027')) #with SSD
    module1025PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1025')) #without SSD
    module1029PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1029')) #without SSD

    module1028PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1028'), mpCore=False)
    module1030PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1030'), mpCore=False)
    module1031PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1031'), mpCore=False)
    module1032PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC1032'), mpCore=False)

    #level 2
    module2058PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC2058'))
    module2059PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC2059'))
    module2060PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC2060'))
    module2065PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC2065'))

    module2056PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)
    module2066PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC2066'), mpCore=False)

    #level 3
    module3002PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3002'))

    module3001PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3001'), mpCore=False)
    module3021PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3021'), mpCore=False)
    module3056PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3056'), mpCore=False)
    module3058PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3058'), mpCore=False)
    module3059PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3059'), mpCore=False)
    module3064PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3064'), mpCore=False)
    module3065PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3065'), mpCore=False)
    module3066PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3066'), mpCore=False)
    module3067PathwayG400 = ModulePathway(pathwayID = pathwayG400, moduleID=Module.objects.get(moduleID='CSC3067'), mpCore=False)

    #PathwayG602 linker tables
    pathwayG602 = Pathway.objects.get(pathwayID='G602')
    #level 1
    module1023PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1023'))
    module1026PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1026'))
    module1033PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1033'))
    module1027PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1027'))
    module1025PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1025'))
    module1029PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1029'))

    module1028PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1028'), mpCore=False)
    module1030PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1030'), mpCore=False)
    module1031PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1031'), mpCore=False)
    module1032PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC1032'), mpCore=False)

    #level 2
    module2058PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC2058'))
    module2059PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC2059'))
    module2063PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC2063'))
    module2065PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC2065'))

    module2056PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)
    module2066PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC2066'), mpCore=False)

    #level 3
    module3021PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3021'), mpCore=False)
    module3031PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3031'), mpCore=False)
    module3045PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3045'), mpCore=False)   
    module3056PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3056'), mpCore=False)
    module3058PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3058'), mpCore=False)
    module3059PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3059'), mpCore=False)
    module3063PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3063'), mpCore=False)
    module3064PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3064'), mpCore=False)
    module3065PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3065'), mpCore=False)
    module3067PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC3067'), mpCore=False)

    #level 4
    module4006PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC4006'))
    module4008PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC4008'))

    moduleECS4003PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='ECS4003'), mpCore=False)
    module4003PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC4003'), mpCore=False)
    module4009PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC4009'), mpCore=False)
    module4010PathwayG602 = ModulePathway(pathwayID = pathwayG602, moduleID=Module.objects.get(moduleID='CSC4010'), mpCore=False)



    #Pathway g604 linker tables
    pathwayG604 = Pathway.objects.get(pathwayID='G604')
    #level 1
    module1023PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1023'))
    module1026PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1026'))
    module1033PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1033'))
    module1027PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1027'))
    module1025PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1025'))
    module1029PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1029'))

    module1028PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1028'), mpCore=False)
    module1030PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1030'), mpCore=False)
    module1031PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1031'), mpCore=False)
    module1032PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC1032'), mpCore=False)

    #level 2
    module2058PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC2058'))
    module2059PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC2059'))
    module2063PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC2063'))
    module2065PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC2065'))

    module2056PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)
    module2066PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC2066'), mpCore=False)

    #level 3
    module3032PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3032'))
    module3045PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3045'))

    module3021PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3021'), mpCore=False)
    module3031PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3031'), mpCore=False)
    module3056PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3056'), mpCore=False)
    module3058PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3058'), mpCore=False)
    module3059PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3059'), mpCore=False)
    module3063PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3063'), mpCore=False)
    module3064PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3064'), mpCore=False)
    module3065PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3065'), mpCore=False)
    module3067PathwayG604 = ModulePathway(pathwayID = pathwayG604, moduleID=Module.objects.get(moduleID='CSC3067'), mpCore=False)

    #PathwayG606 linker tables
    pathwayG606 = Pathway.objects.get(pathwayID='G606')
    #level 1
    module1023PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1023'))
    module1026PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1026'))
    module1033PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1033'))
    module1027PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1027'))
    module1025PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1025'))
    module1029PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1029'))

    module1028PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1028'), mpCore=False)
    module1030PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1030'), mpCore=False)
    module1031PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1031'), mpCore=False)
    module1032PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC1032'), mpCore=False)

    #level 2
    module2058PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC2058'))
    module2059PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC2059'))
    module2063PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC2063'))
    module2065PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC2065'))

    module2056PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)
    module2066PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC2066'), mpCore=False)

    #level3
    module3068PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3068'))

    module3031PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3031'), mpCore=False)
    module3056PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3056'), mpCore=False)
    module3059PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3059'), mpCore=False)
    module3063PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3063'), mpCore=False)
    module3064PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3064'), mpCore=False)

    #level4
    module3069PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3069'))

    module3021PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3021'), mpCore=False)
    module3045PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3045'), mpCore=False)
    module3058PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3058'), mpCore=False)
    module3065PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3065'), mpCore=False)
    module3067PathwayG606 = ModulePathway(pathwayID = pathwayG606, moduleID=Module.objects.get(moduleID='CSC3067'), mpCore=False)

    #PathwayGG45 linker Tables
    pathwayGG45 = Pathway.objects.get(pathwayID='GG45')
    #level 1
    module1023PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1023'))
    module1026PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1026'))
    module1033PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1033'))
    module1027PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1027'))
    module1025PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1025'))
    module1029PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1029'))

    module1028PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1028'), mpCore=False)
    module1030PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1030'), mpCore=False)
    module1031PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1031'), mpCore=False)
    module1032PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC1032'), mpCore=False)

    #level 2
    module2051PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC2051'))
    module2052PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC2052'))
    module2023PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC2053'))
    module2054PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC2054'))
    module2065PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC2065'))

    module2056PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)
    module2066PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC2066'), mpCore=False)

    #level 3
    module3047PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC3047'))
    module3045PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC3045'))
    module3062PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC3062'))

    module3031PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC3031'), mpCore=False)
    module3056PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC3056'), mpCore=False)
    module3064PathwayGG45 = ModulePathway(pathwayID = pathwayGG45, moduleID=Module.objects.get(moduleID='CSC3064'), mpCore=False)

    ####Pathway H602 linker Tables
    pathwayH602 = Pathway.objects.get(pathwayID='H602')
    #level 1
    module1012PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE1012'))
    module1056PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE1056'))
    module1057PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE1057'))
    module1001PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ECS1001'))
    module1005PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ECS1005'))
    module1006PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ECS1006'))

    #Level2
    module2025PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE2025'))
    module2035PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE2035'))
    module2037PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE2037'))

    module2019PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE2019'), mpCore=False)
    module2038PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE2038'), mpCore=False)
    module2039PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ECS2039'), mpCore=False)
    module2040PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE2040'), mpCore=False)
    module2041PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE2041'), mpCore=False)

    #level3
    module3044PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE3044'))

    module3003PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ECS3003'), mpCore=False)
    module3037PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE3037'), mpCore=False)
    module3039PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE3039'), mpCore=False)
    module3040PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE3040'), mpCore=False)
    module3041PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE3041'), mpCore=False)
    module3042PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE3042'), mpCore=False)
    module3045PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE3045'), mpCore=False)
    module3046PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE3046'), mpCore=False)
    #has a music module MUS3006

    #level4
    module4001PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE4001'))

    module4002PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ECS4002'), mpCore=False)
    module4003PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ECS4003'), mpCore=False)
    module4009PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE4009'), mpCore=False)
    module4023PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE4023'), mpCore=False)
    module4024PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE4024'), mpCore=False)
    module4025PathwayH602 = ModulePathway(pathwayID = pathwayH602, moduleID=Module.objects.get(moduleID='ELE4025'), mpCore=False)

    ####H600Pathway linker Tables
    pathwayH600 = Pathway.objects.get(pathwayID='H600')
    #level1
    module1012PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE1012'))
    module1056PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE1056'))
    module1057PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE1057'))
    module1001PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ECS1001'))
    module1005PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ECS1005'))
    module1006PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ECS1006'))

    #level2
    module2025PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE2025'))
    module2035PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE2035'))
    module2037PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE2037'))
    module2037PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE2037'))

    module2019PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE2019'), mpCore=False)
    module2038PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE2038'), mpCore=False)
    module2039PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ECS2039'), mpCore=False)
    module2040PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE2040'), mpCore=False)
    module2041PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE2041'), mpCore=False)

    #level3
    module3001PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3001'))
    module3043PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3043'))

    module3003PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ECS3003'), mpCore=False)
    module3037PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3037'), mpCore=False)
    module3039PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3039'), mpCore=False)
    module3040PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3040'), mpCore=False)
    module3041PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3041'), mpCore=False)
    module3042PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3042'), mpCore=False)
    module3045PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3045'), mpCore=False)
    module3046PathwayH600 = ModulePathway(pathwayID = pathwayH600, moduleID=Module.objects.get(moduleID='ELE3046'), mpCore=False)
    #has a music module MUS3006

    ####IEEEPathway linker Tables
    pathwayIEEE = Pathway.objects.get(pathwayID='IEEE')
    #level 1 - assumed modules as they are not defined in doc
    module1012PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE1012'))
    module1056PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE1056'))
    module1057PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE1057'))
    module1001PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ECS1001'))
    module1005PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ECS1005'))
    module1006PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ECS1006'))

    #level 2
    module2025PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE2025'))
    module2035PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE2035'))
    module2037PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE2037'))

    module2019PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE2019'), mpCore=False)
    module2038PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE2038'), mpCore=False)
    module2039PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ECS2039'), mpCore=False)
    module2040PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE2040'), mpCore=False)
    module2041PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE2041'), mpCore=False)

    #level 3
    module3001PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3001'))
    module3043PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3043'))

    module3003PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ECS3003'), mpCore=False)
    module3037PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3037'), mpCore=False)
    module3039PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3039'), mpCore=False)
    module3040PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3040'), mpCore=False)
    module3041PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3041'), mpCore=False)
    module3042PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3042'), mpCore=False)
    module3045PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3045'), mpCore=False)
    module3046PathwayIEEE = ModulePathway(pathwayID = pathwayIEEE, moduleID=Module.objects.get(moduleID='ELE3046'), mpCore=False)
    #has a music module MUS3006

    ####PathwayGH6Q linker Tables
    pathwayGH6Q = Pathway.objects.get(pathwayID='GH6Q')
    #level 1
    module1029PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC1029'))
    module1012PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE1012'))
    module1001PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ECS1001'))
    module1012PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE1012'))
    module1005PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ECS1005'))
    module1006PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ECS1006'))
    module1057PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE1057'))

    #level2
    module2025PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE2025'))
    module2035PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE2035'))
    module2037PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE2037'))
    module2059PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC2059'))

    module2038PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE2038'), mpCore=False)
    module2039PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ECS2039'), mpCore=False)
    module2040PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE2040'), mpCore=False)
    module2041PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE2041'), mpCore=False)
    module2056PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)

    #level3
    module3044PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE3044'))

    module3021PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC3021'), mpCore=False)
    module3059PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC3059'), mpCore=False)
    module3066PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC3066'), mpCore=False)
    module3067PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC3067'), mpCore=False)
    module3003PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ECS3003'), mpCore=False)
    module3040PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE3040'), mpCore=False)
    module3041PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE3041'), mpCore=False)
    module3042PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE3042'), mpCore=False)
    module3046PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE3046'), mpCore=False)

    #level4
    module4001PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE4001'))
    
    module4003PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC4003'), mpCore=False)
    module4009PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC4009'), mpCore=False)
    module4010PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='CSC4010'), mpCore=False)
    module4002PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ECS4002'), mpCore=False)
    module4003PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ECS4003'), mpCore=False)
    module4009PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE4009'), mpCore=False)
    module4023PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE4023'), mpCore=False)
    module4024PathwayGH6Q = ModulePathway(pathwayID = pathwayGH6Q, moduleID=Module.objects.get(moduleID='ELE4024'), mpCore=False)


    ####PathwayGH6P linker Tables
    pathwayGH6P = Pathway.objects.get(pathwayID='GH6P')
    #level 1
    module1029PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='CSC1029'))
    module1012PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE1012'))
    module1001PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ECS1001'))
    module1012PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE1012'))
    module1005PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ECS1005'))
    module1006PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ECS1006'))
    module1057PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE1057'))

    #level2
    module2025PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE2025'))
    module2035PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE2035'))
    module2037PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE2037'))
    module2059PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='CSC2059'))

    module2038PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE2038'), mpCore=False)
    module2039PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ECS2039'), mpCore=False)
    module2040PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE2040'), mpCore=False)
    module2041PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE2041'), mpCore=False)
    module2056PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='CSC2056'), mpCore=False)
    module2062PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='CSC2062'), mpCore=False)

    #Level 3
    module3001PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE3001'))
    module3043PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE3043'))

    module3021PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='CSC3021'), mpCore=False)
    module3059PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='CSC3059'), mpCore=False)
    module3066PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='CSC3066'), mpCore=False)
    module3067PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='CSC3067'), mpCore=False)
    module3003PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ECS3003'), mpCore=False)
    module3040PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE3040'), mpCore=False)
    module3041PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE3041'), mpCore=False)
    module3042PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE3042'), mpCore=False)
    module3046PathwayGH6P = ModulePathway(pathwayID = pathwayGH6P, moduleID=Module.objects.get(moduleID='ELE3046'), mpCore=False)


    ##ADD level 1 Module links to G402
    G402Mod1_list = [module1023PathwayG402, module1026PathwayG402, module1033PathwayG402,
                module1027PathwayG402, module1025PathwayG402, module1029PathwayG402,
                module1028PathwayG402, module1030PathwayG402, module1031PathwayG402,
                module1032PathwayG402]
    for z in G402Mod1_list:
        z.save()

    ##ADD level 2 Module links to G402
    G402Mod2_list = [module2058PathwayG402, module2059PathwayG402, module2060PathwayG402,
                    module2065PathwayG402, module2056PathwayG402, module2062PathwayG402,
                    module2066PathwayG402]
    for z in G402Mod2_list:
        z.save()

    ##ADD level 3 Module links to G402
    G402Mod3_list = [module3001PathwayG402, module3021PathwayG402, module3056PathwayG402,
                    module3058PathwayG402, module3059PathwayG402, module3064PathwayG402,
                    module3065PathwayG402, module3066PathwayG402, module3067PathwayG402]
    for z in G402Mod3_list:
        z.save()

    ##ADD level 4 Module links to G402
    G402Mod4_list = [module4006PathwayG402, module4008PathwayG402, moduleECS4003PathwayG402,
                    module4003PathwayG402, module4009PathwayG402, module4010PathwayG402]
    for z in G402Mod4_list:
        z.save()

    ###Add level 1 Module links to ICS
    ICSMod1_list = [module1023PathwayICS,
        module1026PathwayICS,
        module1033PathwayICS,
        module1027PathwayICS,
        module1025PathwayICS,
        module1029PathwayICS,
        module1028PathwayICS,
        module1030PathwayICS,
        module1031PathwayICS,
        module1032PathwayICS
    ]
    for z in ICSMod1_list:
        z.save()
    
    ##add level 2 Module links to ICS
    ICSMod2_list = [module2058PathwayICS,
    module2059PathwayICS,
    module2060PathwayICS,
    module2065PathwayICS,
    module2056PathwayICS,
    module2062PathwayICS,
    module2066PathwayICS]

    for z in ICSMod2_list:
        z.save()

    ##add level 3 Module links to ICS
    ICSMod3_list = [module3002PathwayICS,
    module3001PathwayICS,
    module3021PathwayICS,
    module3056PathwayICS,
    module3058PathwayICS,
    module3059PathwayICS,
    module3064PathwayICS,
    module3065PathwayICS,
    module3066PathwayICS,
    module3067PathwayICS
    ]
    for z in ICSMod3_list:
        z.save()
    
                    

    ##ADD level 1 Module links to G400
    G400Mod1_list = [module1023PathwayG400, module1026PathwayG400, module1033PathwayG400,
                    module1027PathwayG400, module1025PathwayG400, module1029PathwayG400,
                    module1028PathwayG400, module1030PathwayG400, module1031PathwayG400,
                    module1032PathwayG400]
    for z in G400Mod1_list:
        z.save()

    ##ADD level 2 Module links to G400
    G400Mod2_list = [module2058PathwayG400, module2059PathwayG400, module2060PathwayG400,
                    module2065PathwayG400, module2056PathwayG400, module2062PathwayG400,
                    module2066PathwayG400]
    for z in G400Mod2_list:
        z.save()

    ##ADD level 3 Module links to G400
    G400Mod3_list = [module3002PathwayG400, module3001PathwayG400, module3021PathwayG400,
                    module3056PathwayG400, module3058PathwayG400, module3059PathwayG400, 
                    module3064PathwayG400, module3065PathwayG400, module3066PathwayG400, 
                    module3067PathwayG400]
    for z in G400Mod3_list:
        z.save()

    ##ADD level 1 Module links to G602
    G602Mod1_list = [module1023PathwayG602, module1026PathwayG602, module1033PathwayG602,
                    module1027PathwayG602, module1025PathwayG602, module1029PathwayG602,
                    module1028PathwayG602, module1030PathwayG602, module1031PathwayG602,
                    module1032PathwayG602]
    for z in G602Mod1_list:
        z.save()

    ##ADD level 2 Module links to G602
    G602Mod2_list = [module2058PathwayG602, module2059PathwayG602, module2063PathwayG602,
                    module2065PathwayG602, module2056PathwayG602, module2062PathwayG602,
                    module2066PathwayG602]
    for z in G602Mod2_list:
        z.save()

    ##ADD level 3 Module links to G602
    G602Mod3_list = [module3021PathwayG602, module3031PathwayG602, module3045PathwayG602,
                    module3056PathwayG602, module3058PathwayG602, module3059PathwayG602, 
                    module3063PathwayG602, module3064PathwayG602, module3065PathwayG602, 
                    module3067PathwayG602]
    for z in G602Mod3_list:
        z.save()

    ##ADD level 4 Module links to G602
    G602Mod4_list = [module4006PathwayG602, module4008PathwayG602, moduleECS4003PathwayG602,
                    module4003PathwayG602, module4009PathwayG602, module4010PathwayG602]
    for z in G602Mod4_list:
        z.save()

    ##ADD level 1 Module links to G604
    G604Mod1_list = [module1023PathwayG604, module1026PathwayG604, module1033PathwayG604,
                    module1027PathwayG604, module1025PathwayG604, module1029PathwayG604,
                    module1028PathwayG604, module1030PathwayG604, module1031PathwayG604,
                    module1032PathwayG604]
    for z in G604Mod1_list:
        z.save()

    ##ADD level 2 Module links to G604
    G604Mod2_list = [module2058PathwayG604, module2059PathwayG604, module2063PathwayG604,
                    module2065PathwayG604, module2056PathwayG604, module2062PathwayG604,
                    module2066PathwayG604]
    for z in G604Mod2_list:
        z.save()

    ##ADD level 3 Module links to G604
    G604Mod3_list = [module3032PathwayG604, module3045PathwayG604, module3021PathwayG604, 
                    module3031PathwayG604, module3056PathwayG604, module3058PathwayG604, 
                    module3059PathwayG604, module3063PathwayG604, module3064PathwayG604, 
                    module3065PathwayG604, module3067PathwayG604]
    for z in G604Mod3_list:
        z.save()

    ##ADD level 1 Module links to G606
    G606Mod1_list = [module1023PathwayG606, module1026PathwayG606, module1033PathwayG606,
                    module1027PathwayG606, module1025PathwayG606, module1029PathwayG606,
                    module1028PathwayG606, module1030PathwayG606, module1031PathwayG606,
                    module1032PathwayG606]
    for z in G606Mod1_list:
        z.save()

    ##ADD level 2 Module links to G606
    G606Mod2_list = [module2058PathwayG606, module2059PathwayG606, module2063PathwayG606,
                    module2065PathwayG606, module2056PathwayG606, module2062PathwayG606,
                    module2066PathwayG606]
    for z in G606Mod2_list:
        z.save()

    ##ADD level 3 Module links to G606
    G606Mod3_list = [module3068PathwayG606, module3031PathwayG606, module3056PathwayG606, 
                    module3059PathwayG606, module3063PathwayG606, module3064PathwayG606] 
    for z in G606Mod3_list:
        z.save()

    ##ADD level 4 Module links to G606
    G606Mod4_list = [module3069PathwayG606, module3045PathwayG606, module3021PathwayG606, 
                    module3058PathwayG606, module3065PathwayG606, module3067PathwayG606]
    for z in G606Mod4_list:
        z.save()

    ##ADD level 1 module links to GG45
    GG45Mod1_list = [module1023PathwayGG45, module1026PathwayGG45, module1033PathwayGG45,
                    module1027PathwayGG45, module1025PathwayGG45, module1029PathwayGG45,
                    module1028PathwayGG45, module1030PathwayGG45, module1031PathwayGG45,
                    module1032PathwayGG45]
    for z in GG45Mod1_list:
        z.save()

    ##ADD level 2 Module links to GG45
    GG45Mod2_list = [module2051PathwayGG45, module2052PathwayGG45, module2023PathwayGG45,
                    module2054PathwayGG45, module2065PathwayGG45, module2056PathwayGG45, 
                    module2062PathwayGG45, module2066PathwayGG45]
    for z in GG45Mod2_list:
        z.save()

    ##ADD level 3 Module links to GG45
    GG45Mod3_list = [module3047PathwayGG45, module3045PathwayGG45, module3062PathwayGG45, 
                    module3031PathwayGG45, module3056PathwayGG45, module3064PathwayGG45]
    for z in GG45Mod3_list:
        z.save()

    ##Add level 1 Module links to H602
    H602Mod1_list = [
    module1012PathwayH602,
    module1056PathwayH602,
    module1057PathwayH602,
    module1001PathwayH602,
    module1005PathwayH602,
    module1006PathwayH602
    ]
    for z in H602Mod1_list:
        z.save()

    ##Add level 2 Module links to H602
    H602Mod2_list = [   module2025PathwayH602,
    module2035PathwayH602,
    module2037PathwayH602,
    module2019PathwayH602,
    module2038PathwayH602,
    module2039PathwayH602,
    module2040PathwayH602,
    module2041PathwayH602]
    for z in H602Mod2_list:
        z.save()

    ##Add level 3 Module links to H602
    H602Mod3_list = [module3044PathwayH602,
    module3003PathwayH602,
    module3037PathwayH602,
    module3039PathwayH602,
    module3040PathwayH602,
    module3041PathwayH602,
    module3042PathwayH602,
    module3045PathwayH602,
    module3046PathwayH602]
    for z in H602Mod3_list:
        z.save()

    ##Add level 4 Module links to H602
    H602Mod4_list = [module4001PathwayH602,
    module4002PathwayH602,
    module4003PathwayH602,
    module4009PathwayH602,
    module4023PathwayH602,
    module4024PathwayH602,
    module4025PathwayH602]
    for z in H602Mod4_list:
        z.save()
    
    ##Add level 1 Module links to H600
    H600Mod1_list = [
    module1012PathwayH600,
    module1056PathwayH600,
    module1057PathwayH600,
    module1001PathwayH600,
    module1005PathwayH600,
    module1006PathwayH600
    ]
    for z in H600Mod1_list:
        z.save()  # save to database

    ##Add level 2 Module links to H600
    H600Mod2_list = [
        module2025PathwayH600,
        module2035PathwayH600,
        module2037PathwayH600,
        module2019PathwayH600,
        module2038PathwayH600,
        module2039PathwayH600,
        module2040PathwayH600,
        module2041PathwayH600
    ]
    for z in H600Mod2_list:
        z.save()  # save to database
    
    ##Add level 3 Module links to H600
    H600Mod3_list = [
        module3001PathwayH600,
        module3043PathwayH600,
        module3003PathwayH600,
        module3037PathwayH600,
        module3039PathwayH600,
        module3040PathwayH600,
        module3041PathwayH600,
        module3042PathwayH600,
        module3045PathwayH600,
        module3046PathwayH600
    ]
    for z in H600Mod3_list:
        z.save()  # save to database
    
    ##Add level 1 Module links to IEEE
    IEEEMod1_list = [module1012PathwayIEEE,
    module1056PathwayIEEE,
    module1057PathwayIEEE,
    module1001PathwayIEEE,
    module1005PathwayIEEE,
    module1006PathwayIEEE]
    for z in IEEEMod1_list:
        z.save()  # save to database

    ##Add level 2 Module links to IEEE
    IEEEMod2_list = [module2025PathwayIEEE,
        module2035PathwayIEEE,
        module2037PathwayIEEE,
        module2019PathwayIEEE,
        module2038PathwayIEEE,
        module2039PathwayIEEE,
        module2040PathwayIEEE,
        module2041PathwayIEEE]
    for z in IEEEMod2_list:
        z.save()  # save to database

    ##Add level 3 Module links to IEEE
    IEEEMod3_list = [module3001PathwayIEEE,
        module3043PathwayIEEE,
        module3003PathwayIEEE,
        module3037PathwayIEEE,
        module3039PathwayIEEE,
        module3040PathwayIEEE,
        module3041PathwayIEEE,
        module3042PathwayIEEE,
        module3045PathwayIEEE,
        module3046PathwayIEEE]
    for z in IEEEMod3_list:
        z.save()  # save to database

    ##Add level 1 Module links to GH6Q
    GH6QMod1_list = [module1029PathwayGH6Q,
        module1012PathwayGH6Q,
        module1001PathwayGH6Q,
        module1012PathwayGH6Q,
        module1005PathwayGH6Q,
        module1006PathwayGH6Q,
        module1057PathwayGH6Q]
    for z in GH6QMod1_list:
        z.save()  # save to database
    
    ##Add level 2 Module links to GH6Q
    GH6QMod2_list = [module2025PathwayGH6Q,
        module2035PathwayGH6Q,
        module2037PathwayGH6Q,
        module2059PathwayGH6Q,
        module2038PathwayGH6Q,
        module2039PathwayGH6Q,
        module2040PathwayGH6Q,
        module2041PathwayGH6Q,
        module2056PathwayGH6Q,
        module2062PathwayGH6Q]
    for z in GH6QMod2_list:
        z.save()  # save to database
    
    ##Add level 3 Module links to GH6Q
    GH6QMod3_list = [module3044PathwayGH6Q,
        module3021PathwayGH6Q,
        module3059PathwayGH6Q,
        module3066PathwayGH6Q,
        module3067PathwayGH6Q,
        module3003PathwayGH6Q,
        module3040PathwayGH6Q,
        module3041PathwayGH6Q,
        module3042PathwayGH6Q,
        module3046PathwayGH6Q]
    for z in GH6QMod3_list:
        z.save()  # save to database
    
    ##Add level 4 Module links to GH6Q
    GH6QMod4_list = [ module4001PathwayGH6Q,
        module4003PathwayGH6Q,
        module4009PathwayGH6Q,
        module4010PathwayGH6Q,
        module4002PathwayGH6Q,
        module4003PathwayGH6Q,
        module4009PathwayGH6Q,
        module4023PathwayGH6Q,
        module4024PathwayGH6Q]
    for z in GH6QMod4_list:
            z.save()  # save to database

    ##Add level 1 Module links to GH6P
    GH6PMod1_list = [module1029PathwayGH6P,
        module1012PathwayGH6P,
        module1001PathwayGH6P,
        module1012PathwayGH6P,
        module1005PathwayGH6P,
        module1006PathwayGH6P,
        module1057PathwayGH6P]
    for z in GH6PMod1_list:
        z.save()  # save to database
    
    ##Add level 2 Module links to GH6P
    GH6PMod2_list = [module2025PathwayGH6P,
        module2035PathwayGH6P,
        module2037PathwayGH6P,
        module2059PathwayGH6P,
        module2038PathwayGH6P,
        module2039PathwayGH6P,
        module2040PathwayGH6P,
        module2041PathwayGH6P,
        module2056PathwayGH6P,
        module2062PathwayGH6P]
    for z in GH6PMod2_list:
        z.save()  # save to database
    
    ##Add level 3 Module links to GH6P
    GH6PMod3_list = [module3001PathwayGH6P,
        module3043PathwayGH6P,
        module3021PathwayGH6P,
        module3059PathwayGH6P,
        module3066PathwayGH6P,
        module3067PathwayGH6P,
        module3003PathwayGH6P,
        module3040PathwayGH6P,
        module3041PathwayGH6P,
        module3042PathwayGH6P,
        module3046PathwayGH6P]
    for z in GH6PMod3_list:
        z.save()  # save to database

if __name__ == "__main__":
    addPathwayModuleLinks()