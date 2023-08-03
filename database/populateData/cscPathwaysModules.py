from database.models import *

"""this data has already been entered into the database, to view the data run these commands:
py manage.py shell
>>>from database.models import *
>>>Pathway.objects.all()
>>>Module.objects.all()
>>>ModulePathway.objects.all()

to add this data to the database again run these commands:
py manage.py shell
>>>from database.models import *
>>>from database.populateData import cscPathwaysModules
to add pathways
>>>cscPathwaysModules.addComputerSciencePathways
to add modules 
>>>cscPathwaysModules.addComputerScienceModules
to add linker tables
>>>cscPathwaysModules.addComputerSciencePathwayModuleLinks
"""

def addModuleDescriptions():
    allModules = Module.objects.all()

    for i in range(len(allModules)):
        allModules[i].moduleDescription = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        allModules[i].save()

def addComputerSciencePathways():
    #Computer science pathways
    pathwayG402 = Pathway(pathwayID ='G402', pathwayName = 'MEng Computer Science', pathwayLevels = 4)
    #pathwayG404 = Pathway(pathwayID = 'G404', pathwayName = 'BENG-I (International) Computer Science', pathwayLevels = 3)
    pathwayG400 = Pathway(pathwayID='G400', pathwayName='BSc Computer Science', pathwayLevels=3)
    pathwayG602 = Pathway(pathwayID='G602', pathwayName='MEng Software Engineering', pathwayLevels=4)
    pathwayG604 = Pathway(pathwayID='G604', pathwayName='BEng Software Engineering', pathwayLevels=3)
    pathwayG606 = Pathway(pathwayID='G606', pathwayName='BEng Software Engineering with Digital Technology Partnership', pathwayLevels=4)
    pathwayGG45 = Pathway(pathwayID='GG45', pathwayName='BSc Computing and Information Technology', pathwayLevels=3)
    #pathwayGN51 = Pathway(pathwayID='GN51', pathwayName='BSc Business Information Technology', pathwayLevels=3)

    ##ADD ALL PATHWAYS
    path_list = [pathwayG402, pathwayG400, pathwayG602, pathwayG604, pathwayG606, pathwayGG45]
    for x in path_list:
        x.save()


