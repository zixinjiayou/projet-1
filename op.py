#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9  2020

"""
import numpy as np
import scipy.sparse as sp

# Gradient operator and boundary terms
def gradient_FV(m, dxp):
    
    # declaration
    Div = np.zeros( np.array ([m-2,m-1]) )
    Gra = np.zeros( np.array ([m-1,m]) )
    
    # divergence
    Div = sp.diags([-1,1], [0,1], (m-2,m-1)).toarray()
    
    # gradient
    Gra = sp.diags([-1/dxp,1/dxp], [0,1], (m-1, m)).toarray()
    
    return Div, Gra
  