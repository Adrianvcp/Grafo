

#!/usr/bin/env python
# coding=utf-8

import pygraphviz as pgv
import pandas as pd

#Diccionario de nodos y arcos

def leerInformacion(Grafo):
    file = 'CPS.xlsx'
    x = pd.ExcelFile(file)
    line1 = pd.read_excel(file)
    nombre1 = line1.columns[1]
    agregarDatosGrafo(nombre1,line1,Grafo)
    

def agregarDatosGrafo(nombre,dataFrame,Grafo):
    print(dataFrame.columns[1])
    print(nombre)
    #Grafo.add_edge('X',nombre,label='10')
    Grafo.add_edge('a','b',label='8')
    Grafo.add_edge('a','c',label='2')
    Grafo.add_edge('a','e',label='6')
    Grafo.add_edge('a','d',label='4')
    Grafo.add_edge('b','c',label='6')
    Grafo.add_edge('b','e',label='9')
    Grafo.add_edge('b','d',label='12')
    Grafo.add_edge('c','e',lebel='5')
    Grafo.add_edge('c','d',label='3')
    Grafo.add_edge('d','e',label='4')

def extraerCoordenadas(dato):
    xy = dato.split('-')
    y = xy[1]
    x = xy[2]
    print( str(x) + " : " + str(y))




G = pgv.AGraph()

leerInformacion(G)



G.layout()

G.draw('file.png')


#extraerCoordenadas('-13.992029757-72.5312662119999')