from database.models import *
############################ Module to Pathway links #########################

def addPathwayModuleLinks():
    #### PathwayG402 Link tables
    #level 1
    module1023PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1023')
    module1026PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1026')
    module1033PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1033')
    module1027PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1027') #with SSD
    module1025PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1025') #without SSD
    module1029PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1029') #without SSD

    module1028PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1028', mpCore=False)
    module1030PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1030', mpCore=False)
    module1031PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1031', mpCore=False)
    module1032PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1032', mpCore=False)

    #level 2
    module2058PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2058')
    module2059PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2059')
    module2060PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2060')
    module2065PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2065')

    module2056PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2056', mpCore=False)
    module2062PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2062', mpCore=False)
    module2066PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2066', mpCore=False)

    #level 3
    module3001PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3001')

    module3021PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3021', mpCore=False)
    module3056PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3056', mpCore=False)
    module3058PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3058', mpCore=False)
    module3059PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3059', mpCore=False)
    module3064PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3064', mpCore=False)
    module3065PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3065', mpCore=False)
    module3066PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3066', mpCore=False)
    module3067PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC3067', mpCore=False)

    #level 4
    module4006PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC4006')
    module4008PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC4008')

    moduleECS4003PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='ECS4003', mpCore=False)
    module4003PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC4003', mpCore=False)
    module4009PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC4009', mpCore=False)
    module4010PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC4010', mpCore=False)

    #PathwayG400 Link tables
    #level 1
    module1023PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1023')
    module1026PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1026')
    module1033PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1033')
    module1027PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1027') #with SSD
    module1025PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1025') #without SSD
    module1029PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1029') #without SSD

    module1028PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1028', mpCore=False)
    module1030PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1030', mpCore=False)
    module1031PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1031', mpCore=False)
    module1032PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1032', mpCore=False)

    #level 2
    module2058PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2058')
    module2059PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2059')
    module2060PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2060')
    module2065PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2065')

    module2056PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2056', mpCore=False)
    module2062PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2062', mpCore=False)
    module2066PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2066', mpCore=False)

    #level 3
    module3002PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3002')

    module3001PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3001', mpCore=False)
    module3021PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3021', mpCore=False)
    module3056PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3056', mpCore=False)
    module3058PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3058', mpCore=False)
    module3059PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3059', mpCore=False)
    module3064PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3064', mpCore=False)
    module3065PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3065', mpCore=False)
    module3066PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3066', mpCore=False)
    module3067PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC3067', mpCore=False)

    #PathwayG602 linker tables
    #level 1
    module1023PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1023')
    module1026PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1026')
    module1033PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1033')
    module1027PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1027')
    module1025PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1025')
    module1029PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1029')

    module1028PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1028', mpCore=False)
    module1030PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1030', mpCore=False)
    module1031PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1031', mpCore=False)
    module1032PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC1032', mpCore=False)

    #level 2
    module2058PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2058')
    module2059PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2059')
    module2063PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2063')
    module2065PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2065')

    module2056PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2056', mpCore=False)
    module2062PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2062', mpCore=False)
    module2066PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2066', mpCore=False)

    #level 3
    module3021PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3021', mpCore=False)
    module3031PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3031', mpCore=False)
    module3045PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3045', mpCore=False)   
    module3056PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3056', mpCore=False)
    module3058PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3058', mpCore=False)
    module3059PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3059', mpCore=False)
    module3063PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3063', mpCore=False)
    module3064PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3064', mpCore=False)
    module3065PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3065', mpCore=False)
    module3067PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC3067', mpCore=False)

    #level 4
    module4006PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC4006')
    module4008PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC4008')

    moduleECS4003PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='ECS4003', mpCore=False)
    module4003PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC4003', mpCore=False)
    module4009PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC4009', mpCore=False)
    module4010PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC4010', mpCore=False)



    #Pathway g604 linker tables
    #level 1
    module1023PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1023')
    module1026PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1026')
    module1033PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1033')
    module1027PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1027')
    module1025PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1025')
    module1029PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1029')

    module1028PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1028', mpCore=False)
    module1030PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1030', mpCore=False)
    module1031PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1031', mpCore=False)
    module1032PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC1032', mpCore=False)

    #level 2
    module2058PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2058')
    module2059PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2059')
    module2063PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2063')
    module2065PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2065')

    module2056PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2056', mpCore=False)
    module2062PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2062', mpCore=False)
    module2066PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2066', mpCore=False)

    #level 3
    module3032PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3032')
    module3045PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3045')

    module3021PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3021', mpCore=False)
    module3031PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3031', mpCore=False)
    module3056PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3056', mpCore=False)
    module3058PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3058', mpCore=False)
    module3059PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3059', mpCore=False)
    module3063PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3063', mpCore=False)
    module3064PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3064', mpCore=False)
    module3065PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3065', mpCore=False)
    module3067PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC3067', mpCore=False)

    #PathwayG606 linker tables
    #level 1
    module1023PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1023')
    module1026PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1026')
    module1033PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1033')
    module1027PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1027')
    module1025PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1025')
    module1029PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1029')

    module1028PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1028', mpCore=False)
    module1030PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1030', mpCore=False)
    module1031PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1031', mpCore=False)
    module1032PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC1032', mpCore=False)

    #level 2
    module2058PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2058')
    module2059PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2059')
    module2063PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2063')
    module2065PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2065')

    module2056PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2056', mpCore=False)
    module2062PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2062', mpCore=False)
    module2066PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2066', mpCore=False)

    #level3
    module3068PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3068')

    module3031PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3031', mpCore=False)
    module3056PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3056', mpCore=False)
    module3059PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3059', mpCore=False)
    module3063PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3063', mpCore=False)
    module3064PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3064', mpCore=False)

    #level4
    module3069PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3069')

    module3021PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3021', mpCore=False)
    module3045PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3045', mpCore=False)
    module3058PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3058', mpCore=False)
    module3065PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3065', mpCore=False)
    module3067PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3067', mpCore=False)

    #PathwayGG45 linker Tables
    #level 1
    module1023PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1023')
    module1026PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1026')
    module1033PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1033')
    module1027PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1027')
    module1025PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1025')
    module1029PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1029')

    module1028PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1028', mpCore=False)
    module1030PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1030', mpCore=False)
    module1031PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1031', mpCore=False)
    module1032PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC1032', mpCore=False)

    #level 2
    module2051PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2051')
    module2052PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2052')
    module2023PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2053')
    module2054PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2054')
    module2065PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2065')

    module2056PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2056', mpCore=False)
    module2062PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2062', mpCore=False)
    module2066PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2066', mpCore=False)

    #level 3
    module3047PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3047')
    module3045PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3045')
    module3062PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3062')

    module3031PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3031', mpCore=False)
    module3056PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3056', mpCore=False)
    module3064PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3064', mpCore=False)

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


if __name__ == "__main__":
    addPathwayModuleLinks()