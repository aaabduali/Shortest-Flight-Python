import numpy as np
import pandas as pd

#Prepare column names
cols=['Airline'
,'AirlineID'
,'Sourceairport'
,'SourceairportID'
,'Destinationairport'
,'DestinationairportID'
,'Codeshare'
,'Stops'
,'Equipment']

#Read routes data from file and create a pandas dataframe
routes=pd.read_csv('routes.csv')
#Change the column names
routes.columns=cols

routes_new = pd.read_csv('routes.txt', delim_whitespace=True,names=['sourceID','Airline','destinationID','cost'])
airports=pd.read_csv('airports.txt',delim_whitespace=True,names=['id','name','city','country','iata','icao','longitude','latitude','altitude','GMT','daylight','Timezone'])
print(airports.head())
print(routes_new.head())







