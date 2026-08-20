# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:09:03 2025

@author: 2k23c
"""
import numpy as np
v=np.array([[1,2],[3,4]])
print(v)
v1=np.array([[12,2],[32,4]])
print()
print(v1)
x=np.concatenate((v,v1),axis=0)
print(x)
print()
x=np.concatenate((v,v1),axis=1)
print(x)
print()
ar=np.stack(x)
print(ar)
print()
ar=np.stack(x,axis=1)
print(ar)
print()
ar=np.vstack(x)
print(ar)
print()
ar=np.hstack(x)
print(ar)