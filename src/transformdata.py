#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:37:08 2020

@author: donmj
"""
import numpy as np


# function that return a numpy matrix from a tabular string
def _getMatrixData(matrix_file):
    # splitting the tabular form of data
    temp_split = matrix_file.split('\n')
    
    # verification of the bank list
    if(temp_split[-1]==''):
        del temp_split[-1]
    
    # put it on the numpy matrix
    m = np.array([[int(j) for j in i.split()] for i in temp_split])
    
    # return the result
    return m
    

# function that extracts informations from data instance file 
def _transformInstance(path_instance):
    # reading the instance
    with open(path_instance, 'r') as f:
        data = f.read()
        
    # parsing the list to get an ouput of the form (n, A, B)
    data_split = data.split('\n\n')
    
    # get the value of n 
    n = int(data_split[0])
    
    # getting the matrix of flows
    A = _getMatrixData(data_split[1])
    
    # getting the matrix of distances
    B = _getMatrixData(data_split[2])
    
    # return the data
    return (n, A, B)


def _getSortedTupleList(M):
    # this function return a list of tuple (a, b, c),
    # where (a,b) is the arc and c is the cost in the given mtarix
    edge_cost = []
    for i in range(M.shape[0]):
        for j in range(i+1, M.shape[0]):
            edge_cost.append((i,j,M[i][j]))
            
    # sorting the liste
    edge_cost = sorted(edge_cost, key=lambda tup: tup[2])
    # return the liste of cost
    return edge_cost
    
    