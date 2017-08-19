# -*- coding: utf-8 -*-

"""
Creating a function who is able to :
	Open any data file 
	Browse all the data table
	Store the select data in a list
"""
def Open_My_File (FileName):
	 with open (FileName,"r") as NxFile1 : # Opening the file as NxFile1
		NxFile2 = csv.reader(NxFile1, delimiter="\t") # Reading the file without taking into account the space
		MyList = [] # Creating a new list to store the data inside it
		for line in NxFile2 :
			MyList.append(line)
		#print MyList # We find that we have a list in a list in which 
						# each list contains a row of the table
		return MyList # the "Open_My_File" function returns as a value the list "MyList"
						# It's means that we Keep the list in memory



"""
Creating function who is able to :
	Create a new Graph
	Looping the "Meta" data file but starting at the position number 1 which corresponds to the header
	Create node who is the laboratory name
	Add the attribute "axis, region, city" to each node 
	Return the Graph
"""
def Create_My_Nodes (MetaData) :
	G=nx.DiGraph()
	for i in range (1,len(MetaData)) : # Looping the data file
		G.add_node(MetaData[i][0], axis=MetaData[i][1], region=MetaData[i][2], city=MetaData[i][3])
	return G



"""
Function allowing to looping the table in line and in column 
According to the interaction values we adds the arcs linking the laboratories between us
Add the attribute "possible" if interaction value = "1"
Add the attribute "proved" if interaction value = "2"

"""
def Create_My_edge (InteractData, G):
	for lineTab in range (1, len(InteractData)): 
		print InteractData[lineTab]
		for columnTab in range (1,len(InteractData)):
			print InteractData[lineTab][columnTab]
			if InteractData[lineTab][columnTab] == "1" :
				G.add_edge(InteractData[lineTab][0], InteractData[0][columnTab], interaction ="possible")
			elif InteractData[lineTab][columnTab] == "2" :
				G.add_edge(InteractData[lineTab][0], InteractData[0][columnTab], interaction ="proved")
	return G



#---------------MainPrincipal------------------------------------------------------------------#

import networkx as nx
import csv

InteractData = Open_My_File ("interac.txt") # Calling the function to open my file interact.txt
#print InteractData

MetaData = Open_My_File ("meta.txt") # Calling the function to open my file meta.txt
#print MetaData

Node=Create_My_Nodes (MetaData)
NumberNode=Node.number_of_nodes() # Using the funtion "number_of_node" to count the number total of nodes
#print NumberNode

Edge=Create_My_edge (InteractData,Node)
NumberEdge=Edge.number_of_edges()
print NumberEdge

nx.write_gexf(Edge, "Graph_Hans.gexf", encoding='utf-8',prettyprint=True, version='1.1draft')#Function allowing funtionality to create the graph with the module Networkx

