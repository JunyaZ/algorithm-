#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:15:16 2018

@author: Junya Zhao

"""
def add_edge(G, v1, v2, ce):
    if v1 in G:
        G[v1].append((v2, ce))
    else:
        G[v1] = [(v2, ce)]
    if v2 in G:
        G[v2].append((v1, ce))
    else:
        G[v2] = [(v1, ce)]
        
def add_edge_1(G, v1, v2, ce):
    if v1 in G:
        G[v1].append((v2, ce+1))
    else:
        G[v1] = [(v2, ce+1)]
    if v2 in G:
        G[v2].append((v1, ce+1))
    else:
        G[v2] = [(v1, ce+1)]
    
def prims(graph,start):
    visited = [start]
    target_node = 0  
    cost=[]  
    while len(visited) != len(graph):           
        min_cost=float("Infinity")  
        for node in visited:
            for edge in graph.get(node):
                if edge[0] not in visited and edge[1]< min_cost:
                    min_cost= edge[1]
                    target_node = edge[0]  
        cost.append(min_cost)
        visited.append(target_node)
    return sum(cost), visited


if __name__ == '__main__':

    input_filename = input('Please provide an input filename:\n')
    input_vertex = int(input('Please provide a start vertex label (1..n):\n'))

    G = {}
    with open(input_filename, 'r') as input_graph_file:
        n, m = tuple(int(x) for x in input_graph_file.readline().split())
        G = {}
        for line in input_graph_file:
            v1, v2, ce = tuple(int(v) for v in line.split())
            #add_edge_1(G, v1, v2, ce)
            add_edge(G, v1, v2, ce)
    print(prims(G, input_vertex))