def addComputerScienceModules():
    #Computer Science Level 1 modules
    module1023 = Module(moduleID = 'CSC1023', 
                        moduleName ='Databases', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1024 = Module(moduleID = 'CSC1024',
                        moduleName = 'Programming and Systems Development',
                        moduleSemester = 3, #full year 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 40)

    module1025 = Module(moduleID = 'CSC1025', 
                        moduleName ='Procedural Programming', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1026 = Module(moduleID = 'CSC1026', 
                        moduleName ='Fundamentals of Maths for Computing', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1027 = Module(moduleID = 'CSC1027', 
                        moduleName ='Programming', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1028 = Module(moduleID = 'CSC1028', 
                        moduleName ='Computer Science Challenges', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1029 = Module(moduleID = 'CSC1029', 
                        moduleName ='Object Oriented Programming', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1030 = Module(moduleID = 'CSC1030', 
                        moduleName ='Web Technologies', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1031 = Module(moduleID = 'CSC1031', 
                        moduleName ='Software Design Principles', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1032 = Module(moduleID = 'CSC1032', 
                        moduleName ='Introduction to Cyber Security', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1033 = Module(moduleID = 'CSC1033', 
                        moduleName ='Introduction to Computer Architecture', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    ##ADD ALL level 1 Modules
    mod1_list = [module1023, module1024, module1025, module1026, module1027, module1028,
                module1029, module1030, module1031, module1032, module1033]
    for a in mod1_list:
        a.save()

    #Computer Science level 2 modules
    module2051 = Module(moduleID = 'CSC2051', 
                        moduleName ='Systems Administration and Support', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2052 = Module(moduleID = 'CSC2052', 
                        moduleName ='Server Side Web Development', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2053 = Module(moduleID = 'CSC2053', 
                        moduleName ='Introduction to Enterprise Computing', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2054 = Module(moduleID = 'CSC2054', 
                        moduleName ='User Experience Design', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2056 = Module(moduleID = 'CSC2056', 
                        moduleName ='Systems Security and Cryptography', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2057 = Module(moduleID = 'CSC2057', 
                        moduleName ='Modern Web App Development', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2058 = Module(moduleID = 'CSC2058', 
                        moduleName ='Software Engineering and Systems Development', 
                        moduleSemester = 3, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2059 = Module(moduleID = 'CSC2059', 
                        moduleName ='Data Structures and Algorithms', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2060 = Module(moduleID = 'CSC2060', 
                        moduleName ='Theory of Computation', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2062 = Module(moduleID = 'CSC2062', 
                        moduleName ='Introduction to AI and Machine Learning', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2063 = Module(moduleID = 'CSC2063', 
                        moduleName ='Service Oriented Programming', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2065 = Module(moduleID = 'CSC2065', 
                        moduleName ='Professional and Transferrable Skills', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    module2066 = Module(moduleID = 'CSC2066', 
                        moduleName ='Networks and Protocols', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 2, 
                        moduleWeight = 20)

    ##ADD Level 2 Modules
    mod2_list = [module2051, module2052, module2053, module2054, module2056, module2057,
                module2058, module2059, module2060, module2062, module2063, module2065,
                module2066]
    for b in mod2_list:
        b.save()

    #Computer Science Level 3 Modules
    module3002 = Module(moduleID = 'CSC3002', 
                        moduleName ='Computer Science Project', 
                        moduleSemester = 3, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 40)

    module3023 = Module(moduleID = 'CSC3023', 
                        moduleName ='BIT Project', 
                        moduleSemester = 3, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 40)

    module3032 = Module(moduleID = 'CSC3032', 
                        moduleName ='Software Engineering Project', 
                        moduleSemester = 3, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 40)

    module3047 = Module(moduleID = 'CSC3047', 
                        moduleName ='CIT Project', 
                        moduleSemester = 3, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 40)

    module3021 = Module(moduleID = 'CSC3021', 
                        moduleName ='Concurrent Programming', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3045 = Module(moduleID = 'CSC3045', 
                        moduleName ='Contemporary Team-Based Projects', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3058 = Module(moduleID = 'CSC3058', 
                        moduleName ='Advanced Computer Architectures/Systems', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3062 = Module(moduleID = 'CSC3062', 
                        moduleName ='Data Analysis and Visualisation', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3065 = Module(moduleID = 'CSC3065', 
                        moduleName ='Cloud Computing', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3067 = Module(moduleID = 'CSC3067', 
                        moduleName ='Video Analytics and Machine Learning', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3069 = Module(moduleID = 'CSC3069', 
                        moduleName ='Software Engineering Enterprise Project', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3001 = Module(moduleID = 'CSC3001', 
                        moduleName ='Formal Methods', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3031 = Module(moduleID = 'CSC3031', 
                        moduleName ='Software Design Principles and Patterns', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3056 = Module(moduleID = 'CSC3056', 
                        moduleName ='Software Testing', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3059 = Module(moduleID = 'CSC3059', 
                        moduleName ='Malware Analysis', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3063 = Module(moduleID = 'CSC3063', 
                        moduleName ='Secure Software Development', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3064 = Module(moduleID = 'CSC3064', 
                        moduleName ='Network Security', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3066 = Module(moduleID = 'CSC3066', 
                        moduleName ='Deep Learning', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    module3068 = Module(moduleID = 'CSC3068', 
                        moduleName ='Software Development Practice', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 3, 
                        moduleWeight = 20)

    ##ADD Level 3 Modules
    mod3_list = [module3001, module3002, module3021 ,module3023, module3031, module3032,
                module3045, module3047, module3056, module3058, module3059, module3062,
                module3063, module3064, module3065, module3066, module3067, module3068,
                module3069]
    for c in mod3_list:
        c.save()

    #Computer Science Level 4 Modules
    module4006 = Module(moduleID = 'CSC4006', 
                        moduleName ='Research and Development Project', 
                        moduleSemester = 3, 
                        moduleDescription = '', 
                        moduleLevel = 4, 
                        moduleWeight = 40)

    moduleECS4003 = Module(moduleID = 'ECS4003', 
                        moduleName ='Advanced Computer Engineering', 
                        moduleSemester = 3, 
                        moduleDescription = '', 
                        moduleLevel = 4, 
                        moduleWeight = 20) #not a mistake - module is full year and 20 cats

    module4008 = Module(moduleID = 'CSC4008', 
                        moduleName ='Digital Transformation: Software Design, Management and Practical Implementation', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 4, 
                        moduleWeight = 20)

    module4010 = Module(moduleID = 'CSC4010', 
                        moduleName ='Parallel and Distributed Computing', 
                        moduleSemester = 1, 
                        moduleDescription = '', 
                        moduleLevel = 4, 
                        moduleWeight = 20)

    module4003 = Module(moduleID = 'CSC4003', 
                        moduleName ='Algorithms: Analysis and Applications', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 4, 
                        moduleWeight = 20)

    module4009 = Module(moduleID = 'CSC4009', 
                        moduleName ='Fairness, Interpretability and Privacy in Machine Learning', 
                        moduleSemester = 2, 
                        moduleDescription = '', 
                        moduleLevel = 4, 
                        moduleWeight = 20)

    ##ADD Level 4 Modules
    mod4_list = [module4003, module4006, module4008, module4009, module4010]
    for d in mod4_list:
        d.save()

def addComputerSciencePathwayModuleLinks():
    #PathwayG402 Link tables
    #level 1
    module1023PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1023')
    module1026PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1026')
    module1033PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1033')
    module1027PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1027')
    module1025PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1025')
    module1029PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1029')

    module1028PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1028', mpCore=False)
    module1030PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1030', mpCore=False)
    module1031PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1031', mpCore=False)
    module1032PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC1032', mpCore=False)

    """ ##ADD level 1 Module links to G402
    G402Mod1_list = [module1023PathwayG402, module1026PathwayG402, module1033PathwayG402,
                    module1027PathwayG402, module1025PathwayG402, module1029PathwayG402,
                    module1028PathwayG402, module1030PathwayG402, module1031PathwayG402,
                    module1032PathwayG402]
    for z in G402Mod1_list:
    z.save() """

    #level 2
    module2058PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2058')
    module2059PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2059')
    module2060PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2060')
    module2065PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2065')

    module2056PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2056', mpCore=False)
    module2062PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2062', mpCore=False)
    module2066PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC2066', mpCore=False)
    """ ##ADD level 2 Module links to G402
    G402Mod2_list = [module2058PathwayG402, module2059PathwayG402, module2060PathwayG402,
                    module2065PathwayG402, module2056PathwayG402, module2062PathwayG402,
                    module2066PathwayG402]
    for z in G402Mod2_list:
    z.save() """

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
    """ ##ADD level 3 Module links to G402
    G402Mod3_list = [module3001PathwayG402, module3021PathwayG402, module3056PathwayG402,
                    module3058PathwayG402, module3059PathwayG402, module3064PathwayG402,
                    module3065PathwayG402, module3066PathwayG402, module3067PathwayG402]
    for z in G402Mod3_list:
    z.save() """

    #level 4
    module4006PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC34006')
    module4008PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC34008')

    moduleECS4003PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='ECS4003', mpCore=False)
    module4003PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC4003', mpCore=False)
    module4009PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC4009', mpCore=False)
    module4010PathwayG402 = ModulePathway(pathwayID = 'G402', moduleID='CSC4010', mpCore=False)
    """ ##ADD level 4 Module links to G402
    G402Mod4_list = [module4006PathwayG402, module4008PathwayG402, moduleECS4003PathwayG402,
                    module4003PathwayG402, module4009PathwayG402, module4010PathwayG402]
    for z in G402Mod4_list:
    z.save() """

    #PathwayG400 Link tables
    #level 1
    module1023PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1023')
    module1026PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1026')
    module1033PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1033')
    module1027PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1027')
    module1025PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1025')
    module1029PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1029')

    module1028PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1028', mpCore=False)
    module1030PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1030', mpCore=False)
    module1031PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1031', mpCore=False)
    module1032PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC1032', mpCore=False)
    """ ##ADD level 1 Module links to G400
    G400Mod1_list = [module1023PathwayG400, module1026PathwayG400, module1033PathwayG400,
                    module1027PathwayG400, module1025PathwayG400, module1029PathwayG400,
                    module1028PathwayG400, module1030PathwayG400, module1031PathwayG400,
                    module1032PathwayG400]
    for z in G400Mod1_list:
    z.save() """

    #level 2
    module2058PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2058')
    module2059PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2059')
    module2060PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2060')
    module2065PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2065')

    module2056PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2056', mpCore=False)
    module2062PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2062', mpCore=False)
    module2066PathwayG400 = ModulePathway(pathwayID = 'G400', moduleID='CSC2066', mpCore=False)
    """ ##ADD level 2 Module links to G400
    G400Mod2_list = [module2058PathwayG400, module2059PathwayG400, module2060PathwayG400,
                    module2065PathwayG400, module2056PathwayG400, module2062PathwayG400,
                    module2066PathwayG400]
    for z in G400Mod2_list:
    z.save()
    """
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
    """ ##ADD level 3 Module links to G400
    G400Mod3_list = [module3002PathwayG400, module3001PathwayG400, module3021PathwayG400,
                    module3056PathwayG400, module3058PathwayG400, module3059PathwayG400, 
                    module3064PathwayG400, module3065PathwayG400, module3066PathwayG400, 
                    module3067PathwayG400]
    for z in G400Mod3_list:
    z.save() """

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
    """ ##ADD level 1 Module links to G602
    G602Mod1_list = [module1023PathwayG602, module1026PathwayG602, module1033PathwayG602,
                    module1027PathwayG602, module1025PathwayG602, module1029PathwayG602,
                    module1028PathwayG602, module1030PathwayG602, module1031PathwayG602,
                    module1032PathwayG602]
    for z in G602Mod1_list:
    z.save() """
    #level 2
    module2058PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2058')
    module2059PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2059')
    module2063PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2063')
    module2065PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2065')

    module2056PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2056', mpCore=False)
    module2062PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2062', mpCore=False)
    module2066PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC2066', mpCore=False)
    """ ##ADD level 2 Module links to G602
    G602Mod2_list = [module2058PathwayG602, module2059PathwayG602, module2063PathwayG602,
                    module2065PathwayG602, module2056PathwayG602, module2062PathwayG602,
                    module2066PathwayG602]
    for z in G602Mod2_list:
    z.save() """

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
    """ ##ADD level 3 Module links to G602
    G602Mod3_list = [module3021PathwayG602, module3031PathwayG602, module3045PathwayG602,
                    module3056PathwayG602, module3058PathwayG602, module3059PathwayG602, 
                    module3063PathwayG602, module3064PathwayG602, module3065PathwayG602, 
                    module3067PathwayG602]
    for z in G602Mod3_list:
    z.save() """

    #level 4
    module4006PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC34006')
    module4008PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC34008')

    moduleECS4003PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='ECS4003', mpCore=False)
    module4003PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC4003', mpCore=False)
    module4009PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC4009', mpCore=False)
    module4010PathwayG602 = ModulePathway(pathwayID = 'G602', moduleID='CSC4010', mpCore=False)
    """ ##ADD level 4 Module links to G602
    G602Mod4_list = [module4006PathwayG602, module4008PathwayG602, moduleECS4003PathwayG602,
                    module4003PathwayG602, module4009PathwayG602]
    for z in G602Mod4_list:
    z.save() """


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
    """ ##ADD level 1 Module links to G604
    G604Mod1_list = [module1023PathwayG604, module1026PathwayG604, module1033PathwayG604,
                    module1027PathwayG604, module1025PathwayG604, module1029PathwayG604,
                    module1028PathwayG604, module1030PathwayG604, module1031PathwayG604,
                    module1032PathwayG604]
    for z in G604Mod1_list:
    z.save() """

    #level 2
    module2058PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2058')
    module2059PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2059')
    module2063PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2063')
    module2065PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2065')

    module2056PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2056', mpCore=False)
    module2062PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2062', mpCore=False)
    module2066PathwayG604 = ModulePathway(pathwayID = 'G604', moduleID='CSC2066', mpCore=False)
    """ ##ADD level 2 Module links to G604
    G604Mod2_list = [module2058PathwayG604, module2059PathwayG604, module2063PathwayG604,
                    module2065PathwayG604, module2056PathwayG604, module2062PathwayG604,
                    module2066PathwayG604]
    for z in G604Mod2_list:
    z.save() """

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
    """ ##ADD level 3 Module links to G604
    G604Mod3_list = [module3032PathwayG604, module3045PathwayG604, module3021PathwayG604, 
                    module3031PathwayG604, module3056PathwayG604, module3058PathwayG604, 
                    module3059PathwayG604, module3063PathwayG604, module3064PathwayG604, 
                    module3065PathwayG604, module3067PathwayG604]
    for z in G604Mod3_list:
    z.save() """

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
    """ ##ADD level 1 Module links to G606
    G606Mod1_list = [module1023PathwayG606, module1026PathwayG606, module1033PathwayG606,
                    module1027PathwayG606, module1025PathwayG606, module1029PathwayG606,
                    module1028PathwayG606, module1030PathwayG606, module1031PathwayG606,
                    module1032PathwayG606]
    for z in G606Mod1_list:
    z.save() """

    #level 2
    module2058PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2058')
    module2059PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2059')
    module2063PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2063')
    module2065PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2065')

    module2056PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2056', mpCore=False)
    module2062PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2062', mpCore=False)
    module2066PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2066', mpCore=False)
    """ ##ADD level 2 Module links to G606
    G606Mod2_list = [module2058PathwayG606, module2059PathwayG606, module2063PathwayG606,
                    module2065PathwayG606, module2056PathwayG606, module2062PathwayG606,
                    module2066PathwayG606]
    for z in G606Mod2_list:
    z.save() """

    #level3
    module3068PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC2058')

    module3031PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3031', mpCore=False)
    module3056PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3056', mpCore=False)
    module3059PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3059', mpCore=False)
    module3063PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3063', mpCore=False)
    module3064PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3064', mpCore=False)
    """ ##ADD level 3 Module links to G606
    G606Mod3_list = [module3068PathwayG606, module3031PathwayG606, module3056PathwayG606, 
                    module3059PathwayG606, module3063PathwayG606, module3064PathwayG606] 
    for z in G606Mod3_list:
    z.save() """

    #level4
    module3069PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3069')

    module3021PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3021', mpCore=False)
    module3045PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3045', mpCore=False)
    module3058PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3058', mpCore=False)
    module3065PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3065', mpCore=False)
    module3067PathwayG606 = ModulePathway(pathwayID = 'G606', moduleID='CSC3067', mpCore=False)
    """ ##ADD level 4 Module links to G606
    G606Mod4_list = [module3069PathwayG606, module3045PathwayG606, module3021PathwayG606, 
                    module3058PathwayG606, module3065PathwayG606, module3067PathwayG606]
    for z in G606Mod4_list:
    z.save() """


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
    """ ##ADD level 1 module links to GG45
    GG45Mod1_list = [module1023PathwayGG45, module1026PathwayGG45, module1033PathwayGG45,
                    module1027PathwayGG45, module1025PathwayGG45, module1029PathwayGG45,
                    module1028PathwayGG45, module1030PathwayGG45, module1031PathwayGG45,
                    module1032PathwayGG45]
    for z in GG45Mod1_list:
    z.save() """

    #level 2
    module2051PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2051')
    module2052PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2052')
    module2023PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2053')
    module2054PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2054')
    module2065PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2065')

    module2056PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2056', mpCore=False)
    module2062PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2062', mpCore=False)
    module2066PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC2066', mpCore=False)
    """ ##ADD level 2 Module links to GG45
    GG45Mod2_list = [module2051PathwayGG45, module2052PathwayGG45, module2023PathwayGG45,
                    module2054PathwayGG45, module2065PathwayGG45, module2056PathwayGG45, 
                    module2062PathwayGG45, module2066PathwayGG45]
    for z in GG45Mod2_list:
    z.save() """

    #level 3
    module3047PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3047')
    module3045PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3045')
    module3062PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3062')

    module3031PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3031', mpCore=False)
    module3056PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3056', mpCore=False)
    module3064PathwayGG45 = ModulePathway(pathwayID = 'GG45', moduleID='CSC3064', mpCore=False)
    """ ##ADD level 3 Module links to GG45
    GG45Mod3_list = [module3047PathwayGG45, module3045PathwayGG45, module3062PathwayGG45, 
                    module3031PathwayGG45, module3056PathwayGG45, module3064PathwayGG45]
    for z in GG45Mod3_list:
    z.save() """

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
                    module4003PathwayG602, module4009PathwayG602]
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