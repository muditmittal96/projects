# Luigi Assignment

This program was designed in response to a data engineering internship coding challenge. The task was to build a successful pipeline using the Python Module Luigi and SQLAlchemy to get data from a excel spreadsheet and store it in a SQLite database.

The program follows a logical data pipeline workflow:

1.  read the 'dictionary' and 'prices' sheets from the 'data.xlsm' spreadsheet in the data folder
2.  create 'task.db'  (this should happen automatically)
3.  upload the 'dictionary' and 'price' data to 'task.db'
4.  the program will be executed by running from the command prompt:

        (env):> python -m main


## Build

1.  Decompress this archive
2.  Create a python virtual environment.
3.  Go to this directory in the command line and activate the python environment. 
4.  Install the python dependencies into the environemnet by typing from the    
    command prompt:

            (env):> pip install -r requirements.txt

5.  Install this library in developer mode:

            (env):> pip setup.py build
            (env):> pip install -e .