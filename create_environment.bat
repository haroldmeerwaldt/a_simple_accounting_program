@echo off
echo This program will create a virtual environment and install the required packages
echo Some steps may take 1-2 minutes without showing output
echo:
echo This program requires Python 3.8 or higher to run.
echo Your Python installation has the following Python version and location
python --version
python -c "import sys; print(sys.executable)"
echo:
echo If this version is below 3.8, please download a higher Python version at https://www.python.org/downloads/
echo To abort, press ctrl+C, otherwise press any other key.
pause
python -m venv env
echo ... Virtual environment created at .\env
.\env\Scripts\python -m pip install --upgrade pip
echo ... Pip upgraded
.\env\Scripts\python -m pip install -r requirements.txt
echo ... Virtual environment and necessary packages installed successfully
pause