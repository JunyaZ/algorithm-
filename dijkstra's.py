# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:12:46 2018

@author: Junya Zhao

Assignment 5 dijkstra's shortest path algorithm 
"""
import math
import numpy as np
def get_data(file_name):
    graph = {}
    with open (file_name) as file:
        for val in file:
            line = val.split()
            key = int(line[0])
            value = list(map(eval, line[1:]))
            subgraph = {key:value}
            graph.update(subgraph)
    return graph

def dijkstra(graph, start):
    visited = [start]
    distance = [10000] * len(graph.keys())
    distance[start - 1] = 0
    loop = False
    while not loop:
        min_cost = 100000000
        target_node = 0
        for node in visited:
            path = graph.get(node)
            for i in path:
    
                if i[0] not in visited:
                   # print(distance[node - 1])
                    cost = distance[node - 1] + i[1]
                    if cost <= min_cost:
                        min_cost = cost
                        target_node = i[0]
        distance[target_node - 1] = min_cost
        visited.append(target_node)
        if len(visited) == len(distance):
            loop = True
    return distance
        

if __name__ == '__main__':
     file = input('Please provide a filename containing an adjacency list:\n')
     vertex = input('Please provide a start vertex label (1..n):\n')
     start_vertex = int(vertex)
     '''
     text = np.loadtxt(file, dtype = str)
     
     Graph = {int(text[i][0]):[tuple(map(int,tuple(text[i][1].replace(",","")))), tuple(map(int,tuple(text[i][2].replace(",",""))))] for i in range(len(text))}
     '''
     Graph = get_data(file)
     v= dijkstra(Graph, start_vertex)
     print(*v, sep = ",")
