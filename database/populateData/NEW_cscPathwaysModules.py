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
        allModules[i].moduleDescription = ""
        allModules[i].save()


def addEEModules():
    # ELE & ECS Level 1 modules
    moduleECS1001 = Module(moduleID='ECS1001',
                    moduleName='Embedded Systems',
                    moduleSemester=3,  # full year
                    moduleDescription='Introduction to embedded systems, PCB design, and C programming for embedded systems. The module covers microcontroller architecture, peripheral devices, sensors interfacing, and DC motor control. Students will gain a basic understanding of CPU architecture, instruction set, timing control, interrupts, and resource estimation for embedded applications.',
                    moduleLevel=1,
                    moduleWeight=20)

    moduleECS1005 = Module(moduleID='ECS1005',
                    moduleName='Digital Systems',
                    moduleSemester=3,  # full year
                    moduleDescription='Introduction to logic components, digital circuits, and hardware platforms. Topics include number systems, basic gates, combinational logic design, k-maps, Boolean Algebra, sequential logic, flip-flops, timing considerations, digital hardware technologies, FPGA technology, digital counters, finite state machines, computer architecture fundamentals, ISA, and Verilog HDL.',
                    moduleLevel=1,
                    moduleWeight=20)

    moduleECS1006 = Module(moduleID='ECS1006',
                    moduleName='Fundamentals of Electric Circuits',
                    moduleSemester=3,  # full year
                    moduleDescription='This module covers fundamental components (R, L, C), circuit elements and sources, electric circuit laws and theorems, AC and DC circuit analysis, phasor representation, frequency response of simple circuits, basic amplifiers and system concepts, feedback systems, operational amplifiers, diode characteristics and circuits, and bipolar junction transistors.',
                    moduleLevel=1,
                    moduleWeight=20)

    moduleELE1012 = Module(moduleID='ELE1012',
                    moduleName='Mathematics 1',
                    moduleSemester=3,  # full year
                    moduleDescription='A comprehensive module covering complex arithmetic, linear algebra, differentiation, differential equations, integration, sequences and series, and function approximation. Students will gain skills in formulating and analyzing arithmetic problems, manipulating high-dimensional mathematical objects, solving linear algebraic problems using matrix arithmetic, differentiation of various functions, and solving first and second-order differential equations.',
                    moduleLevel=1,
                    moduleWeight=20)

    moduleELE1056 = Module(moduleID='ELE1056',
                    moduleName='Electrical Engineering',
                    moduleSemester=3,  # full year
                    moduleDescription='An introduction to the history of electrical science, electrostatics, electromagnetism, capacitance, inductance, the International Unit System, analog and digital instruments, electric power, alternating voltage and current, energy resources, electrical generation, economic and safety aspects of power supply systems, and practical transformers.',
                    moduleLevel=1,
                    moduleWeight=20)

    moduleELE1057 = Module(moduleID='ELE1057',
                    moduleName='Signals and Communications',
                    moduleSemester=3,  # full year
                    moduleDescription='The module covers discrete and continuous time signals and systems, signal arithmetic and manipulation, transformations of independent variables, properties of systems (including linearity, time invariance, stability, memory, and causality), LTI systems, convolution, impulse response, communication systems overview, gain, attenuation, decibels, analog and digital modulation, radio receivers and transmitters, noise, transmission lines, antennas, link design equation, propagation, optical communications, and an introduction to secure communications.',
                    moduleLevel=1,
                    moduleWeight=20)
    """
    module1029 = Module(moduleID = 'CSC1029', 
                    moduleName ='Object Oriented Programming', 
                    moduleSemester = 2, 
                    moduleDescription = 'An introduction to the fundamentals of object-oriented programming with emphasis on data modeling, code reuse, and algorithm design. The module covers abstraction, encapsulation, inheritance, polymorphism, recursion, searching and sorting, data structures, and testing.', 
                    moduleLevel = 1, 
                    moduleWeight = 20) """
    
    # ADD FIRST YEAR MODULE CODE TO DATABASE HERE:
    
    
    
    # ELE & ECS Level 2 modules

    # Full year modules
    moduleELE2019 = Module(moduleID='ELE2019',
                    moduleName='Electrical Power Engineering',
                    moduleSemester=3,  # full year
                    moduleDescription='This module covers electrical machine fundamentals, '
                                      'the DC machine, the induction machine, and other machine types. '
                                      'It provides a deep dive into three-phase quantities, the per-unit system, '
                                      'synchronous generation, transmission lines, and load flow analysis. '
                                      'It also includes lab classes for hands-on learning with various machines '
                                      'and offers insights into asymmetric fault analysis. Upon completion, '
                                      'students will have a strong understanding of machine operation, power flow, '
                                      'and control, with key skills in numeric and analytical techniques.',
                    moduleLevel=2,
                    moduleWeight=20)

    moduleELE2025 = Module(moduleID='ELE2025',
                    moduleName='Embedded Systems',
                    moduleSemester=3,  # full year
                    moduleDescription='This module offers a comprehensive understanding of digital embedded '
                                      'system design using digital logic and embedded technologies. Topics include '
                                      'Boolean algebra, programmable logic technology, sequential logic, finite state '
                                      'machines, principles of VHDL-based circuit design, and embedded system design '
                                      'using 32bit ARM microcontroller. Students will acquire problem-solving skills, '
                                      'design and modeling skills, ICT skills, and C++ programming skills for embedded systems.',
                    moduleLevel=2,
                    moduleWeight=20)

    moduleELE2035 = Module(moduleID='ELE2035',
                    moduleName='Mathematics and Algorithms',
                    moduleSemester=3,  # full year
                    moduleDescription='Covering vector and matrix notations, linear systems, eigenvalues, '
                                      'eigenvectors, orthogonal vectors, Fourier series, multivariate calculus, and '
                                      'numerical solution methods, this module provides a foundation in engineering '
                                      'mathematics, probability, statistics, and algorithm implementation. Students will '
                                      'gain a fundamental understanding of modern engineering mathematics and learn to '
                                      'implement numerical algorithms efficiently in C++.',
                    moduleLevel=2,
                    moduleWeight=20)

    moduleELE2037 = Module(moduleID='ELE2037',
                    moduleName='Employability Skills and Placement Preparation',
                    moduleSemester=3,  # full year
                    moduleDescription='Designed to prepare students for placements and employment, this module enhances '
                                      'awareness of the business environment, career management issues, and key transferable '
                                      'skills. Students will develop professional practices and improve their performance '
                                      'through critical self-reflection. The module includes CV building, interview skills training, '
                                      'and interactive workshops focusing on essential employability skills.',
                    moduleLevel=2,
                    moduleWeight=0)

    moduleELE2038 = Module(moduleID='ELE2038',
                    moduleName='Signals and Control',
                    moduleSemester=3,  # full year
                    moduleDescription='This comprehensive module introduces Continuous Time (CT) and Discrete Time (DT) signals, '
                                      'their mathematical representations, transformations, and classifications. It provides a deep '
                                      'understanding of system concepts, including interconnecting CT and DT systems, memory, '
                                      'time-reversal, inversion, causality, stability, and linearity. The module also covers Linear '
                                      'Time-Invariant (LTI) systems, Fourier Transform, Z-transform, and control concepts, providing '
                                      'a solid foundation in signals and control theory.',
                    moduleLevel=2,
                    moduleWeight=20)

    moduleECS2039 = Module(
                    moduleID='ECS2039',
                    moduleName='Digital Systems',
                    moduleSemester=3,  # full year
                    moduleDescription='Digital Systems is an advanced course aimed at providing students with a comprehensive understanding '
                                    'and application of digital system design through hands-on hardware circuit design and programming '
                                    'with Verilog HDL. The module encompasses a detailed study of complex digital system design, '
                                    'with an application-based approach in the second semester. Topics covered include Technologies '
                                    '(Processors, GPU, AI processor, PLDs, ASIC, FPGAs), Hardware Description Language (Verilog), '
                                    'Sequential and Multiple-output Circuits, as well as Fault Detection and Design for Testability. '
                                    'Students will engage with various technical design exercises and a project to apply their learning '
                                    'in real-world digital applications, gaining valuable practical and analytical skills in the process.',
                    moduleLevel=2,
                    moduleWeight=20
)

    moduleELE2040 = Module(
                    moduleID='ELE2040',
                    moduleName='Communications',
                    moduleSemester=3,  # full year
                    moduleDescription='Communications is a critical undergraduate module that offers students a robust understanding of '
                                'electromagnetics, antennas, and wireless communication principles. The module is divided into two parts; '
                                'the first part provides fundamental knowledge on Electromagnetics and Antennas, while the second '
                                'part delves deep into Wireless Communication. Through engaging sessions and practical labs using '
                                'MATLAB and Simulink, students will acquire the necessary skills to understand, analyze, and design '
                                'antennas, electromagnetic fields, and modern digital communication systems, thereby gaining a '
                                'solid grounding in the field of Communications.',
                    moduleLevel=2,
                    moduleWeight=20
)

    moduleELE2041 = Module(
                    moduleID='ELE2041',
                    moduleName='Electronics and Circuits',
                    moduleSemester=3,  # full year
                    moduleDescription='The Electronics and Circuits module provides students with foundational knowledge and skills in '
                                    'electronic circuits and devices. It consists of two primary sections: Circuits and Electronics. The '
                                    'Circuits section introduces students to system equations, linear circuits, circuit analysis theorems and '
                                    'methods, two-port networks, and Laplace transform applications in circuit analysis. The Electronics '
                                    'section explores various semiconductor devices and applications, including operational amplifiers, diodes, '
                                    'transistors, and their respective applications in circuit design and analysis. Students will engage '
                                    'with SPICE simulation software, producing equivalent circuits, understanding semiconductor devices, and '
                                    'designing analogue circuits for real-world applications.',
                    moduleLevel=2,
                    moduleWeight=20
)

    """
    module2059 = Module(moduleID='CSC2059',
                    moduleName='Data Structures and Algorithms',
                    moduleSemester=1,  # first semester
                    moduleDescription='',
                    moduleLevel=2,
                    moduleWeight=20)
                    """
    """
    # Second semester modules
    # CS Modules that CAN BE DONE BY EE students 
    module2056 = Module(moduleID='CSC2056',
                    moduleName='Systems Security and Cryptography',
                    moduleSemester=2,  # second semester
                    moduleDescription='',
                    moduleLevel=2,
                    moduleWeight=20)

    module2062 = Module(moduleID='CSC2062',
                    moduleName='Introduction to AI and Machine Learning',
                    moduleSemester=2,  # second semester
                    moduleDescription='',
                    moduleLevel=2,
                    moduleWeight=20) """
    
    #ADD SECOND YEAR MODULE CODE TO DATABASE HERE:


    # ELE & ECS Level 3 modules

    moduleELE3001 = Module(moduleID='ELE3001',
                    moduleName='Project',
                    moduleSemester=3,  # full year
                    moduleDescription='An investigation or design study in various branches of electrical and electronic engineering. The project incorporates elements of design, manufacture, and testing, even for software-based projects.',
                    moduleLevel=3,
                    moduleWeight=40)

    moduleECS3003 = Module(moduleID='ECS3003',
                    moduleName='Connected Health',
                    moduleSemester=3,  # full year
                    moduleDescription='This course focuses on the Connected Health model which uses technology for healthcare delivery remotely. The module examines technology’s role in healthcare, covering topics like the evolution of Connected Health, Tele-health, medical electronics and sensors, personal health data networks, electronic patient records, data management, standards, and regulations.',
                    moduleLevel=3,
                    moduleWeight=20)

    moduleELE3037 = Module(moduleID='ELE3037',
                    moduleName='High Frequency Systems Techniques',
                    moduleSemester=3,  # full year
                    moduleDescription='Offers knowledge and skills for designing high-frequency electronic systems and circuits. Covers noise theory, antenna techniques, nonlinear circuits, satellite systems, transmission line theory, microwave circuit design, impedance matching, amplifier design, and practical design exercises.',
                    moduleLevel=3,
                    moduleWeight=20)

    moduleELE3039 = Module(moduleID='ELE3039',
                    moduleName='Electrical Power and Energy',
                    moduleSemester=3,  # full year
                    moduleDescription='Provides deep understanding of synchronous generators, steady-state and dynamic operations, system stability and control, transmission line parameters, overcurrent protection, fault analysis, embedded generation, and DC transmission.',
                    moduleLevel=3,
                    moduleWeight=20)

    moduleELE3040 = Module(moduleID='ELE3040',
                    moduleName='Networks and Communications Protocols',
                    moduleSemester=3,  # full year
                    moduleDescription='Foundational knowledge in networks and communication protocols, covering OSI layers, error detection, queuing theory principles, MAC Layer, TCP/IP, physical layer principles, and high spectrally-efficient techniques for cellular systems.',
                    moduleLevel=3,
                    moduleWeight=20)

    moduleELE3041 = Module(moduleID='ELE3041',
                    moduleName='Signal Processing and Communications',
                    moduleSemester=3,  # full year
                    moduleDescription='Focuses on signal processing and communication systems, with emphasis on discrete-time signals, Fourier analysis, adaptive filtering, Laplace transform, stochastic signal processing, digital modulation, and channel coding.',
                    moduleLevel=3,
                    moduleWeight=20)

    moduleELE3042 = Module(moduleID='ELE3042',
                    moduleName='Control Systems Engineering',
                    moduleSemester=3,  # full year
                    moduleDescription='Imparts understanding of classical control systems and digital feedback control methods, with hands-on experience in designing and implementing real-time control systems, especially in robotics.',
                    moduleLevel=3,
                    moduleWeight=20)

    moduleELE3043 = Module(moduleID='ELE3043',
                    moduleName='BEng Engineering Entrepreneurship',
                    moduleSemester=3,  # full year
                    moduleDescription='Introduces enterprise and entrepreneurship with focus on startup processes, intellectual property, funding, branding, product and business development.',
                    moduleLevel=3,
                    moduleWeight=20)

    # NOT SURE WHETHER TO REMOVE OR NOT
    """
    module3044 = Module(moduleID='ELE3044',
                    moduleName='MEng Engineering Entrepreneurship',
                    moduleSemester=3,  # full year
                    moduleDescription='',
                    moduleLevel=3,
                    moduleWeight=40)
    """

    moduleELE3045 = Module(moduleID='ELE3045',
                    moduleName='Power Electronics and Motor Drives',
                    moduleSemester=3,  # full year
                    moduleDescription='Introduction to power electronics, focusing on power semiconductor devices, switched RLC circuits, DC/DC converters, DC power supplies and drives, PWM inverters, thyristor circuits, controlled rectifiers, AC voltage controllers, and AC motor drives.',
                    moduleLevel=3,
                    moduleWeight=20)

    moduleELE3046 = Module(moduleID='ELE3046',
                    moduleName='Advanced Electronics',
                    moduleSemester=3,  # full year
                    moduleDescription='Advanced concepts of analog circuit design, including device physics, second-order effects, transistor configurations, differential pairs, feedback circuits, frequency response, filter design, and basic noise analysis.',
                    moduleLevel=3,
                    moduleWeight=20)
    

    #CS MODULES THAT CAN BE done by EE students
    """
    module3021 = Module(moduleID='CSC3021',
                    moduleName='Concurrent Programming',
                    moduleSemester=1,  # first semester
                    moduleDescription='',
                    moduleLevel=3,
                    moduleWeight=20)

    module3067 = Module(moduleID='CSC3067',
                    moduleName='Video Analytics and Machine Learning',
                    moduleSemester=1,  # first semester
                    moduleDescription='',
                    moduleLevel=3,
                    moduleWeight=20)

    module3059 = Module(moduleID='CSC3059',
                    moduleName='Malware Analysis',
                    moduleSemester=2,  # second semester
                    moduleDescription='',
                    moduleLevel=3,
                    moduleWeight=20)

    module3066 = Module(moduleID='CSC3066',
                    moduleName='Deep Learning',
                    moduleSemester=2,  # second semester
                    moduleDescription='',
                    moduleLevel=3,
                    moduleWeight=20)
    """


