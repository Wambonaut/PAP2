# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:35:49 2019

@author: jojos
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#Wellenlänge
Messanfang=np.array([200,1472,770,320,374])
Messende=np.array([3162,4438,3732,3372,3328])
Maxima=np.array([11170,11250,11134,11133,11140])
Fehler_Länge=9
Fehler_M=10
lambas=2*(Messende-Messanfang)/Maxima
Fehler_lambas=lambas*np.sqrt((Fehler_M/Maxima)**2+(Fehler_Länge/(Messende-Messanfang))**2)
print(lambas ,"+-" ,Fehler_lambas)
lamb_av=np.average(lambas)
lamb_error=1/np.sqrt(5)*np.sqrt(np.sum(Fehler_lambas**2))

print("Average=",lamb_av, "+- ",lamb_error )
#Brechungsindex
m=np.array([0,5,10,15,20,25,30,35,40,45])
p_1=np.array([-730,-630,-565,-490,-410,-335,-245,-165,-100,-20])*133.322
p_2=np.array([-740,-660,-585,-510,-440,-360,-290,-210,-140,-60])*133.322
p_3=np.array([-700,-650,-580,-510,-430,-380,-285,-210,-125,-50])*133.322
p_fehler=10

def linear1(a,x,b):
    return a*x+b
popt1,pcov1=curve_fit(linear1,m,p_1)
plt.errorbar(m,p_1,yerr=p_fehler,fmt='.',label="Werte 1. Messreihe")
plt.plot(m,linear1(m,*popt1),label="linearer Fit erste Messreihe")
def linear2(a,x,b):
    return a*x+b
popt2,pcov2=curve_fit(linear2,m,p_2)
plt.errorbar(m,p_2,yerr=p_fehler,fmt='.',label="Werte 2. Messreihe")
plt.plot(m,linear2(m,*popt2),label="linearer Fit 2. Messreihe")
def linear3(a,x,b):
    return a*x+b
popt3,pcov3=curve_fit(linear3,m,p_3)
plt.errorbar(m,p_3,yerr=p_fehler,fmt='.',label="Werte 3. Messreihe")
plt.plot(m,linear3(m,*popt3),label="linearer Fit 3. Messreihe")
plt.ylabel("Druck in Pa")
plt.xlabel("Anzahl der Maxima")
plt.legend()
plt.show()
steigungen=np.array([popt1[0],popt2[0],popt3[0]])
print("Steigung1=%.2f+-%.2f"%(popt1[0], np.sqrt(pcov1[0][0])))
print("Steigung2=%.2f+-%.2f"%(popt2[0], np.sqrt(pcov2[0][0])))
print("Steigung3=%.2f+-%.2f"%(popt3[0], np.sqrt(pcov3[0][0])))
a_mw=np.average(steigungen)
a_fehler=1/np.sqrt(3)*np.sqrt((pcov1[0][0])**2+(pcov2[0][0]**2)+(pcov3[0][0])**2)
print("Steigung_mw=%.2f+-%.2f"%(a_mw, np.sqrt(a_fehler)))
lamb=532e-9
a=0.05
a_error=5e-5
lamb_error=1e-9
p0=101325
T0=273.15
T=23.4+273.15
t_error=0.1
n_m_1=lamb/2/a/a_mw*p0*T/T0
n_m_1_error=n_m_1*np.sqrt((a_error/a)**2+(lamb_error/lamb)**2+(t_error/T)**2)
print("n0-1=%.5e+-%.2e"%( n_m_1,n_m_1_error))
