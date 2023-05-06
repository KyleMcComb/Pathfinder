# CSC3068-Pathfinder
This README includes an introduction to the project (what the project is along with what technologies were used to build it), how to set up the system (the steps needed to execute the code either with docker or a virtual environment) and account information to log into the system.

## Introduction

### Project Description
This project is the prototype for the system which our team (Dean Logan, Conor Nugent, Kyle McComb & Ross McAllister) is building for our final year project, this was completed as part of the module CSC3068. 

This is a website (built using the Django framework) that will aid students in picking their modules through the use of a chatbot. The website will also store the students grade information to help them track their degree progression along with giving students an easy way of finding out all the modules within EEECS. More information within Product Vision.

### Technologies Used
* Python 3.7.9
* Django >=3.2, <3.3
* Chatterbot 1.0.8
* Spacy 3.2.0 (English language model)
* Sass (for css)

### Product Vision

To create a system (Pathfinder) that will assist students in delivering information about modules that are available to them along with relevant career information for these modules. This will be done using a chatbot that will aid students in picking modules based on information provided by the student (likes/dislikes, career choices, etc), improving student satisfaction. 

Students will also be able to search and filter all modules within EEECS on a separate page where they will be able to see information on all modules. The motivation for adding this feature is to aid students in the event they wish to switch pathway so they can investigate the modules for other pathways in an easier manner than looking through a lengthy PDF.

Pathfinder will also provide a dashboard for students that will display information relating to their grades throughout their time at Queen’s (overall degree percentage, module grades, assessment grades and useful statistics). The motivation for adding this feature is to help students track their progress throughout their degree, motivating students to work harder to obtain a better grade. It also gives students an easier way to view how well they are progressing throughout their degree.


## Set Up 
(Note: the terminal commands are surrounded by “” do not enter these into the terminal)
### Docker
1.	Clone the repository to your system.
2.	[Install Docker Desktop](https://www.docker.com/products/docker-desktop/)
3.	Open a terminal window then navigate to the directory where the project has been cloned to, make sure to open into the Pathfinder file (open the folder CSC3068-Pathfinder\Pathfinder).
4.	Then run the following command to build the image “docker build -t csc3068pathfinder .”
### Virtual Environment
1.	Clone the repository to your system.
2.	[Install Python 3.7.9](https://www.python.org/downloads/release/python-379/)
3.	Open a terminal window then navigate to the directory where the project has been cloned to (open the folder CSC3068-Pathfinder).
4.	Then in the terminal create a virtual environment by running the following command “<directory to python install that was installed in step 1> -m venv .”.
5.	Then to activate the script run the following command “.\Scripts\activate”.
6.	Once this is done install the packages by entering the following command into the terminal “pip install -r .\Pathfinder\requirements.txt” (keep this terminal open).
7.	Then within file explorer navigate to where the repository was cloned to, go into the Pathfinder folder (CSC3068-Pathfinder), now copy the tagging.py file.
8.	Now find the tagging.py file within the chatterbot package using file explorer (directory is as follows CSC3068-Pathfinder\Lib\site-packages\chatterbot) once you’re in this directory replace the tagging.py file found here with the tagging.py file you copied from the Pathfinder folder.
9.	Once this file has been replaced go back to the terminal and run the following command “python -m spacy download en_core_web_sm”.

## Running The Project
### Docker
1.	Navigate to the repository within a terminal window then open the Pathfinder folder (CSC3068-Pathfinder\Pathfinder).
2.	Create a container for the project to run in by entering this command into the terminal “docker run –name pathfinderContainer -p 8080:8000 -d csc3068pathfinder”
3.	Now you can navigate to http://localhost:8080/ (or whichever port you have specified the container to run in) to view the website.

### Virtual Environment
1.	Navigate to the repository within a terminal window then open the Pathfinder folder (CSC3068-Pathfinder\Pathfinder).
2.	In the terminal run the following command “.\Scripts\activate”.
3.	In the terminal run the following command “python .\Pathfinder\manage.py runserver”.
4.	Now you can navigate to http://localhost:8000/ (or whichever port you have specified the container to run in) to view the website.
## Accounts

There are 2 access levels to the system “admin” and “student”. Admin accounts has access to the database through the admin panel and have full access to all data, student accounts do not have access to the admin panel, they can see personalised information on the grade dashboard page.

* Admin Account 
  * Student Number: admin
  * Password: admin
* Student Account 1
  * Student Number: 40294254
  * Password: 8characters
* Student Account 2
  * Student Number: 40191566
  * Password: b450ma11
* Student Account 3
  * Student Number: 40291577
  * Password: b550ma11


