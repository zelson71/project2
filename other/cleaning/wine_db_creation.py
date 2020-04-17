# import sql alchemy and modules for database creation and manipulation
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
import sqlalchemy
import pandas as pd
import glob
from ipywidgets.embed import embed_minimal_html
# Create loop to convert 16 csv files to dataframes, apply utf-8 coding and put into list. Concatenate dataframes in list into one dataframe.
path = 'Resources/WE_data'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, encoding='utf-8')
    li.append(df)

all_wines_df = pd.concat(li, axis=0, ignore_index=True, sort=True)


# assign the id to index
all_wines_df.index.name = ('ID')


# create the engine and initiate the session
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/wines_db', echo=False)
session = Session(engine)
if not database_exists(engine.url):
    create_database(engine.url)
conn = engine.connect()
session = Session(engine)


# convert the dataframe to SQL Table
all_wines_df.to_sql("all_wines", index=True, if_exists='replace', con=engine)
