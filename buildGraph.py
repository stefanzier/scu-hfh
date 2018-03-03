import csv

import classes.graph as graphs

file = "data.csv"

state_dict = dict();
graph = graphs.Graph(None);
	
with open(file, 'rb') as csvfile:
	data= csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			### build a state
			### put it in the map
			### update the graph 
