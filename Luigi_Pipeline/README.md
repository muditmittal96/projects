# Introduction

The task is to complete the classes: 

    InsertDictionaryTask()
    InsertPricesTask()

in the main.py module.

The program needs to:

1.  read the 'dictionary' and 'prices' sheets from the 'data.xlsm' spreadsheet in the data folder
2.  create 'task.db'  (this should happen automatically for you)
3.  upload the 'dictionary' and 'price' data to 'task.db'
4.  the program will be executed by running from the command prompt:

        (env):> python -m main


# Build

1.  Decompress this archive
2.  Create a python environment.  If you don't know how to do this, there are 
    plenty of online resources that explain this.
3.  Go to this directory in the command line and activate the python environment. 
4.  Install the python dependencies into the environemnet by typing from the    
    command prompt:

            (env):> pip install -r requirements.txt

5.  Install this library in developer mode:

            (env):> pip setup.py build
            (env):> pip install -e .


# Various

1.  Review the __init__.py file.  It does a lot of work for you.
2.  The task.db file is created the first time you run main.py.   
3.  Use DB Browser for SQLite (https://sqlitebrowser.org/) to view the dB.