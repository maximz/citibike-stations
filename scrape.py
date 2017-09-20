
import pandas as pd

# could do pd.read_json("the https link here")
# but then get two columns: executionTime and stationBeanList, which just has a python dict under it

# would rather have all columns broken out, not nested

# https://stackoverflow.com/questions/40588852/pandas-read-nested-json
#import json
from pandas.io.json import json_normalize   
#with open('myJson.json') as data_file:    
#    data = json.load(data_file)  
import requests
url = 'https://feeds.citibikenyc.com/stations/stations.json'
r = requests.get(url)
assert r.status_code == 200
# could use r.text()
data = r.json()
df = json_normalize(data, 'stationBeanList', ['executionTime'])
# df.executionTime.dtype: O
df['parsed_time'] = pd.to_datetime(df['executionTime'])
# df.parsed_time.dtype: <M8[ns]


# write to DB
# pip install SQLAlchemy psycopg2

from sqlalchemy import create_engine

#conn = create_engine('postgresql://username:password@yoururl.com:5439/yourdatabase')
conn = create_engine('sqlite+pysqlite:///file.db')

df.to_sql('livestations', conn, index = False, if_exists = 'append')

# test that it made it in with:
# pd.read_sql('livestations', conn)