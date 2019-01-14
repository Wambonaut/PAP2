# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:33:45 2018

@author: jojos
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats

def Frequenzgangbei274k():
    frequency=np.array([100,300,700,1000,3000,7000,10000,30000,70000,100000,300000,200000])
    voltage_out274=np.array([2.24,2.16,2.16,2.16,2.08,1.76,1.52,0.68,0.31,0.222,0.078,0.116])
    plt.plot(frequency,voltage_out274,linestyle='')
    plt.errorbar(frequency,voltage_out274,yerr=voltage_out274*0.05,xerr=1,fmt='.')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Frequenz[Hz]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 5: Frequenzgang bei 680kΩ")
    plt.show
Frequenzgangbei274k()