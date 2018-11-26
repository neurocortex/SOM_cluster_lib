"""
author: a.k.m.
breif: SOM clustering functions, designed for analysis of MEG data timeslices
"""

"""
imports
"""
from mvpa2.suite import *
import numpy as np

"""
functions
"""

#### read in MEG timeseries and create a new list of timeslice arrays
def MEGreadin(mFile):
    tsVectors = np.array([])
    #open mFile
    #for every timeslice in mfile
        #append timeslice vector as item in tsVectors
    return tsVectors

#### read in MEG timeseries and add add them to provided timeslice array
def MEGaddin(nFile, tsVec):
    #open nFile
    #for every timeslice in nfile
        #append timeslice vector as item in tsVec

#### load averaged 'exemplar' event timeslices for cluster labeling
def clusterLabel(cFile):
    #create list for test slices
    laVectors = np.array([])
    #create list for test slice names
    laNames = []
    #create list of apropriate size filled with colours
    laColours = n.array([])
    #predefined list of RBG colours for map labeling, simplest as a preset
    colours = np.array(
        [[.0,.0,.0],
         [.0,.0,.1],
         [.0,1.,.0],
         [.0,1.,1.],
         [1.,.0,.0],
         [1.,.0,1.],
         [1.,1.,.0],
         [1.,1.,1.],
         [.0,.0,.5],
         [.0,.5,.0],
         [.0,.5,.5],
         [.5,.0,.0],
         [.5,.0,.5],
         [.5,.5,.0],
         [.5,.5,.5],
         [.0,.0,.25],
         [.0,.25,.0],
         [.0,.25,.25],
         [.25,.0,.0],
         [.25,.0,.25],
         [.25,.25,.0],
         [.25,.25,.25]])
    #for each exemplar timeslice
        #add slice to laVectors
        #add name to laNames
        #add next unused colour value to laColours

    return laVectors, laNames, laColours

#### placeholder function for generating testing list of timeslices
def testSampleGen(size,ideal):
    #array for generated timeslices
    tgenVectors = np.array([])
    #generate a vector of specified size filled with 'fake' timeslices for testing
    #by randomly choosing and partially corrupting one of the ideal slices
    #for size:
        #randomly, choose one ideal slice
            #alter all items in slice by small random amount (+/-0.15)
            #OR
            #randomly, overwrite half of the data in ideal slice with random new value (1.0 to 0.0)
            #OR
            #do both of the above
        #append generated timeslice        
    return tgenVectors
    
#### placeholder function for generating testing list of examplar timeslices
def testExemplarGen(length):
    #generate predefined list of uncorrupted, exemplar slices  


#### initialize and train a SOM of provided size, learning rate, etc and train on dataset
## also, create output dump about training process, general network statistics, etc.
## h = som height, default 400
## w = som width, default 400
## ep = training epocs, default 1000
## lr = som learning rate, default 0.05
def somWrap(h=400,w=400,lr=0.05,ep=1000,dataSet):
    #create output file
    #create som, note som size is (rows,colums)
    somMEG = SimpleSOMMapper((w,h), ep, learning_rate=lr)
    #train som
    somMEG.train(dataset)
    #fill output file, close output file
    return somMEG

#### read in 'exemplar' timeslices and assign them a unique colour
def exampleSetup(source)

#### create labeled graph with exemplar/colour patches to identify clustering


#### present trained map with single timeslice, generate activation figure for timeslice


#### present trained map with single timeslice, return what cluster it belongs to with % confidence


#### present trained map with all timeslices in given list, and return % accurately clustered