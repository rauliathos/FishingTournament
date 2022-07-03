# Welcome to the Fishing Tournament Registration Form App

You can register a Team name, Team email and check if the team has paid the entry fee.
Once the Team has paid the entry fee, it can be accessed in the Catches database.
You can register a catch by adding a team, the fish species and the catch weight.
You can also see all the teams or all catches.

## Starting the app
## Install Python
### Windows/MacOS
Install Python on your computer by going to:
https://www.python.org/download

The version should be Python 3.6 or greater.

Download and Run the installer ensuring you check the Add Python to PATH option at the bottom.

### Linux (Debian/Ubuntu)

To install Python on either Debian or Ubuntu, you will need to open up a terminal. From here, you can type the following commands:


**sudo apt update**

**sudo apt install python3 -y**


### This tutorial assumes you are working on an Ubuntu VM, at least version 18.04 LTS.

Fork/clone the repoository.
use any IDE to open the cloned repo and open the bash terminal:
#### First, install apt dependencies:

**sudo apt install python3 python3-venv python3-pip**

Make your current directory is _/application_
#### We now need to create a Python virtual environment to install our pip requirements in:
 
 **python3 -m venv venv**
 
**source venv/bin/activate**

#### Install requirements.txt 

**pip3 install -r requirements.txt**

## Run the App
### Now create your database's schema by running:

**python3 create.py**
### And run the app with the command:

**python3 app.py**

## Clean Up
### To stop your Flask application running, navigate back to your terminal and press __ Ctrl+C__ You should now have control over your terminal again.

#### To deactivate the virtual environment, run:

**deactivate**
#### If you wish to delete the virtual environment, run:

**rm -rf venv**
