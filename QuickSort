#!/usr/bin/env python3
"""
Created on Wed Oct  3 11:22:45 2018

@author: Junya Zhao
"""

import numpy as np
import random 
Comparison=[]
def readfile (filenemae):
   file = np.loadtxt(filename,delimiter='\n')
   data = list(file)[1:]
   inputData = list(map(lambda x:int(x),data))
   return inputData
            
def partition (array,left_index,right_index):
    pivot =array[left_index]
    i = left_index + 1
    for j  in range (left_index + 1, right_index):
        if array[j] < pivot:
            array[j], array[i] = array[i],array[j]
            i+=1
    array[left_index],array[i-1] = array[i-1],array[left_index]
    return i-1, right_index-left_index

def choose_pivot(A, left,right,variant):
    if variant == "first":
        pivot_index = left
        return pivot_index
    if variant == "median3":
        left_index =left
        right_index =right-1
        middle_index = int((left + right-1)/2)
        if A[left_index] <= A[middle_index] <= A[right_index] or A[right_index] <=  A[middle_index] <= A[left_index]:
            return middle_index
        elif A[middle_index] <= A[left_index] <= A[right_index] or A[right_index] <= A[left_index] <= A[middle_index]:
            return left_index
        else:
            return right_index
    if variant =="random":
        pivot_index = random.randint(left,right-1)
        return pivot_index

def QuickSort(A,left,right,variant):
    if (left - right)==0:
        return A
    pivotIndex =choose_pivot(A,left,right,variant)
    A[pivotIndex],A[left] =A[left],A[pivotIndex]
    current_pivot,comparison = partition(A, left,right)
    global Comparison
    Comparison.append(comparison)
    QuickSort(A, left, current_pivot,variant)
    QuickSort(A, current_pivot + 1, right,variant)
    comparison +=comparison
    #print(comparison-len(A))
    return A,sum(Comparison)-len(A)


if __name__== "__main__":
    filename= input("Please enter a filename:")
    variant = input("Please enter a Quicksort variant :")
    array = readfile(filename)
    Sorted_A,Total_Compar= QuickSort(array,0,len(array), variant)
    print(Total_Compar)

    
    
        
