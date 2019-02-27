#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:11:30 2019

@author: wambo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
##Dämpfung

t=np.array([0,2,4,6,8,10,12])*60
d_t=5/60
f=np.array([800,720,660,620,570,535,505])
d_f=5
plt.yscale("log")
plt.errorbar(t,f,yerr=d_f, xerr=d_t)
(A,l),cov=optimize.curve_fit(lambda x, A, l: A*np.exp(-l*x), t, f, p0=[1000, 0.03])
print(A,l)
plt.plot(np.linspace(0,800), A*np.exp(-np.linspace(0,800)*l))
plt.show()
print("Dämpfungskonstante: %.6f 1/s +- %.6f, Halbwertszeit: %.1f +- %.1f s"%(l, np.sqrt(cov[1,1]),np.log(2)/l,np.log(2)/l**2*np.sqrt(cov[1,1])))

##3b

cm15_1weight=np.array([[315,475,580,723], [54,1*60+19,1*60+37,2*60]])
cm20_1weight=np.array([[280,385,540,717], [36,52,1*60+12,1*60+36]])
cm15_2weight=np.array([[274,385,547,640], [25,35,52,58]])
cm20_2weight=np.array([[300,435,620,690], [21,31,43,47]])
all_slopes=[]##Das ist die badeste Practice und der schlechteste Code den ich je geschrieben habe, Herr im Himmel verzeih mir
def process_3b(values, label):
    values[0]=(values[0]*np.exp(values[1]*-l)+values[0])/2
    plt.errorbar(values[0],values[1],yerr=1,xerr=5,fmt=".")
    (slope, ), cov= optimize.curve_fit(lambda x, a: a*x,values[0],values[1])
    plt.plot(np.linspace(200,800,10),np.linspace(200,800,10)*slope, label=label)
    all_slopes.append([slope,np.sqrt(cov[0][0])])##tut weg
    return (slope, np.sqrt(cov[0][0]))
print("Steigung 15cm 1 Gewicht: %.4f +- %.4f" % process_3b(cm15_1weight, "15 cm 1 Gewicht"))
print("Steigung 20cm 1 Gewicht: %.4f +- %.4f" % process_3b(cm20_1weight, "20 cm 1 Gewicht"))
print("Steigung 15cm 2 Gewichte: %.4f +- %.4f" % process_3b(cm15_2weight, "15 cm 2 Gewichte"))
print("Steigung 20cm 2 Gewichte: %.4f +- %.4f" % process_3b(cm20_2weight, "20 cm 2 Gewichte"))
plt.legend()
plt.show()
all_slopes=np.array(all_slopes)
Iz=981*np.array([9.85,9.85,9.85*2,9.85*2])*np.array([15,20,15,20])*all_slopes[:,0]##au
d_Iz=Iz*all_slopes[:,1]/all_slopes[:,0]
av_Iz=np.average(Iz)
d_av_Iz=np.sqrt(np.var(Iz)+np.sum(d_Iz**2))/len(d_Iz)
print("Alle Drehmomente:", Iz)
print("Mittleres Drehmoment: %.1f+-%.1f"%(av_Iz,d_av_Iz))

##4b
w=np.array([500,18.8,370,24.5,430,22.5,520,18.4,590,16.16,310,29.5,410,22.8,465,20,350,27.8,540,16.5])
w.shape=(10,2)
w[:,0]=w[:,0]/60
w=w[w[:,0].argsort()]##sortiert nach der Drehfrequenz
print(w)
w_freq=1/w[:,1]*10
w_yerr=1/w[:,1]*w_freq
plt.errorbar(w[:,0], w_freq, xerr=5/60, yerr=w_yerr)
(slope, intercept), cov=optimize.curve_fit(lambda x,a,b:a*x+b,w[:,0],w_freq,sigma=w_yerr)
plt.plot(np.linspace(5,10),np.linspace(5,10)*slope+intercept)
plt.show()
print("Steigung: %.3f +- %.3f" % (slope , np.sqrt(cov[0][0])))
Ix=av_Iz/((1/slope)-1)+av_Iz
d_Ix=Ix/slope*np.sqrt(cov[0][0])
print("Ix=%.2f+-%.2f"%(Ix,d_Ix))

##5

w=np.array([585,540,670,630,435,410,580,540,650,603,862,800,763,710,410,380,660,620,480,450])
w.shape=(10,2)
w=w[w[:,0].argsort()]
print(w)
plt.errorbar(w[:,0],w[:,1],xerr=5,yerr=5, fmt=".")
(slope,), ((cov,),)=optimize.curve_fit(lambda x, a: a*x,w[:,0],w[:,1], p0=1)
plt.plot(np.linspace(400,900),np.linspace(400,900)*slope)
plt.show()
print("Steigung: %.4f+-%.4f"%(slope,np.sqrt(cov)))
Ix2=av_Iz/slope
d_Ix2=Ix2/slope*np.sqrt(cov)
print("Ix: %.2f+.%.2f"%(Ix2,d_Ix2))