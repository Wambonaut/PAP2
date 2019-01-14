#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:26:31 2019

@author: wambo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

f=np.linspace(1,10,10)*1000
phi=[1.26,1.00,0.072,0.065,0.055,0.048,0.040,0.036,0.033,0.030]
#plt.plot(f,phi)
test_func = lambda x, a, b: a*np.arctan(1/b*x)
(popt, pcov)=optimize.curve_fit(test_func, f, phi, p0=[1, 0.0001])
print(popt)
plt.plot(test_func(f, *popt))