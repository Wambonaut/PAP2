# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 18:14:22 2018

@author: jojos
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats
 

def Comparisonatresistance49k():
    voltage_IN=np.array([0.21,0.182,0.142,0.091,0.027,-0.049,-0.08,-0.135,-0.174,-0.213])
    voltage_OUT=np.array([-3.27,-2.67,-1.97,-1.17,-0.42,0.893,1.45,2.63,2.97,4.07])
    x=np.array(np.linspace(-0.25,0.25,100))
    y=x*-(49000/3000)
    (gradient, offset, r_value, p_value, stderr) =stats.linregress(voltage_IN,voltage_OUT)
    Regression,=plt.plot (x,gradient*x+offset, label='Regression')
    plt.plot(voltage_IN,voltage_OUT,linestyle='')
    plt.errorbar(voltage_IN,voltage_OUT,yerr=voltage_OUT*0.05,xerr=voltage_IN*0.05,fmt='.')
    plt.xlabel("Eingangsspannung [V]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 2: Vergleich Eingangs- und Ausgangspannung bei Wechselspannung und 680kΩ")
    Berechnet,=plt.plot(x,y,label='berechnet')
    plt.legend(handles=[Regression,Berechnet])
    print('Steigung ' + str(gradient) + '±' + str(stderr) )
    print(49000/3000)
    plt.show
Comparisonatresistance49k()

 