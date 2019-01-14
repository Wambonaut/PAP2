# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:36:07 2018

@author: jojos
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats
 
#number 1 part 1
def Comparisonatresistance274k():
    voltage_IN=np.array([0.238,0.198,0.142,0.094,0.027,-0.049,-0.079,-0.135,-0.184,-0.244])
    voltage_OUT=np.array([-12.9,-12.8,-12.6,-7.87,-2.31,4.65,8.03,13,14.9,14.9])
    voltage_IN_reduced=np.array([0.142,0.094,0.027,-0.049,-0.079,-0.135])
    voltage_OUT_reduced=np.array([-12.6,-7.87,-2.31,4.65,8.03,13])
    x=np.array(np.linspace(-0.25,0.25,100))
    y=x*-(274000/3000)
    (gradient, offset, r_value, p_value, stderr) =stats.linregress(voltage_IN_reduced ,voltage_OUT_reduced )
    Regression,=plt.plot (x,gradient*x+offset, label='Regression')
    plt.plot(voltage_IN,voltage_OUT,linestyle='')
    plt.errorbar(voltage_IN,voltage_OUT,yerr=voltage_OUT*0.05,xerr=voltage_IN*0.05,fmt='.')
    plt.xlabel("Eingangsspannung [V]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 2: Vergleich Eingangs- und Ausgangspannung bei Wechselspannung und 680kΩ")
    Berechnet,=plt.plot(x,y,label='berechnet')
    plt.legend(handles=[Regression,Berechnet])
    print('Steigung ' + str(gradient) + '±' + str(stderr) )
    print(-274000/3000)
    plt.show
Comparisonatresistance274k()
 