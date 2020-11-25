#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:36:25 2020

@author: donmj
"""
import transformdata
import permutation

path_instance = '/home/donmj/Bureau/QAP/data/Els19'

if __name__ == '__main__':
    
    input_data = transformdata._transformInstance(path_instance)
    
    liste_distance = transformdata._getSortedTupleList(input_data[1])
    liste_flow = transformdata._getSortedTupleList(input_data[2])
    
    # application of permutation
    result = permutation._permutation(liste_distance, liste_flow)
    
    # calulation de cost
    cost = permutation._costPermutation(input_data[1], input_data[2], result[0])
    
    
    print("END")