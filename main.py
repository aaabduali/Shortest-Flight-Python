import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
#Prepare column names
cols=[
'Airline',
'AirlineID',
'Sourceairport',
'SourceairportID',
'Destinationairport',
'DestinationairportID',
'Codeshare',
'Stops',
'Equipment']

#Read routes data from file and create a pandas dataframe
routes=pd.read_csv('routes.csv')
#Change the column names
routes.columns=cols

routes_new = pd.read_csv('routes.txt', delim_whitespace=True,names=['sourceID','Airline','destinationID','cost'])
airports=pd.read_csv('airports.txt',delim_whitespace=True,names=['id','name','city','country','iata','icao','longitude','latitude','altitude','GMT','daylight','Timezone'])
airports.head()
merged=routes_new.merge(airports[['id','iata']], left_on='sourceID', right_on='id',how='left')
merged.drop('id',axis=1,inplace=True)
merged.rename(columns={"iata": "origin"},inplace=True)
merged.head()
merged=merged.merge(airports[['id','iata']],left_on='destinationID',right_on='id',how='left')
merged.head()
merged.drop('id',axis=1,inplace=True)
merged.rename(columns={"iata": "destination"},inplace=True)
merged.head()
name_to_node = {name: i for i, name in enumerate(np.unique(merged[["sourceID", "destinationID"]].values))}
n_nodes = len(name_to_node)
A = np.zeros((n_nodes, n_nodes))
for row in merged.itertuples():
    n1 = name_to_node[row.sourceID]
    n2 = name_to_node[row.destinationID]
    A[n1, n2] += float(row.cost)
    A[n2, n1] += float(row.cost)
edgeDict = dict(enumerate(dict(enumerate(row)) for row in A))

for k, d in edgeDict.items():
    for ik in d:
        d[ik] = {'weight': d[ik]}

g = nx.DiGraph(edgeDict)

g.add_nodes_from(edgeDict.keys())
print(g[1107,113])







