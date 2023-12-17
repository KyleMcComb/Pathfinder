# Pathfinder
This README includes a project description (what the project is along with what technologies were used to build it), how to set up the system (the steps needed to execute the code either with docker or a virtual environment), and account information to log into the system.

## Contents

* [Project Description](#project-description)
* [Set Up](#set-up)
  * [Docker](#docker)
  * [Virtual Environment](#virtual-environment)
  * [Populating the database from scratch](#populate-database)
* [Running The Project](#running-the-project)
  * [Docker (Creating a container)](#docker-creating-a-container)
  * [Virtual Environment](#virtual-environment-1)
* [Cloud Backup Storage](#cloud-backup-storage)
  * [Azurite for Local Azure Storage Emulation](#azurite-for-local-azure-storage-emulation)
    * [Setting Up Azurite](#setting-up-azurite)
    * [Running Azurite](#running-azurite-1)
  * [Using your own Azure Blob Storage](#using-your-own-azure-storage-account)
* [Accounts](#accounts)
* [Useful Links](#useful-links)

## Project Description

This project is a prototype for a system called Pathfinder that will assist students in selecting modules based on their preferences and relevant career information. The system will use a chatbot built with the Django framework and Chatterbot 1.0.8. Students will also be able to search and filter all modules within EEECS on a separate page and access a dashboard to track their grades throughout their degree. The project was completed as part of the module CSC3068 and the technologies used include Python 3.7.9, Django >=3.2, <3.3, Spacy 3.5.0 (English language model), Sass (for CSS) and Azurite (for Azure storage emulation through a docker container).
The group for this project is as follows: Dean Logan, Conor Nugent, Ross McAllister & Kyle McComb.


## Set Up 
(Note: at the bottom of this README are some links to resources that might help you use Docker or Virtual Environments if this is your first time using these)
### Docker
1.	Clone the repository to your system.
2.	[Install Docker Desktop](https://www.docker.com/products/docker-desktop/) on your computer if it has not already been installed.
3.	Open a terminal window then navigate to the directory where the project has been cloned to, the folder should be called CSC3068-Pathfinder.
4.	Then run the following command to build the image ```docker-compose up -d```

### Virtual Environment
1.  Clone the repository to your computer.
2.  [Install Python 3.7.9](https://www.python.org/downloads/release/python-379/) on your computer if it has not already been installed.
3.  Open a terminal window (PowerShell if you're on Windows) on your computer and navigate to the directory where the project has been cloned to. To do this, open the folder where you extracted the repository, then right-click on the folder called "CSC3068-Pathfinder" and choose "Open in Terminal" (for Linux/Mac) or "Open Powershell window here" (for Windows).
4.  In the terminal, create a virtual environment by running the following command, replacing "<directory to python install>" with the directory where Python 3.7.9 was installed: ```<directory to python install>\python.exe -m venv .```. For example, if Python 3.7.9 was installed in ```C:\Python37```, the command would be: ```C:\Python37\python.exe -m venv .```.
5.  Activate the virtual environment by running the following command: ```.\Scripts\activate``` (for Windows) or ```source bin\activate``` (for Linux/Mac).
6.  Install the required packages by entering the following command into the terminal: ```pip install -r requirements.txt``` (keep this terminal open).
7.  Open a file manager on your computer and navigate to the folder where you extracted the repository. Then go into the "CSC3068-Pathfinder" folder and copy the "tagging.py" file.
8.  In a file manager, navigate to the following directory: "CSC3068-Pathfinder\Lib\site-packages\chatterbot". Replace the "tagging.py" file found in this directory with the "tagging.py" file you copied from the "CSC3068-Pathfinder" folder. Alternatively you can navigate back to the terminal and enter the following ```cp -f tagging.py venv/lib/python3.x/site-packages/chatterbot/tagging.py``` (for MacOS/Linux) or ```Copy-Item -Path "tagging.py" -Destination ".\venv\Lib\site-packages\chatterbot\tagging.py" -Force``` (for Windows).
9.  If you wish to have the cloud backup storage functionality (which is not required for the rest of the system to work), please follow the set up steps outlined [here](#setting-up-azurite).

### Populate Database

If you have wiped the database or the database is completey empty use these commands to populate with some starting data.

1. In the directory path enter the command ```python manage.py shell```
2. ```>>> from database.models import *```

Adding Pathways for EEECs (excludes BIT)
1. ```>>> from database.populateData import pathways```
2. ```>>> pathways.addPathways()```
3. To view database: ```>>> Pathway.objects.all()```

Next add CSC modules
1. ```>>> from database.populateData import cscPathwayModules```
2. ```>>> cscPathwayModules.addComputerScienceModules()```
3. To view database: ```>>> Module.objects.all()```

Next add ELE modules
1. ```>>> from database.populateData import elePathwayModules```
2. ```>>> elePathwayModules.addEEModules()```
3. To view database: ```>>> Module.objects.all()```

Next add the assessments to each CSC module
1. ```>>> from database.populateData import cscAssessments```
2. ```>>> cscAssessments.addAssessments()```
3. To view database: ```>>> Assessment.objects.all()```

Next add the assessments to each ELE module
1. ```>>> from database.populateData import eleAssessments```
2. ```>>> eleAssessments.addAssessments()```
3. To view database: ```>>> Assessment.objects.all()```

Next add the links from each pathway to their modules
1. ```>>> from database.populateData import pathwayModuleLinks```
2. ```>>> pathwayModuleLinks.addPathwayModuleLinks()```
3. To view database: ```ModulePathway.objects.all()```

Next add the lecturers
1. ```>>> from database.populateData import lecturers```
2. ```>>> lecturers.addLecturers()```
3. ```>>> lecturers.addLecturersToModules()```
4. To view database: ```Lecturer.objects.all()```

## Running The Project
### Docker (Creating a container)
1.	Open a terminal window then navigate to the directory where the project has been cloned to, the folder should be called CSC3068-Pathfinder.
2.	Then run the following command this will build the images and run the corresponding containers ```docker-compse up -d```
3.	Now you can navigate to http://localhost:8080/ to view the website.

### Virtual Environment
1.	Open a terminal window then navigate to the directory where the project has been cloned to, the folder should be called CSC3068-Pathfinder.
2.  If you wish to have the Azurite Emulator running for cloud storage see the steps [here](#running-azurite), if you want to run the system without cloud storage please skip this step and proced to step 3.
3.	In the terminal run the following command ```.\Scripts\activate```.
4.	In the terminal run the following command ```python manage.py runserver```.
5.	Now you can navigate to http://localhost:8000/ (or whichever port you have specified the container to run in) to view the website.

## Cloud Backup Storage
In this project, Azurite is employed to simulate a cloud-based backup solution. The system is fully functional even without cloud storage emulation. If you do not have Docker installed, prefer not to install it, or do not possess your own Azure Storage Account (and do not wish to acquire one), you may skip the instructions provided in this section.

The following content provides insights into Azurite: what it is, its typical use cases, the rationale behind its usage in this project, and instructions on how to utilize it effectively. Additionally, we have included step-by-step guides on setting up Azurite and running it. Furthermore, instructions are available on how to integrate your own Azure Storage Account, should you choose to do so.

### Azurite for Local Azure Storage Emulation
[Azurite](https://github.com/Azure/Azurite) is an open-source, cross-platform Azure Storage emulator that allows you to develop and test Azure Storage applications locally. It provides an efficient way to emulate Azure Storage services, such as Blob, Queue, and Table storage, without the need for an actual Azure subscription.

- **Local Development**: Azurite enables you to develop and test your Azure Storage-dependent applications locally, reducing the need for an active internet connection or an Azure subscription during development.

- **Cost-Efficiency**: It eliminates potential costs associated with using actual Azure resources for development and testing purposes.

While Azurite serves as a valuable emulator for local development, it's important to emphasize that it is not a replacement for a cloud-based backup solution. In the context of this University project, Azurite was chosen to demonstrate our ability to leverage cloud technologies without incurring any associated costs. However, it's crucial to note that for production environments, a comprehensive cloud-based backup strategy should be implemented for data security and redundancy.

#### Setting Up Azurite
(Note: The below steps are only necassary if you wish to use the system with a [Virtual Environment](#virtual-environment), if you are using [Docker](#docker) this is not necassary)

Before you start using Azurite, make sure you have [Docker](https://www.docker.com/products/docker-desktop/) installed on your system, as Azurite is available as a Docker container.

1. Pull the Azurite Docker Image, open a terminal window and run the following command to pull the Azurite Docker image ```docker pull mcr.microsoft.com/azure-storage/azurite```.
2. To create a container from this image, within the terminal, run the following command ```docker run -d -p 10000:10000 -p 10001:10001 -p 10002:10002 --name azurite-storage-pathfinder mcr.microsoft.com/azure-storage/azurite```.


#### Running Azurite
1. To run the container created in [Setting Up Azurite](#setting-up-azurite), open a terminal window and run the following command ```docker start azurite-storage-pathfinder```.


### Using your own Azure Storage Account
1. Open up a file manager and navigate to the local repository of this project, once here open the "backups" folder then in your prefered IDE open "azureBlobStorage.py". 
2. Once in this file chagne the variable CONNECTION_STRING to the connection string for the Azure Blob Storage service you wish to use instead. If you do not have a connection string for you storage account see the tutorial [here](https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string) for help.
3. If you wish you can also change the CONTAINER_NAME variable to a different container within your Blob. If the CONTAINER_NAME variable is set to a container that does not yet exists within your container, do not worry as the system will create this container automtically for you.


## Accounts

There are 2 access levels to the system “admin” and “student”. Admin accounts have access to the database through the admin panel and have full access to all data, student accounts do not have access to the admin panel, they can see personalised information on the grade dashboard page.

* Admin Account 
  * Student Number: admin
  * Password: admin
* Student Account 1
  * Student Number: 40294254 (Note this account currently has 2FA enabled, so unless you have the TOTP you cannot login)
  * Password: 8characters
* Student Account 2
  * Student Number: 40191566
  * Password: b450ma11
* Pathfinder Email Account:
  * Email Address: pathfinder3068@gmail.com
  * Password: PageRank12*

### Scrapy spiders
scrapy runspider .\webScraping\spiders\IndeedJobSpider.py

## Useful Links
Below are some links that might be helpful in creating/running docker containers and virtual environments if this is the first time using these resources. If you have used Docker or Virtual Environments before or are familiar with similar technologies these resources can be ignored.
* [Download Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Getting Started Tutorial](https://github.com/docker/getting-started)
* [Overview of Docker Build Docker Documentation](https://docs.docker.com/build/)
* [Containerize an application Docker Documentation](https://docs.docker.com/get-started/02_our_app/)
* [Creation of virtual environments Python Documentation](https://docs.python.org/3.7/library/venv.html)
* [How to Set Up a Virtual Environment in Python – And Why It's Useful By freecodecamp.org](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
* [How to create a Python virtual environment for a new project - IDG TECHtalk Youtube Channel](https://www.youtube.com/watch?v=ohlRbcasPAc)
* [Azurite Github Page](https://github.com/Azure/Azurite)
* [Configure Azure Storage connection strings](https://learn.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string)
