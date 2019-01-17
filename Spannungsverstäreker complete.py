#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 04:37:13 2019

@author: wambo, jojos
"""

##Alle Spannungsverstärkersachen in einem

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats

def Comparisonatresistance274k():
    voltage_IN=np.array([0.238,0.198,0.142,0.094,0.027,-0.049,-0.079,-0.135,-0.184,-0.244])
    voltage_OUT=np.array([-12.9,-12.8,-12.6,-7.87,-2.31,4.65,8.03,13,14.9,14.9])
    voltage_IN_reduced=np.array([0.142,0.094,0.027,-0.049,-0.079,-0.135])
    voltage_OUT_reduced=np.array([-12.6,-7.87,-2.31,4.65,8.03,13])
    x=np.array(np.linspace(-0.25,0.25,100))
    y=x*-(274000/3000)
    (gradient, offset), cov =np.polyfit(voltage_IN_reduced ,voltage_OUT_reduced, 1, cov=True)
    Regression,=plt.plot (x,gradient*x+offset, label='Regression')
    plt.plot(voltage_IN,voltage_OUT,linestyle='')
    plt.errorbar(voltage_IN,voltage_OUT,yerr=voltage_OUT*0.05,xerr=voltage_IN*0.05,fmt='.')
    plt.xlabel("Eingangsspannung [V]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 1: Vergleich Eingangs- und Ausgangspannung bei Gleichspannung und 274kΩ")
    Berechnet,=plt.plot(x,y,label='berechnet')
    plt.legend(handles=[Regression,Berechnet])
    print('Steigung ' + str(gradient) + '±' + str(np.sqrt(cov[0][0])) )
    print(-274000/3000)
    plt.show()
Comparisonatresistance274k()
def Comparisonatresistance49k():
    voltage_IN=np.array([0.21,0.182,0.142,0.091,0.027,-0.049,-0.08,-0.135,-0.174,-0.213])
    voltage_OUT=np.array([-3.27,-2.67,-1.97,-1.17,-0.42,0.893,1.45,2.63,2.97,4.07])
    x=np.array(np.linspace(-0.25,0.25,100))
    y=x*-(49000/3000)
    (gradient, offset), cov =np.polyfit(voltage_IN,voltage_OUT, 1, cov=True)
    Regression,=plt.plot (x,gradient*x+offset, label='Regression')
    plt.plot(voltage_IN,voltage_OUT,linestyle='')
    plt.errorbar(voltage_IN,voltage_OUT,yerr=voltage_OUT*0.05,xerr=voltage_IN*0.05,fmt='.')
    plt.xlabel("Eingangsspannung [V]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 2: Vergleich Eingangs- und Ausgangspannung bei Gleichspannung und 48.7kΩ")
    Berechnet,=plt.plot(x,y,label='berechnet')
    plt.legend(handles=[Regression,Berechnet])
    print('Steigung ' + str(gradient) + '±' + str(np.sqrt(cov[0][0])) )
    print(49000/3000)
    plt.show()
Comparisonatresistance49k()

def Comparisonatresistance274kAC():
    voltage_IN=np.array([0.1,0.08,0.07,0.05,0.03,0.01])
    voltage_OUT=np.array([7.6,5.72,5.04,3.58,2.18,0.76])
    x=np.array(np.linspace(0,0.12,100))
    y=x*(274000/3000)
    (gradient, offset), cov =np.polyfit(voltage_IN,voltage_OUT, 1, cov=True)
    Regression,=plt.plot (x,gradient*x+offset, label='Regression')
    plt.plot(voltage_IN,voltage_OUT,linestyle='')
    plt.errorbar(voltage_IN,voltage_OUT,yerr=voltage_OUT*0.05,xerr=voltage_IN*0.05,fmt='.')
    plt.xlabel("Eingangsspannung [V]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 3: Vergleich Eingangs- und Ausgangspannung bei Wechselspannung und 274kΩ")
    Berechnet,=plt.plot(x,y,label='berechnet')
    plt.legend(handles=[Regression,Berechnet])
    print('Steigung ' + str(gradient) + '±' + str(np.sqrt(cov[0][0])) )
    print(274000/3000)
    plt.show()
Comparisonatresistance274kAC()

def Comparisonatresistance680kAC():
    voltage_IN=np.array([0.1,0.08,0.07,0.05,0.03,0.01])
    voltage_OUT=np.array([17.9,14.5,12.2,8.88,5.28,1.8])
    x=np.array(np.linspace(0,0.12,100))
    y=x*(680000/3000)
    (gradient, offset), cov =np.polyfit(voltage_IN,voltage_OUT, 1, cov=True)
    Regression,=plt.plot (x,gradient*x+offset, label='Regression')
    plt.plot(voltage_IN,voltage_OUT,linestyle='')
    plt.errorbar(voltage_IN,voltage_OUT,yerr=voltage_OUT*0.05,xerr=voltage_IN*0.05,fmt='.')
    plt.xlabel("Eingangsspannung [V]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 4: Vergleich Eingangs- und Ausgangspannung bei Wechselspannung und 680kΩ")
    Berechnet,=plt.plot(x,y,label='berechnet')
    plt.legend(handles=[Regression,Berechnet])
    print('Steigung ' + str(gradient) + '±' + str(np.sqrt(cov[0][0])) )
    print(680000/3000)
    plt.show()
Comparisonatresistance680kAC()


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