#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:05:50 2020

@author: donmj
"""
import os, sys

# defining the function that construct the permutation
def _permutation(list_distance, list_flow):
    # testing if our liste are not empty
    permutation = {}
    while(list_distance != [] and list_flow != []):
         permutation[list_flow[0][0]] = list_distance[0][0]
         permutation[list_flow[0][1]] = list_distance[0][1]
         # initialisation of the cost
         cost = list_flow[0][2] + list_distance[0][2]
         
         # filtering on element adding the permutation list
         list_distance = list(filter(lambda x: x[0]!=list_distance[0][0] and x[1]!=list_distance[0][0] \
                                     and x[0]!=list_distance[0][1] and x[1]!=list_distance[0][1], list_distance))
         list_flow = list(filter(lambda x: x[0]!=list_flow[0][0] and x[1]!=list_flow[0][0] \
                                 and x[0]!=list_flow[0][1] and x[1]!=list_flow[0][1], list_flow))
    
    
    # returninig the result
    return(permutation, cost, list_distance, list_flow)



# calulating the cost of the permutation
def _costPermutation(A,B, permutation):
    c = 0
    for key1, value1 in permutation.items():
        for key2, value2 in permutation.items():
            c += A[key1][key2]*B[value1][value2]
    # returning the result
    return c

