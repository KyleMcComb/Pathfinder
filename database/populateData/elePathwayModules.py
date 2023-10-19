from database.models import *

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
    
    # ADD FIRST YEAR MODULE CODE TO DATABASE HERE:
    mod1_list = [moduleECS1001, moduleECS1005, moduleECS1006, moduleELE1012, moduleELE1056, moduleELE1057]
    for a in mod1_list:
        a.save()
    
    
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

    
    #ADD SECOND YEAR MODULE CODE TO DATABASE HERE:
    mod2_list = [moduleELE2019, moduleELE2025, moduleELE2035, moduleELE2037, moduleELE2038, moduleECS2039, moduleELE2040, moduleELE2041]
    for a in mod2_list:
        a.save()

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

    moduleELE3044 = Module(moduleID='ELE3044',
                    moduleName='MEng Engineering Entrepreneurship',
                    moduleSemester=3,  # full year
                    moduleDescription='An introductory course on enterprise and entrepreneurship in engineering. Covers the startup process, intellectual property, funding opportunities, branding, and business consultancy approaches. Engages students in hands-on activities such as product development, team-building, marketing strategies, and financial planning. Enhances skills in report writing, business presentations, idea generation, business pitch, and product development. Prior knowledge of "ELE2036 Professional Engineering & Innovation" is required.',
                    moduleLevel=3,
                    moduleWeight=40)

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


#ADD THIRD (FINAL) YEAR MODULE CODE TO DATABASE HERE:
    mod3_list = [moduleELE3001, moduleECS3003, moduleELE3037, moduleELE3039, moduleELE3040, moduleELE3041, moduleELE3042, moduleELE3043, moduleELE3044, moduleELE3045, moduleELE3046]
    for a in mod3_list:
        a.save()


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
    
    moduleECS4003 = Module(moduleID = 'ECS4003', 
                    moduleName ='Advanced Computer Engineering', 
                    moduleSemester = 3, 
                    moduleDescription = "This course covers streaming workload modeling languages, algorithm optimization schemes, handling of time in algorithm design, number systems, high-level synthesis for FPGAs, application partitioning for parallel processing, and system optimization.",
                    moduleLevel = 4, 
                    moduleWeight = 20)  # Not a mistake - module is full year and 20 cats

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
    
    mod4_list = [moduleELE4001, moduleECS4002, moduleECS4003, moduleELE4009, moduleELE4023, moduleELE4024, moduleELE4025]
    for a in mod4_list:
        a.save()


if __name__ == "__main__":
    addEEModules()