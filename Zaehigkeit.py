#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:04:04 2019

@author: wambo
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
##mesurements made
mm9=[5.87, 5.86,5.82,5.76,5.66]
mm7_144=[4.20,4.12,4.15,4.14,4.18]
mm8=[3.81,3.78,3.62,3.62,3.70]
mm6=[2.68,2.68,2.65,2.81,2.92]
mm5=[3.58,3.65,3.62,3.67,3.68]
mm4=[5.64,5.66,5.62,5.80,6.07]
mm3=[8.72,9.53,9.86,9.98,10.09]
mm2=[20.07,20.10,20.31,20.95,20.48]
distance=np.array([50,50,50,50,50,100,100,200])
radius=np.array([2,3,4,5,6,7.144,8,9])/2
radius_tube=75/2
rho_k=np.array([1.377,1.377,1.377,1.377,1.377,1.377,1.357,1.362])
ladenburg_factor=1+2.1*radius/radius_tube
rho_f=1.1475

##calculate avges
avges=np.array([np.average(a) for a in [mm2,mm3,mm4,mm5,mm6,mm7_144,mm8,mm9]])
avges_ERROR=np.array([np.sqrt(np.var(a)) for a in [mm2,mm3,mm4,mm5,mm6,mm7_144,mm8,mm9]])

##calculate the y-axis factor
rel_velocities=distance/avges/(rho_k-rho_f)
rel_velocities_ERROR=rel_velocities*np.sqrt((avges_ERROR**2+0.2**2)/avges**2 + 5**2/distance**2+2*0.005**2/rho_k**2)
r2=radius**2

##plot the factors, and linear fit them
plt.errorbar(r2,rel_velocities, rel_velocities_ERROR, fmt=".", label="Messwerte")
(slope,), cov=optimize.curve_fit(lambda x, a: a*x, r2, rel_velocities, p0=[2],sigma=rel_velocities_ERROR)
ny=2*980.9/(9*slope)*10
plt.plot(np.linspace(0,25,20),np.linspace(0,25,20)*slope, label="Fit an die Messwerte")

##Ladenburg-Correcture and do the same again
rel_velocities_corr=rel_velocities*ladenburg_factor
rel_velocities_corr_ERROR=rel_velocities_ERROR*ladenburg_factor
r2=radius**2
plt.errorbar(r2,rel_velocities_corr, rel_velocities_corr_ERROR, fmt=".", label="Korrigierte Messwerte")
(slope_corr,), cov_corr=optimize.curve_fit(lambda x, a: a*x, r2[:4], rel_velocities_corr[:4], p0=[2],sigma=rel_velocities_corr_ERROR[:4])
ny_corr=2/9*980.9/slope_corr*10
plt.plot(np.linspace(0,25,20),np.linspace(0,25,20)*slope_corr, label="Korrigierter Fit")
plt.legend()
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.xlabel("Kugelradius r²[mm²]")
plt.ylabel("Velocity smth")
plt.show()
print("Ny Korrigiert: %.2f+-%.2f mPa*s"%(ny_corr,ny*np.sqrt((cov_corr[0][0]))/slope_corr))


##Now do the Reynoldszahlthing
v_lam=2/9*9.81*(rho_k+rho_f)/ny_corr*r2
reynhols=rho_f*distance/avges*radius*2/ny_corr
plt.plot(reynhols, distance/avges/v_lam, linestyle="-")
plt.xscale("log")
plt.xlabel("Reynholszahl")
plt.ylabel("v_lam/v")
plt.show()

##Hagen-Poisseuille
V=np.array([5,10,15,20,25])
t=np.array([1*60+35,3*60+40,5*60+57,8*60+8,10*60+26])
t_ERROR=5
plt.errorbar(t,V, xerr=t_ERROR, fmt=".")
(V_per_t,intercept), V_per_t_cov=optimize.curve_fit(lambda x,a,b: a*x+b, t,V, p0=[0.05,0], sigma=[0.05*t_ERROR]*5)
plt.plot(np.linspace(0,700), np.linspace(0,700)*V_per_t+intercept)
filling_avg=(513.5+510.5)/2/10#cm
filling_avg_ERROR=np.sqrt(2)*0.5/2/10
R=1.5/2/10
ny_hp=np.pi*981*rho_f*filling_avg*R**4/8/V_per_t*10
ny_hp_ERROR=ny_hp*np.sqrt((filling_avg_ERROR/filling_avg)**2+(np.sqrt(V_per_t_cov[0,0])/V_per_t)**2)
plt.show()
print("Ny Hagen-Poiseuille %.2f +- %.2f mPa*s" %(ny_hp, ny_hp_ERROR))
Re=2*rho_f*V_per_t/(np.pi*ny_hp*R)*100
Re_ERROR=Re*np.sqrt((np.sqrt(V_per_t_cov[0][0])/V_per_t)**2)
print("Reynholszahl des Kapillars: %.4f +- %.4f"%(Re,Re_ERROR))