#ADD THIRD (FINAL) YEAR MODULE CODE TO DATABASE HERE:


# ELE & ECS Level 4 modules


    moduleELE4001 = Module(moduleID='ELE4001',
                       moduleName='Project 4',
                       moduleSemester=3,  # full year
                       moduleDescription='The project normally takes the form of an investigation or design study concerned with one of the various branches of electrical and electronic engineering. The project originator typically endeavours to ensure an element of design, manufacture and test in the project specification, even if the project is software-based.',
                       moduleLevel=4,
                       moduleWeight=40)

    moduleECS4002 = Module(moduleID='ECS4002',
                       moduleName='Wireless Sensor Systems',
                       moduleSemester=3,  # full year
                       moduleDescription='Introduction to sensor systems, with a focus on wireless technologies. Topics include Zigbee, 6LoWPAN, 802.11 MAC layer, low power WSN MACs, IoT technologies, routing for WSN, power management, synchronization, and localization.',
                       moduleLevel=4,
                       moduleWeight=20)

    moduleELE4009 = Module(moduleID='ELE4009',
                       moduleName='Wireless Communications',
                       moduleSemester=3,  # full year
                       moduleDescription='This course provides an understanding of the concepts and techniques used in modern wireless communication systems, covering cellular systems, propagation modeling, spectrum management, multiuser systems, multiple antennas techniques, multicarrier communications, and cognitive radio techniques.',
                       moduleLevel=4,
                       moduleWeight=20)

    moduleELE4023 = Module(moduleID='ELE4023',
                       moduleName='Control Methods for Cyber-Physical Systems',
                       moduleSemester=3,  # full year
                       moduleDescription='The module focuses on the analysis and control of dynamical systems, with an emphasis on cyber-physical systems. It covers continuous time systems, discrete-time systems, hybrid dynamical systems, simulation, stability analysis, estimation, and control of dynamical systems.',
                       moduleLevel=4,
                       moduleWeight=20)

    moduleELE4024 = Module(moduleID='ELE4024',
                       moduleName='Robotics and Intelligent Systems',
                       moduleSemester=3,  # full year
                       moduleDescription='Introduction to core aspects of robotics and intelligent techniques. The module covers robot kinematics, dynamics, control systems, vision systems, force-based control, manufacturing robots, machine learning, neural networks, and fuzzy logics.',
                       moduleLevel=4,
                       moduleWeight=20)

    moduleELE4025 = Module(moduleID='ELE4025',
                       moduleName='Sustainable Energy and Smart Grids',
                       moduleSemester=3,  # full year
                       moduleDescription='Overview of sustainable energy resources and smart grid technologies. Topics include load frequency control, system non-synchronous penetration, demand side management, battery energy storage, electric vehicles, substation automation, telecommunications, phasor measurement units, power quality, design & deployment, market liberalization, and renewable energy integration.',
                       moduleLevel=4,
                       moduleWeight=20)


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

    moduleECS4003 = Module(moduleID = 'ECS4003', 
                    moduleName ='Advanced Computer Engineering', 
                    moduleSemester = 3, 
                    moduleDescription = "This course covers streaming workload modeling languages, algorithm optimization schemes, handling of time in algorithm design, number systems, high-level synthesis for FPGAs, application partitioning for parallel processing, and system optimization.",
                    moduleLevel = 4, 
                    moduleWeight = 20)  # Not a mistake - module is full year and 20 cats

    ##ADD Level 4 Modules
    mod4_list = [module4003, moduleECS4003, module4006, module4008, module4009, module4010]
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

if __name__ == "__main__":
    addComputerSciencePathways()
    addComputerScienceModules()
    addComputerSciencePathwayModuleLinks()
    addModuleDescriptions()