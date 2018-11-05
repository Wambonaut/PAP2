#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:24:35 2018

@author: wambo
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats
####Teil 1: Frequenz/Spannnung, Strom/Spannung Diagramme
###Frequenz/Spannung
##plot shit
def FrequencyVoltage():
    frequency_Hz=[15, 12, 9, 6, 3]
    frequency_Volt=[5.1, 4.0, 2.9, 1.8, 0.8]
    Voltage_Error=0.1
    plt.errorbar(frequency_Hz, frequency_Volt, yerr=Voltage_Error, color="blue")
    plt.ylabel("Spannung[V]")
    plt.xlabel("Frequeny[Hz]")
    plt.title("Diagramm 1: Spannung in Abhängigkeit der Drehfrequenz bei 4,0±0.05A")
    ##do the regression thing
    (gradient, offset, r_value, p_value, stderr) =stats.linregress(frequency_Hz, frequency_Volt)
    ##plot the regression
    plt.plot([offset + x*gradient for x in range(17)], color="red")
    plt.text(4, 3, "Steigung: " + str(gradient.round(2)))
    
    red_patch = mpatches.Patch(color='red', label='Regression')
    blue_patch = mpatches.Patch(color='blue', label='Gemessen')
    plt.legend(handles=[red_patch, blue_patch])
    print("Stderr Slope Diag 1:" + str(stderr))
    plt.show()
###Strom/Spannung
def CurrentVoltage():
    current_Ampere=[0.5*i for i in range(1,10)]
    current_Volt=[0.5, 0.9, 1.3, 1.7, 2.1, 2.5, 2.9, 3.4, 3.8]
    plt.errorbar(current_Ampere, current_Volt, yerr=0.05, xerr=0.15)
    plt.xlabel("Strom[A]")
    plt.ylabel("Pannung[V]")
    plt.title("Diagramm 2: Spannung in Abhängigkeit des Stroms bei f=10±1Hz")
    
    ##linear Regression again
    (gradient, offset, r_value, p_value, stderr) =stats.linregress(current_Ampere, current_Volt)
    ##plot the regression
    plt.plot([offset + x*gradient for x in range(6)], color="red")
    plt.text(1, 3, "Steigung: " + str(gradient.round(2)))
    
    red_patch = mpatches.Patch(color='red', label='Regression')
    blue_patch = mpatches.Patch(color='blue', label='Gemessen')
    plt.legend(handles=[red_patch, blue_patch])
    print("Stderr Slope Diag 2:" + str(stderr))
    plt.show()

####Teil 2: Spannung bei Periodischem Strom
###Winkel/Spannung
def AngleVoltage(sine_fit=True):
    angle=[x*30 for x in range(7)]
    Volt=[1.5,1.3,0.7,0.2,0.8,1.3,1.5]
    xerr=2
    yerr=0.05
    plt.errorbar(angle, Volt, xerr=xerr, yerr=yerr, color="blue")
    plt.xlabel("Winkel[°]")
    plt.ylabel("Spannung[V]")
    angle=[x*30 for x in range(13)]
    Volt.extend(Volt[1:])
    if sine_fit:
        ##Do a sine fit (because y not)
        def test_func(x, a, b, c, d):
            return a * np.sin(b * x + c ) + d
        
        params, params_covariance = optimize.curve_fit(test_func, angle, Volt,
                                                       p0=[2.0, 0.05, 0, 1])
        plt.plot(range(190), [test_func(angl, params[0], params[1], params[2], params[3]) for angl in range(190)], color="red")
        red_patch = mpatches.Patch(color='red', label='Sinus Fit')
    
    blue_patch = mpatches.Patch(color='blue', label='Gemessen')
    plt.legend(handles=[red_patch, blue_patch])
    plt.title("Diagramm 3: Spannung in Abhängigkeit des Drehwinkels bei Wechselstrom")
    plt.show()
####Angelegte/Induzierte spannung als Funktion der Frequenz
def Induced_currentFrequency():
    frequency=np.array([21.3,43.9,66.7, 89.3,112,227,459,667,897,1140,1460,1960])
    Volt_ind=np.array([1.08,2.98,2.76,2.98,1.88,2.50, 2.64,2.5,2.42,2.42,2.45,2.42])
    Volt=    np.array([1.12,1.56,1.27,1.78,2.80,2.56,1.12,0.48,0.32,0.24,0.24,0.16])
    mAmp=np.array([196,143,97,71,61,34,15,11,8,6,5,4])
    frequency_err_relative=0.01
    frequency_err=frequency_err_relative*frequency
    Volt_err=0.01*np.sqrt(2)
    mAmp_err=1
    
    Volt_compared=Volt_ind/Volt
    
    plt.errorbar(frequency, Volt_compared, xerr=frequency_err, yerr=Volt_err, color="blue")
    plt.xlabel("Frequenz[Hz]")
    plt.ylabel("Induzierte/Angelegte Spannung [V/V]")
    plt.title("Diagramm 4: Verhältnis Induziert/Angelegte Spannung in Abhängigkeit der Frequenz")
    ###linear fit
    (gradient, offset, r_value, p_value, stderr)=stats.linregress(frequency, Volt_compared)
    print("Stderr Slope Diag 4:" + str(stderr))
    plt.text(250,10, "Steigung: "+ str(round(gradient, 2)) + "V/Hz")
    plt.plot(frequency, gradient*frequency+offset, color="red")
    plt.show()
def ResistanceFrequency():
    frequency=np.array([21.3,43.9,66.7, 89.3,112,227,459,667,897,1140,1460,1960])
    Volt_ind=np.array([1.08,2.98,2.76,2.98,1.88,2.50, 2.64,2.5,2.42,2.42,2.45,2.42])
    Volt=    np.array([1.12,1.56,1.27,1.78,2.80,2.56,1.12,0.48,0.32,0.24,0.24,0.16])
    mAmp=np.array([196,143,97,71,61,34,15,11,8,6,5,4])
    frequency_err_relative=0.01
    frequency_err=frequency_err_relative*frequency
    Volt_err=0.01
    mAmp_err=1
    
    Ohm=Volt_ind/(mAmp/1000)
    Ohm_err=Ohm*np.sqrt((Volt_err/Volt)**2+(mAmp_err/mAmp)**2)
    
    
    plt.errorbar(frequency, Ohm, xerr=frequency_err, yerr=Ohm_err)
    plt.xlabel("Frequenz[Hz]")
    plt.ylabel("Widerstand[Ω]")
    plt.title("Diagramm 5: Widerstand der in Abhängigkeit der Frequenz")
    ##linear fit
    (gradient, offset, r_value, p_value, stderr)=stats.linregress(frequency, Ohm)
    plt.plot(frequency, frequency*gradient+offset, color="red")
    plt.text(250, 600, "Steigung: " + str(round(gradient, 2)) + "Ω/Hz")
    red_patch = mpatches.Patch(color='red', label='Regression')
    blue_patch = mpatches.Patch(color='blue', label='Gemessen')
    plt.legend(handles=[red_patch, blue_patch])
    print("Stderr Slope Diag 5:" + str(stderr))

    plt.show()
FrequencyVoltage()
CurrentVoltage()
AngleVoltage()
Induced_currentFrequency()
ResistanceFrequency()
    