# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:36:34 2019

@author: jojos
"""

import numpy as np 
##nach Clement und Desormes
h1_r=np.array([64.7,64.4,64.5,64.9,64.8])
h3_r=np.array([61.9,61.6,61.6,61.7,61.7])
h1_l=120.5-h1_r
h3_l=120.5-h3_r
h1=h1_r-h1_l
h3=h3_r-h3_l
print(h1)
print(h3)
fehler_h3=np.sqrt(2*0.1**2+0.5**2)
fehler_h1=np.sqrt(2*0.1**2+0.5**2)
k=h1/(h1-h3)
k_error=np.sqrt((h3/(h1-h3)**2*fehler_h1)**2+(h1/(h1-h3)**2*fehler_h3)**2)
print("k=",k ,"+-" ,k_error)
k_mittel=np.average(k)
d_k_mittel=np.sqrt(np.var(k)+np.max(k_error)**2)
print("K Mittlewert: %.2f +- %.2f"%(k_mittel,d_k_mittel))
##nach Rüchhardt
T=np.array([46,49.42])/50
Error_T=np.array([0.2,0.3])/50
m=np.array([26.006,26.1168])
Error_m=np.array([0.002,0.002])
V=np.array([5460,5370])
Error_V=np.array([5,5])
p=1021
Error_p=1
r=np.array([15.97,15.95])/2
Error_r=np.array([0.05,0.02])/2
k_2=4*m*V/r**4/T**2/p
Error_k=k_2*np.sqrt((2*Error_T/T)**2+(Error_m/m)**2+(Error_V/V)**2+(Error_p/p)+(4*Error_r/r)**2)
print("kappa =" ,k_2, "+-", Error_k)
