@ECHO OFF

@ECHO Activating the virtual environment...
CALL venv\Scripts\activate

@ECHO Installing python packages:
pip install -r requirements.txt

@ECHO Successfully installed packages!
cls

@ECHO Running the application...

python -i app.py

pause
exit 0



