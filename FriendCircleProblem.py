# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:22:53 2018

@author: Junya Zhao
CSC 611  Assignment 4  friend cricle problem
"""
def DFS(friends, v, explored):
    explored[v]=True
    for s in range(len(friends[v])):
        if friends[v][s]=="Y" and not explored[s]:
            DFS(friends, s, explored)

def count_friend_circles(friends):
    explored=[False]*len(friends)  
    num=0
    for v in range(len(friends)):
        if not explored[v]:
            DFS(friends, v, explored)
            num+=1
    return num  

if __name__ == '__main__':

    matrix_filename = input('Please provide a filename containing a friends matrix:\n')

    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]

    num_circles = count_friend_circles(friends)
    print(f'Number of friend circles: {num_circles}')
