#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:17:54 2019

@author: wambo
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, signal
#########FOURIEROPTIK IM GOING TO KMS#################
length=845##mm
LAMBDA=635##Wellenlänge in nm
max_zero=479.91
minima=max_zero-np.array([430.75,384.14,335.84,279.91])
order_min=np.array([1,2,3,4])
error_minima_position=([2,2,2,10])
plt.errorbar(order_min,minima,error_minima_position, fmt=".", label="Minima")
(slope, intercept), cov =optimize.curve_fit(lambda x,m,b: m*x+b, order_min, minima, sigma=error_minima_position)
plt.plot(np.linspace(0,5), np.linspace(0,5)*slope+intercept, label="Fit durch die Minima")
maxima=max_zero-np.array([max_zero,409.57,356.18,307.84,250.24])
order_max=np.array([0,1,2,3,4])
maxima_in_line=(maxima-intercept)/slope
print("maxima liegen bei %.2f,%.2f,%.2f,%.2f,%.2f"%tuple(maxima_in_line), "theoretisch liegen sie bei .5")
plt.errorbar(maxima_in_line,maxima,[2,2,2,2,10],fmt=".", label="Maxima auf Gerade plaziert")
plt.xlabel("Ordnung")
plt.ylabel("px Abstand von Max 0ter Ordnung")
plt.legend()
plt.show()
##Berechnen der Spaltbreite
##Kalibrierung
opening=np.array([420,670,810,1060])##Öffnungsbreite in mikrometer
d_opening=10##rechnet sich grob in ein sigma von 146/420*10 um
image=np.array([146,250,353,454])##Bildbreite in px
d_image=2
plt.errorbar(opening,image, xerr=d_opening, yerr=d_image, fmt=".",label="Messpunkte")
(slopecal,), ((cov_slopecal,))=optimize.curve_fit(lambda x,a: a*x,opening, image)
plt.plot(np.linspace(300,1200),np.linspace(300,1200)*slopecal, label="fit")
plt.title("Kalibration des Spalts")
plt.xlabel("Mikrometer")
plt.ylabel("Pixel")
plt.show()
def px_to_um(px, px_cov=2):
    return np.array((px/slopecal, px/slopecal*np.sqrt(cov_slopecal/slopecal**2+(px_cov/px)**2)))
##berechne jetzt die spaltbreite
B, d_B=LAMBDA/(length)*px_to_um(slope)
print("Spaltbreite:%.4f+-%.4f nm"%(B,d_B))
##Intensitäten
inten_max=(np.array([307,185,121,105])-60)/3460
d_inten_max=np.array([3,2,3,10])/3520
##theoretisch
def beugung_spalt(x):
    return np.sinc(x)**2
inten_max_single=beugung_spalt(np.linspace(0,5,100)[signal.argrelmax(beugung_spalt(np.linspace(0,5,100)), order=2)])

print("Theoretisch", inten_max_single, "Praktisch", inten_max, "+-", d_inten_max)
for index, x in enumerate(inten_max):
    print("%i tes Maximum: Theoretisch: %.3f Praktisch: %.3f+-%.3f"%(index+1,inten_max_single[index], inten_max[index], d_inten_max[index]))
##Aufgabe 2
v=(107+88)/88
a=1
def beugung_doppelspalt(x):
    return np.sinc(x)**2*np.cos(np.pi*v*x)**2
x=np.linspace(-(a+1), a+1, 200)
plt.plot(x, beugung_spalt(x), label="Einzelspalt")
plt.plot(x, beugung_doppelspalt(x), label="Doppelspalt")
plt.xlabel("pi*x")
plt.ylabel("rel. Intensität")
plt.ylim(0,1.1)
plt.legend()
plt.show()
x=np.linspace(0,a+1,100)
##Aufgabe 3