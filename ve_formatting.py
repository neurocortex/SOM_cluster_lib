# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:24:06 2016

@author: a
"""

import h5py
import numpy as np
import scipy.io as sio

#### saves a set of hdf5 files into a .mat file (hopefully?)
def VE_mat_former(file_list,hd5_path,mat_name):
    intoNp = np.array()
    for item in file_list:
        with h5py.File(item,'r') as f:
            intoNp.append(f[hd5_path][()])
    sio.savemat(mat_name, dict(intoNp))
    
#### saves a set of hdf5 files into a 3d numpy array
def VE_np_former(file_list,hd5_path):
    intoNp = np.array()
    for item in file_list:
        with h5py.File(item,'r') as f:
            intoNp.append(f[hd5_path][()])
    return intoNp