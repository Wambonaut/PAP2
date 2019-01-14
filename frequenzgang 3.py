# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:33:46 2018

@author: jojos
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats

def Frequenzgangbei49k():
    frequency=np.array([100,300,700,1000,3000,7000,10000,30000,70000,100000,300000,200000])
    voltage_out49=np.array([1.26,1.25,1.24,1.24,1.24,1.23,1.22,1.1,0.8,0.63,0.25,0.35])
    plt.plot(frequency,voltage_out49,linestyle='')
    plt.errorbar(frequency,voltage_out49,yerr=voltage_out49*0.05,xerr=1,fmt='.')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Frequenz[Hz]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 5: Frequenzgang bei 680kΩ")
    plt.show
Frequenzgangbei49k()