import cur as cur
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float, Date
from models import import_d


stations_data = import_data('clean_stations.csv')
stations_data = stations_data[1:]

measures_data = import_data('clean_measure.csv')
measures_data = measures_data[1:]


engine = create_engine('sqlite:///stations.db')

meta = MetaData()

measures = Table(
   'measures', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('date', String),
   Column('precip', Float),
   Column('tobs', Integer),
)

stations = Table(
   'stations', meta,
   Column('station', String, primary_key=True),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Float),
   Column('name', String),
   Column('country', String),
   Column('state', String)
)

meta.create_all(engine)

ins = stations.insert()
result = map(lambda x: {'station': x[0], 'latitude' : x[1], 'longitude' : x[2], 'elevation' : x[3],'name' : x[4],'country' : x[5],'state' : x[6]}, stations_data)
result = list(result)
conn = engine.connect()
conn.execute(ins,result)

ins = measures.insert()
result = map(lambda x: {'station': x[0], 'date' : x[1], 'precip' : x[2], 'tobs': x[3]}, measures_data)
result = list(result)
conn = engine.connect()
conn.execute(ins,result)



