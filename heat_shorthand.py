# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 10:06:21 2016

@author: a
"""

import som_cluster_lib
from som_cluster_lib import *
import matplotlib.pyplot as plot

#lets make some heat plots
def lazyHeatWorkup(SOM,data):
    cbook = SOM.codebook    
    
    vis = data[75]
    aud = data[225]
    vdis = data[375]
    adis = data[525]
    pair = data[675]
    bint = data[825]
    
    vis_heat = sliceHeat(cbook,vis,sliceLabel='Visual')
    plot.clf()
    aud_heat = sliceHeat(cbook,aud,sliceLabel='Auditory')
    plot.clf()
    vdis_heat = sliceHeat(cbook,vdis,sliceLabel='Visual Distractor')
    plot.clf()    
    adis_heat = sliceHeat(cbook,adis,sliceLabel='Auditory Distractor')
    plot.clf()
    pair_heat = sliceHeat(cbook,pair,sliceLabel='Paired')
    plot.clf()
    bint_heat = sliceHeat(cbook,bint,sliceLabel='Between Interleaved')
    plot.clf()
    
    v_aud_h = quickHComp(vis,aud,SOM,label='Visual vs Auditory')
    plot.clf()
    v_vdis_h = quickHComp(vis,vdis,SOM,label='Visual vs Visual Distractor')
    plot.clf()
    v_adis_h = quickHComp(vis,adis,SOM,label='Visual vs Auditory Distractor')
    plot.clf()
    v_pair_h = quickHComp(vis,pair,SOM,label='Visual vs Paired')
    plot.clf()
    v_bint_h = quickHComp(vis,bint,SOM,label='Visual vs Between Interleaved')
    plot.clf()
    
    
    v_aud_bmu = clustComp(vis,aud,SOM,e1='Visual',e2='Auditory',bmu_no=200)
    v_vdis_bmu = clustComp(vis,vdis,SOM,e1='Visual',e2='Visual Distractor',bmu_no=200)
    v_adis_bmu = clustComp(vis,adis,SOM,e1='Visual',e2='Auditory Distractor',bmu_no=200)
    v_pair_bmu = clustComp(vis,pair,SOM,e1='Visual',e2='Paired',bmu_no=200)
    v_bint_bmu = clustComp(vis,bint,SOM,e1='Visual',e2='Between Interleaved',bmu_no=200)