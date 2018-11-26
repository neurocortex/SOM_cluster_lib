# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:23:02 2016

@author: a
"""
import numpy as np

def textInTest(fName):
    results = [] #hold raw values from text file
    with open((fName+'.txt')) as inputfile:
        for line in inputfile:
            lin = line.split()
            res = []
            for i in lin:
                res.append(float(i))
            r = res[1:-1]
            results.append(r)
            #results.append(res)
    fResult = np.array(results) #transform into numpy array
    return fResult