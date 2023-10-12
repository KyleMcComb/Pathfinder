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

def addComputerScienceModules():
    #Computer Science Level 1 modules
    module1023 = Module(moduleID = 'CSC1023', 
                        moduleName ='Databases', 
                        moduleSemester = 2, 
                        moduleDescription = 'Introduction to fundamental concepts in database systems with a focus on solving real-world problems using data models, schemas, and SQL. Topics also include relational database design, normalization theory, dependency theory, data management, and database access using programming languages.', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1024 = Module(moduleID = 'CSC1024',
                        moduleName = 'Programming and Systems Development',
                        moduleSemester = 3, #full year 
                        moduleDescription = 'Introduces the fundamentals of programming through real-world examples, emphasizing good algorithm design, data structures, and object-oriented programming. Students learn about assignment, selection, repetition, functions/methods, and I/O handling.', 
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
                        moduleDescription = 'Introduces foundational maths necessary for computing, covering number theory, algebra, logic, set theory, vectors, matrices, statistics, and graph theory. The module prepares students for algorithm design, logical reasoning, and programming.', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1027 = Module(moduleID = 'CSC1027', 
                        moduleName ='Programming', 
                        moduleSemester = 1, 
                        moduleDescription = 'Covers the fundamentals of object-oriented programming, introducing abstraction, encapsulation, inheritance, and polymorphism. Students will also learn about data modeling, code reuse, algorithm design, testing, and code version control.', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1028 = Module(moduleID = 'CSC1028', 
                        moduleName ='Computer Science Challenges', 
                        moduleSemester = 2, 
                        moduleDescription = 'Students engage with practical problems in Computer Science, exploring areas like data science, machine learning, cybersecurity, or computing systems, enhancing their programming experience and professional programming standards and practices.', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1029 = Module(moduleID = 'CSC1029', 
                        moduleName ='Object Oriented Programming', 
                        moduleSemester = 2, 
                        moduleDescription = 'An introduction to the fundamentals of object-oriented programming with emphasis on data modeling, code reuse, and algorithm design. The module covers abstraction, encapsulation, inheritance, polymorphism, recursion, searching and sorting, data structures, and testing.', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1030 = Module(moduleID = 'CSC1030', 
                        moduleName ='Web Technologies', 
                        moduleSemester = 2, 
                        moduleDescription = 'The module covers the combination of HTML, CSS, and JavaScript to develop client-side web applications, focusing on content design, presentation, dynamic behaviors, and accessibility across multiple browser platforms, including mobile web applications.', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1031 = Module(moduleID = 'CSC1031', 
                        moduleName ='Software Design Principles', 
                        moduleSemester = 2, 
                        moduleDescription = 'This module introduces the fundamentals of good, secure software design, applying object-oriented principles, design, and cybersecurity principles through theoretical foundations and practical exercises with real-world projects.', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1032 = Module(moduleID = 'CSC1032', 
                        moduleName ='Introduction to Cyber Security', 
                        moduleSemester = 2, 
                        moduleDescription = 'Covers foundational concepts, principles, and practices of cybersecurity, including attack types, threats, vulnerabilities, confidentiality, integrity, availability, authentication, access control, security policies, human threats, system design, and countermeasures.', 
                        moduleLevel = 1, 
                        moduleWeight = 20)

    module1033 = Module(moduleID = 'CSC1033', 
                        moduleName ='Introduction to Computer Architecture', 
                        moduleSemester = 1, 
                        moduleDescription = 'This module provides an overview of computer architecture and technology, digital design basics, number representation, arithmetic operations, microarchitecture, instruction sets, assembly programming, compilation flow, and the role of operating systems.', 
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
                    moduleDescription = "Introduction to systems administration and support with focus on hardware, Windows-based systems, and SoHo networking principles. Covers installation, maintenance, and updating of Windows operating systems and applications, Active Directory planning and implementation, and troubleshooting of major PC components.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2052 = Module(moduleID = 'CSC2052', 
                    moduleName ='Server Side Web Development', 
                    moduleSemester = 1, 
                    moduleDescription = "Focus on object-oriented design, agile and lean software design, user experience design, database principles, and secure coding practices for server-side web development. Emphasizes contemporary web programming and application of agile and lean principles to design and develop dynamic web-based software applications.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2053 = Module(moduleID = 'CSC2053', 
                    moduleName ='Introduction to Enterprise Computing', 
                    moduleSemester = 2, 
                    moduleDescription = "Introduction to concepts and systems in Enterprise Computing including cloud computing and Linux. Covers virtualization technologies, shell scripting, secure communication with networked systems, and architecture of modern data centers.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2054 = Module(moduleID = 'CSC2054', 
                    moduleName ='User Experience Design', 
                    moduleSemester = 2, 
                    moduleDescription = "Overview of user experience design including ergonomics, human factors, prototyping, design principles, and usability metrics. Focuses on developing user interfaces for specific applications and assessing their usability.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2056 = Module(moduleID = 'CSC2056', 
                    moduleName ='Systems Security and Cryptography', 
                    moduleSemester = 2, 
                    moduleDescription = "Introduction to fundamental concepts in cyber security, secure information system design, and cryptography. Provides an understanding of vulnerabilities, threats, attacks, and cryptographic algorithms for confidentiality, integrity, and authentication.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2057 = Module(moduleID = 'CSC2057', 
                    moduleName ='Modern Web App Development', 
                    moduleSemester = 1, 
                    moduleDescription = "Exploration of web development technologies and software engineering practices for developing dynamic web applications. Covers client-side technologies, server-side programming languages, RDBMS, and principles of solution-based design, development, deployment, and testing.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2058 = Module(moduleID = 'CSC2058', 
                    moduleName ='Software Engineering and Systems Development', 
                    moduleSemester = 3, 
                    moduleDescription = "In-depth study of software development methodologies, object-oriented design principles, GUI design, algorithmic design, and secure and reliable system delivery. Covers use of version control, automated tests, and various software and project management tools in the context of software engineering projects.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2059 = Module(moduleID = 'CSC2059', 
                    moduleName ='Data Structures and Algorithms', 
                    moduleSemester = 1, 
                    moduleDescription = "Study of data structures and algorithms including stacks, lists, queues, trees, hash tables, graphs, sets, maps, searching, sorting, and recursion. Provides understanding of asymptotic analysis of algorithms and programming language representation and implementation.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2060 = Module(moduleID = 'CSC2060', 
                    moduleName ='Theory of Computation', 
                    moduleSemester = 2, 
                    moduleDescription = "Introduction to theory of computation including automata, formal languages, computability theory, decidability theory, and complexity theory. Provides understanding of how computation occurs using finite state machines and Turing machines and ability to reason about algorithmic complexity.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2062 = Module(moduleID = 'CSC2062', 
                    moduleName ='Introduction to AI and Machine Learning', 
                    moduleSemester = 2, 
                    moduleDescription = "Introduction to concepts of artificial intelligence and machine learning including supervised and unsupervised learning, experimental settings, feature selection, evaluation in machine learning, and various classification and clustering models.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2063 = Module(moduleID = 'CSC2063', 
                    moduleName ='Service Oriented Programming', 
                    moduleSemester = 2, 
                    moduleDescription = "Study of design and development of software with service-oriented architecture (SoA), focusing on modular architecture, SoA design principles, Web services technology, Web APIs, and serialization techniques.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2065 = Module(moduleID = 'CSC2065', 
                    moduleName ='Professional and Transferrable Skills', 
                    moduleSemester = 1, 
                    moduleDescription = "Preparation for employment through development of business and professional awareness, transferable skills, and critical reflection abilities. Covers legal, social, ethical, and professional issues, intellectual property, data protection, privacy, security, globalisation, communication, cultural sensitivity, and gender neutrality.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    module2066 = Module(moduleID = 'CSC2066', 
                    moduleName ='Networks and Protocols', 
                    moduleSemester = 2, 
                    moduleDescription = "Overview of networking fundamentals, protocols, Internet and World Wide Web, computer network layers, routing, LAN topologies, data compression, application protocols, software-defined networks, socket-based connections, and network security.", 
                    moduleLevel = 2, 
                    moduleWeight = 20)

    ##ADD Level 2 Modules
    mod2_list = [module2051, module2052, module2053, module2054, module2056, module2057,
                module2058, module2059, module2060, module2062, module2063, module2065,
                module2066]
    for b in mod2_list:
        b.save()

    #Computer Science Level 3 Modules
    module3001 = Module(moduleID = 'CSC3001', 
                    moduleName ='Formal Methods', 
                    moduleSemester = 2, 
                    moduleDescription = "A rigorous approach to software development, logical foundations, specification of data types, implicit and explicit specification of functions and operations. Assessment includes assignments and a final paper.", 
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3002 = Module(moduleID = 'CSC3002', 
                    moduleName ='Computer Science Project', 
                    moduleSemester = 3, 
                    moduleDescription = "A project requiring construction of a software system, including specification, design, and realization. Assessment is entirely project-based.", 
                    moduleLevel = 3, 
                    moduleWeight = 40)

    module3021 = Module(moduleID = 'CSC3021', 
                    moduleName ='Concurrent Programming', 
                    moduleSemester = 1, 
                    moduleDescription = "Focuses on Concurrent Programming, Java Threads, mutual exclusion, semaphores, models of concurrency, and other related topics. The course is assessed through coursework.", 
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3023 = Module(moduleID = 'CSC3023', 
                    moduleName ='BIT Project', 
                    moduleSemester = 3, 
                    moduleDescription = "A project-focused module requiring the construction of IT-based solutions to business-related problems, emphasizing agile software design and user acceptance testing. Assessment is project-based.", 
                    moduleLevel = 3, 
                    moduleWeight = 40)

    module3031 = Module(moduleID = 'CSC3031', 
                    moduleName ='Software Design Principles and Patterns', 
                    moduleSemester = 2, 
                    moduleDescription = "The module covers good software design principles, creation, structure, and behavior patterns, and architectural patterns, with an emphasis on object-oriented design and commercialization of software products.", 
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3032 = Module(moduleID = 'CSC3032', 
                    moduleName ='Software Engineering Project', 
                    moduleSemester = 3, 
                    moduleDescription = "Team-based project module focused on developing an IT solution. Emphasizes system and data architectural design, project management skills, and societal, commercial, and economic considerations.", 
                    moduleLevel = 3, 
                    moduleWeight = 40)

    module3045 = Module(moduleID = 'CSC3045', 
                    moduleName ='Contemporary Team-based Computing Projects', 
                    moduleSemester = 1, 
                    moduleDescription = "Module covers ambiguous problem situations, agile software development practices, project management, and team collaboration. Emphasizes on innovative design thinking and application of software development technologies in both remote and local environments.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3047 = Module(moduleID = 'CSC3047', 
                    moduleName ='CIT Project', 
                    moduleSemester = 3, 
                    moduleDescription = "A user-focused IT project module, encompassing agile software design, user experience design, and user acceptance testing. The module emphasizes developing web apps deployable to various devices while applying various project management skills.",
                    moduleLevel = 3, 
                    moduleWeight = 40)

    module3056 = Module(moduleID = 'CSC3056', 
                    moduleName ='Software Testing', 
                    moduleSemester = 2, 
                    moduleDescription = "Module provides a comprehensive understanding and application of software testing principles and techniques. It allows students to develop, organize, and execute test plans for software applications, employing various test automation tools.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3058 = Module(moduleID = 'CSC3058', 
                    moduleName ='Advanced Computer Architectures', 
                    moduleSemester = 1, 
                    moduleDescription = "A study on the evolution of computer architecture and design of hardware and software elements of computer systems, focusing on performance, instruction sets, processor micro-architecture, caches, parallel architectures and fault tolerance.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3059 = Module(moduleID = 'CSC3059', 
                    moduleName ='Malware Analysis', 
                    moduleSemester = 2, 
                    moduleDescription = "Module introduces students to malware analysis, covering basic static and dynamic techniques, different malware types, and automated detection methods. Provides hands-on experience with analysis tools and understanding malware behavior.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3062 = Module(moduleID = 'CSC3062', 
                    moduleName ='Data Analysis and Visualisation', 
                    moduleSemester = 1, 
                    moduleDescription = "This module covers various techniques and tools for data analysis and visualization. It introduces students to the fundamental principles and best practices of data analytics, supporting them in developing critical skills required for analyzing, interpreting, and visualizing data effectively.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3063 = Module(moduleID = 'CSC3063', 
                    moduleName ='Secure Software Development', 
                    moduleSemester = 2, 
                    moduleDescription = "This module explores principles and practices of secure software development. Students will learn about common security threats and vulnerabilities, methods to secure software development practices, and security testing techniques to ensure the resilience of the software.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3064 = Module(moduleID = 'CSC3064', 
                    moduleName ='Network Security', 
                    moduleSemester = 2, 
                    moduleDescription = "Network Security module covers the principles, techniques, and practical skills required to secure networks and data. It includes topics on cryptographic protocols, network security infrastructure, wireless security, and various network attack mechanisms and defenses.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3065 = Module(moduleID = 'CSC3065', 
                    moduleName ='Cloud Computing', 
                    moduleSemester = 1, 
                    moduleDescription = "Introduction to the fundamental concepts and technologies of cloud computing, including cloud service models, deployment models, architectural designs, and key challenges associated with planning, developing, and managing in the cloud environment.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3066 = Module(moduleID = 'CSC3066', 
                    moduleName ='Deep Learning', 
                    moduleSemester = 2, 
                    moduleDescription = "Deep Learning module provides a comprehensive introduction to the fundamental principles and practices of deep learning. The module covers neural networks, convolutional networks, sequence modeling, and their applications in computer vision, natural language processing, and other fields.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3067 = Module(moduleID = 'CSC3067', 
                    moduleName ='Video Analytics and Machine Learning', 
                    moduleSemester = 1, 
                    moduleDescription = "This module introduces students to video analytics and machine learning, focusing on video processing techniques, feature extraction, classification, object detection, and tracking. It also explores machine learning models applicable to video analytics.",
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3068 = Module(moduleID = 'CSC3068', 
                    moduleName ='Software Development Practice', 
                    moduleSemester = 2, 
                    moduleDescription = "This module covers best practices in software development, including agile methodologies, version control, continuous integration, and test-driven development. Students will learn how to effectively collaborate in a development team and manage the lifecycle of a software project from planning to deployment. The module also discusses ethical considerations in software development and how to address common challenges in the field.", 
                    moduleLevel = 3, 
                    moduleWeight = 20)

    module3069 = Module(moduleID = 'CSC3069', 
                    moduleName ='Software Engineering Enterprise Project', 
                    moduleSemester = 1, 
                    moduleDescription = "This enterprise-level project module challenges students to apply their software engineering skills in a real-world setting. Students will work in teams to develop a substantial software product for an external client, following all stages of the software development lifecycle. The module emphasizes project management, client communication, and the application of software engineering principles and practices. Assessment is based on the delivered software product, project documentation, and individual and team performance throughout the project.", 
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
    module4003 = Module(moduleID = 'CSC4003', 
                    moduleName ='Algorithms: Analysis and Applications', 
                    moduleSemester = 2, 
                    moduleDescription = "The course covers analysis and design of algorithms, complexity, n-p completeness, and various algorithms for searching, sorting, operating on trees, graphs, and strings. It includes database algorithms, B-tree and hashing, and applications of algorithms.",
                    moduleLevel = 4, 
                    moduleWeight = 20)

    module4006 = Module(moduleID = 'CSC4006', 
                    moduleName ='Research and Development Project', 
                    moduleSemester = 3, 
                    moduleDescription = "Students undertake a research investigation, developing software for generating research results, analyzing, validating, and drawing conclusions from these results. This includes writing and defending a research article and software development report.",
                    moduleLevel = 4, 
                    moduleWeight = 40)

    module4008 = Module(moduleID = 'CSC4008', 
                    moduleName ='Digital Transformation: Software Design, Management and Practical Implementation', 
                    moduleSemester = 1, 
                    moduleDescription = "The module covers opportunity analysis, entrepreneurship, innovation, business planning, software design principles and patterns, software architecture, legal, social and ethical considerations, and software project and team management within a modern commercial setting.",
                    moduleLevel = 4, 
                    moduleWeight = 20)

    module4009 = Module(moduleID = 'CSC4009', 
                    moduleName ='Fairness, Interpretability and Privacy in Machine Learning', 
                    moduleSemester = 2, 
                    moduleDescription = "This course covers the ethics of data-driven systems, fairness testing and mechanisms, privacy preservation, interpretability in machine learning, and adversarial attacks and defenses, aiming to create fair, privacy-preserving, and explainable ML pipelines.",
                    moduleLevel = 4, 
                    moduleWeight = 20)

    module4010 = Module(moduleID = 'CSC4010', 
                    moduleName ='Parallel and Distributed Computing', 
                    moduleSemester = 1, 
                    moduleDescription = "This module focuses on using multiple compute resources for problem-solving. Topics include basic concepts and terminology of parallel programming models, program and problem analysis, practical parallel programming, implementation of parallel code, distributed computing theory, and data synchronization methods.",
                    moduleLevel = 4, 
                    moduleWeight = 20)

    ##ADD Level 4 Modules
    mod4_list = [module4003, module4006, module4008, module4009, module4010]
    for d in mod4_list:
        d.save()

if __name__ == "__main__":
    addComputerScienceModules()