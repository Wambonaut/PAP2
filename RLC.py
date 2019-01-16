#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 22:34:05 2019

@author: wambo
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
f=np.linspace(1,10,10)*1000
phi=np.array([1.26,1.00,0.073,0.065,0.055,0.048,0.040,0.036,0.033,0.030])/np.pi*180
plt.plot(f, phi)
plt.xscale("log")
plt.show()
phi_Grenz=(45-phi[2])/(phi[1]-phi[2])*3000+(phi[1]-45)/(phi[1]-phi[2])*2000
print("Phi_Grenz: ",phi_Grenz)
print("Fehler grob abgeschätzt: 200")
print("Theoretischer Wert:", 1/(2*np.pi*1e3*47e-9))


##bestimmen von L aus den Resonanzfreuqnzen
L=lambda f, C: 1/(2*np.pi*f)**2/C
L_ERROR=lambda df, f, C: 2/(2*np.pi)**2/f**3/C*df
print("Messung R=1kOhm: L=", L(3440, 47e-9) , "+-", L_ERROR(10, 3440, 47e-9))
print("Messung über R=22Ohm,47 Ohm: L=", L(3300, 47e-9), "+-", L_ERROR(10,3300, 47e-9))

##bestimmen von R+Rv
RvR=lambda b1,b2,f,C: (b2-b1)*2*np.pi*L(f,C)
RvR_ERROR=lambda b1,b2,f,C:np.sqrt(2*(50/f)**2)*RvR(b1,b2,f,C)
print("Bestimminug von RV+R\n\n\nMessung 1: Rv+R=", RvR(2150,5550,3440,47e-9),"+-",RvR_ERROR(2150,5550,3440,47e-9))
print("Messung 2: Rv+R=", RvR(2850,3950,3300,47e-9),"+-",RvR_ERROR(2850,3950,3300,47e-9))
print("Messung 3: Rv+R=", RvR(3050,3550,3300,47e-9),"+-",RvR_ERROR(3050,3550,3300,47e-9))


##Bestimmen von Rv aus verhältnis ein und ausgangsspannung
Rv=lambda R, Ua, Ue: Ue*R/Ua-R
print("\n\nNUR FÜR STUDENTEN MIT HAUPTFACH PHYSIK:\nMessung 1: Rv=", Rv(1000,0.91,0.96))
print("Messung 2: Rv=", Rv(220,0.71,0.96))
print("Messung 3: Rv=", Rv(47,0.31,0.90))

##5. Bestimmung der Dämpfungskonstante
print("\n\n5. Bestimmung der Dämpfungskonstante\nL: Warte das ist doch gar keine Resonanzfrequenz")
amps=np.array([4.78,2.86,1.69,1.03,0.56])
fitfun=lambda x, a, b: a*np.exp(-b*x)
popt, pcov = optimize.curve_fit(fitfun,np.linspace(0,0.00145,5),amps,p0=[5,20])
plt.plot(np.linspace(0,0.00145,50),fitfun(np.linspace(0,0.00145,50), *popt))
plt.errorbar(np.linspace(0,0.00145,5),amps, yerr=0.1, fmt="none")
plt.show()
print("Dämpfungskonstante aus Fit:", popt[1],"+-",np.sqrt(pcov[1][1]))
print("Daraus R+RV:",popt[1]*2*L(3440, 47e-9),"+-",popt[1]*2*L(3440, 47e-9)*np.sqrt(pcov[1][1]/popt[1]**2+L_ERROR(10,3440,47e-9)))
##Bestimmung aus Logarithmischem Dekrement
T=0.00145/4
T_ERROR=0.0003/4
logarithmic_dek=np.array([np.log(amps[i]/amps[i+1]) for i in range(4)])
logarithmic_dek_ERROR=logarithmic_dek*np.array([1/(amps[i]/amps[i+1])*0.05 for i in range(4)])
damp_const=logarithmic_dek/T
amps_ERROR=0.05
damp_const_ERROR=damp_const*np.sqrt((logarithmic_dek_ERROR/logarithmic_dek)**2+2*(amps_ERROR/amps[:-1])**2)
print("\n\nBestimmung der Dämpfungskonstante aus logarithmischem Dekrement")
for i in range(4):
    print("Logarithmisches Dekrement %i: %.3f +- %.3f\nDaraus Dämpfungskonstante %.1f+-%.1f" % (i+1,logarithmic_dek[i], logarithmic_dek_ERROR[i], damp_const[i],damp_const_ERROR[i]))
print("\n\nDurchschnittliches Dekrement: %.3f +- %.3f\nDurchschnittliche Dämpfungskonstante%.1f +- %.1f"
      %(np.average(logarithmic_dek),np.sqrt(np.sum(np.square(logarithmic_dek_ERROR)))/2,np.average(damp_const),np.sqrt(np.sum(np.square(damp_const_ERROR)))/2))