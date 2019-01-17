# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:38:39 2018

@author: jojos
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats

def Frequenzgangbei49kwithdifferentbandwith():
    frequency=np.array([100,300,700,1000,3000,7000,10000,30000,70000,100000,200000,300000])
    voltage_out1=np.array([1.32,1.28,1.25,1.22,1.12,0.84,0.67,0.27,0.111,0.078,0.0395,0.0267])
    frequency2=np.array([300,700,1000,3000,7000,10000,20000])
    voltage_out2=np.array([0.352,0.68,0.856,1.18,1.23,1.23,1.18])
    voltage_out680=np.array([5.48,5.44,5.36,5.30,4.4,2.7,2.06,0.73,0.314,0.222,0.114,0.114])
    erstesOhm,=plt.plot(frequency,voltage_out680,linestyle='-',label='680kΩ')
    plt.errorbar(frequency,voltage_out680,yerr=voltage_out680*0.05,xerr=1,fmt='.')
    voltage_out274=np.array([2.24,2.16,2.16,2.16,2.08,1.76,1.52,0.68,0.31,0.222,0.116,0.078])
    zweitesOhm,=plt.plot(frequency,voltage_out274,linestyle='-',label='274kΩ')
    plt.errorbar(frequency,voltage_out274,yerr=voltage_out274*0.05,xerr=1,fmt='.')
    voltage_out49=np.array([1.26,1.25,1.24,1.24,1.24,1.23,1.22,1.1,0.8,0.63,0.35,0.25])
    drittesOhm,=plt.plot(frequency,voltage_out49,linestyle='-',label='490kΩ')
    plt.errorbar(frequency,voltage_out49,yerr=voltage_out49*0.05,xerr=1,fmt='.')
    Tiefpass,=plt.plot(frequency,voltage_out1,linestyle='-',label='mit 48.7pF und 48.7kΩ')
    plt.errorbar(frequency,voltage_out1,yerr=voltage_out1*0.05,xerr=1,fmt='.',ecolor='blue')
    Hochpass,=plt.plot(frequency2,voltage_out2,linestyle='-',label='mit 47nF und 48.7kΩ')
    plt.errorbar(frequency2,voltage_out2,yerr=voltage_out2*0.05,xerr=1,fmt='.',ecolor='10')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Frequenz[Hz]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 5: Frequenzgänge bei unterschiedlichen Rückkopplungen")
    plt.legend(handles=[Tiefpass,Hochpass,erstesOhm,zweitesOhm,drittesOhm])
    plt.show()
Frequenzgangbei49kwithdifferentbandwith()