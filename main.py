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

print(routes.head())








