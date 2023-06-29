# Pathfinder
This README includes a project description (what the project is along with what technologies were used to build it), how to set up the system (the steps needed to execute the code either with docker or a virtual environment), and account information to log into the system.

## Project Description

This project is a prototype for a system called Pathfinder that will assist students in selecting modules based on their preferences and relevant career information. The system will use a chatbot built with the Django framework and Chatterbot 1.0.8. Students will also be able to search and filter all modules within EEECS on a separate page and access a dashboard to track their grades throughout their degree. The project was completed as part of the module CSC3068 and the technologies used include Python 3.7.9, Django >=3.2, <3.3, Spacy 3.2.0 (English language model), and Sass (for CSS).
The group for this project is as follows: Dean Logan, Conor Nugent, Ross McAllister & Kyle McComb.


## Set Up 
(Note: at the bottom of this README are some links to resources that might help you use Docker or Virtual Environments if this is your first time using these)
### Docker
1.	Clone the repository to your system.
2.	[Install Docker Desktop](https://www.docker.com/products/docker-desktop/) on your computer if it has not already been installed.
3.	Open a terminal window then navigate to the directory where the project has been cloned to, make sure to open into the Pathfinder file (open the folder CSC3068-Pathfinder\Pathfinder).
4.	Then run the following command to build the image ```docker build -t csc3068pathfinder .```
### Virtual Environment
1.  Clone the repository to your computer.
2.  [Install Python 3.7.9](https://www.python.org/downloads/release/python-379/) on your computer if it has not already been installed.
3.  Open a terminal window on your computer and navigate to the directory where the project has been cloned to. To do this, open the folder where you extracted the repository, then right-click on the folder called "CSC3068-Pathfinder" and choose "Open in Terminal" (for Linux/Mac) or "Open Powershell window here" (for Windows).
4.  In the terminal, create a virtual environment by running the following command, replacing "<directory to python install>" with the directory where Python 3.7.9 was installed: ```<directory to python install>\python.exe -m venv .```. For example, if Python 3.7.9 was installed in ```C:\Python37```, the command would be: ```C:\Python37\python.exe -m venv .```.
5.  Activate the virtual environment by running the following command: ```.\Scripts\activate``` (for Windows) or ```source bin/activate``` (for Linux/Mac).
6.  Install the required packages by entering the following command into the terminal: ```pip install -r .\Pathfinder\requirements.txt``` (keep this terminal open).
7.  Open File Explorer on your computer and navigate to the folder where you extracted the repository. Then go into the "CSC3068-Pathfinder" folder and copy the "tagging.py" file.
8.  In File Explorer, navigate to the following directory: "CSC3068-Pathfinder\Lib\site-packages\chatterbot". Replace the "tagging.py" file found in this directory with the "tagging.py" file you copied from the "CSC3068-Pathfinder" folder.
9.  Go back to the terminal and run the following command to download a required package: ```python -m spacy download en_core_web_sm```. Once the download is complete, you can close the terminal.

## Running The Project
### Docker (Creating a container)
(Note: if a container has already been created from the image made in Set Up then just run that container, [more help here](https://docs.docker.com/engine/reference/commandline/container_run/). If a container has already been created skip to step 3).
1.	Navigate to the repository within a terminal window then open the Pathfinder folder (CSC3068-Pathfinder\Pathfinder).
2.	Create a container for the project to run in by entering this command into the terminal ```docker run -p 8080:8000 -d csc3068pathfinder```.
3.	Now you can navigate to http://localhost:8080/ (or whichever port you have specified the container to run in) to view the website.

### Virtual Environment
1.	Navigate to the repository within a terminal window then open the Pathfinder folder (CSC3068-Pathfinder\Pathfinder).
2.	In the terminal run the following command ```.\Scripts\activate```.
3.	In the terminal run the following command ```python .\Pathfinder\manage.py runserver```.
4.	Now you can navigate to http://localhost:8000/ (or whichever port you have specified the container to run in) to view the website.
## Accounts

There are 2 access levels to the system “admin” and “student”. Admin accounts have access to the database through the admin panel and have full access to all data, student accounts do not have access to the admin panel, they can see personalised information on the grade dashboard page.

* Admin Account 
  * Student Number: admin
  * Password: admin
* Student Account 1
  * Student Number: 40294254
  * Password: 8characters
* Student Account 2
  * Student Number: 40191566
  * Password: b450ma11
  

## Useful Links
Below are some links that might be helpful in creating/running docker containers and virtual environments if this is the first time using these resources. If you have used Docker or Virtual Environments before or are familiar with similar technologies these resources can be ignored.
* [Docker Getting Started Tutorial](https://github.com/docker/getting-started)
* [Overview of Docker Build Docker Documentation](https://docs.docker.com/build/)
* [Containerize an application Docker Documentation](https://docs.docker.com/get-started/02_our_app/)
* [Creation of virtual environments Python Documentation](https://docs.python.org/3.7/library/venv.html)
* [How to Set Up a Virtual Environment in Python – And Why It's Useful By freecodecamp.org](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
* [How to create a Python virtual environment for a new project - IDG TECHtalk Youtube Channel](https://www.youtube.com/watch?v=ohlRbcasPAc)
