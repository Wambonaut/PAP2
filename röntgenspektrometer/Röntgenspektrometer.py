#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 00:26:34 2019

@author: wambo
"""

##Auswertung zum Röntgenspektrometer
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy import optimize, stats
from scipy.constants import c, e
import os

LiF_DIST=201.4e-12
def checkdir():
    for filename in os.listdir("/home/wambo/PAP2/röntgenspektrometer"):
        if filename.endswith(".txt"): 
            print(filename)
            a=np.loadtxt(filename)
            plt.plot(a[:,0],a[:,1])
            plt.show()

LiC=np.loadtxt("20_11_2018 15_09_42.txt")
plt.plot(LiC[:,0],LiC[:,1])
slope, intercept, r, p, stderr=stats.linregress(LiC[10:15])
plt.errorbar(LiC[10:15,0], LiC[10:15,1], np.sqrt(LiC[10:15,1]))
plt.plot(np.linspace(4,7,25), np.linspace(4,7,25)*slope+intercept)
plt.title("Gesamtes Spektrum mit gefittetem linearem Abfall")
plt.ylabel("Intensität")
plt.xlabel("Winkel")
plt.show()
root=-intercept/slope
root_ERROR=-intercept/slope**2*stderr
print("Nullstelle:", root, "+-", root_ERROR)
##load single spikes
first_order=np.loadtxt("20_11_2018 15_15_14.txt")
kb_2=np.loadtxt("20_11_2018 15_30_34.txt")
ka_2=np.loadtxt("20_11_2018 15_38_08.txt")
kb_1=first_order[3:14]
ka_1=first_order[14:]

##plot single spikes

fit_func=lambda x, a, b,c,d: d + a*np.exp(-(x-c)**2/b)
def analyze_peak(k, p0, name, order=1):
    ##this just fits a peak to exp funtion, plots it and return the parameters and error of the fit. It also prints Peak height and position
    plt.plot(k[:,0],k[:,1])
    plt.title(name)
    plt.ylabel("Intensität")
    plt.xlabel("Winkel")
    popt, pcov=optimize.curve_fit(fit_func, k[:,0],k[:,1],p0=p0)
    plt.plot(np.linspace(k[0,0], k[-1,0], 100), fit_func(np.linspace(k[0,0], k[-1,0], 100), *popt))
    plt.show()
    print("Peak Höhe:", popt[0]+popt[3], "+-", np.sqrt(pcov[0][0]+pcov[3,3]))
    print("Peak Position: ", popt[2], "+-", np.sqrt(pcov[2][2]))
    y=2*LiF_DIST/order*np.sin(popt[2]/180*np.pi)
    y_ERROR=2*LiF_DIST/order*np.cos(popt[2]/180*np.pi)*np.sqrt(pcov[2][2])
    print("Zugehörige Wellenlänge", y, "+-",y_ERROR)
    return popt, pcov
analyze_peak(kb_1, [700, 0.1, 9, 100], "K-Beta erste Ordnung")
analyze_peak(ka_2, [250, 0.5, 20.5, 50], "K-Alpha zweite Ordnung", order=2)
analyze_peak(kb_2, [130, 0.2, 18.1, 40], "K-Beta zweite Ordnung", order=2)

##fit the k_alpha spike to gaussian
popt, pcov=analyze_peak(ka_1, [1800, 0.5, 10, 100], "K-alpha erste Ordnung")
##calculate Halbwertsbreite#
zero_func=lambda x: fit_func(x,*popt)-popt[0]/2
##find root of reduced function using Newton_krylov, since broyden doesnt seem to work here
a=optimize.newton_krylov(zero_func, [9.9])[0]
b=optimize.newton_krylov(zero_func, [10.3])[0]
HWB=b-a
print("Halbwertsbreite:", HWB)
##The countinous spectrum can also be subtracted, giving a halbwertbreite a bit higher
zero_func=lambda x: fit_func(x,*popt)-popt[0]/2-popt[3]
a=optimize.newton_krylov(zero_func, [9.9])[0]
b=optimize.newton_krylov(zero_func, [10.3])[0]
HWB2=b-a
print("Halbwertsbreite ohne kontinuierliches Spektrum:", HWB2)


###Einsatzspannungsberechnung
Voltage=np.linspace(20,35,16)
Intensity=[1.00,1.75,2.55,8.3,46.15,84.20,116.6,155.5,190.3,217.8,254.5,281.4,313.1,337.9,377.7,421.3]
plt.errorbar(Voltage, Intensity,np.sqrt(Intensity), fmt="none")
##using sqrt(Intensity) is a very vague estimate but doesnt matter
plt.xlabel("Spannung[kV]")
plt.ylabel("Intensität")
##linreg this shit

slope, intercept, r, p, stderr=stats.linregress(Voltage[3:], Intensity[3:])
root=-intercept/slope*1000
root_ERROR=-intercept/slope**2*np.sqrt(stderr)*1000
plt.plot(Voltage[2:], Voltage[2:]*slope+intercept)
plt.show()
print("Nullstelle:", root, "+-", root_ERROR)
l=2*LiF_DIST*np.sin(7.55/180*np.pi)
print("Dies entspricht einem Plankschen Wirkungsquantum von ", l*e*root/c, "+-", l*e*root_ERROR/c)


##NaCL Kristall Analyse
NaCl=np.loadtxt("20_11_2018 16_07_49.txt")
plt.plot(NaCl[:,0], NaCl[:,1])
plt.show()
##since we dont really have enough data points to justify any fit
##well just take the local maxima directly from the data and give an error of 0.2 degrees
peaks=sig.argrelmax(NaCl[:,1],order=3)[0][1:]##disregard the first element, it's where the continoous spectrum starts
peaks_ang=NaCl[peaks, 0]
print(peaks, peaks_ang)
peaks_ERROR=0.2
##Es dauert länger, das ausrechnen voll Gitterkonstante und Avogadrozahl hier zu machen als auf Papier, deswegen lassen wir das
