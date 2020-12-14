

import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd 
import sqlalchemy as sa
from task.base import Base
from task.tables import Dictionary, Prices


# load .env variables
PROJECTDIR  = Path.cwd().parent.parent
env_path = PROJECTDIR / '.env'
load_dotenv(dotenv_path=env_path)
DATADIR = PROJECTDIR / os.getenv('DATADIR')
spreadsheet = DATADIR / os.getenv('FILENAME')
connection_string = os.getenv('DATABASE')

#sqlalchemy init
engine = sa.create_engine(connection_string, echo=False)
conn = engine.connect()
Session = sa.orm.sessionmaker(bind=conn)
session = Session()

# create tables in dB
Dictionary()
Prices()
Base.metadata.create_all(engine, checkfirst=True)
