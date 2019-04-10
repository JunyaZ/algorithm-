# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:15:37 2019

@author: Junya
"""

def insertionsort(A):
    for j in range(2,len(A)):
        key = A[j]
        i = j-1 
        while (i > 0) and key < A[i]: 
            A[i+1]=A[i] 
            i=i-1 
        A[i+1] = key
    return A

if __name__=="__main__":
    x = [5,2,4,6,1,3]
    insertionsort(x)
    print (x)
