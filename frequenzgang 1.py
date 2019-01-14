# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:05:44 2018

@author: jojos
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats

def Frequenzgangbei680k():
    frequency=np.array([100,300,700,1000,3000,7000,10000,30000,70000,100000,300000,200000])
    voltage_out680=np.array([5.48,5.44,5.36,5.30,4.4,2.7,2.06,0.73,0.314,0.222,0.114,0.114])
    plt.plot(frequency,voltage_out680,linestyle='')
    plt.errorbar(frequency,voltage_out680,yerr=voltage_out680*0.05,xerr=1,fmt='.')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Frequenz[Hz]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 5: Frequenzgang bei 680kΩ")
    plt.show
Frequenzgangbei680k()