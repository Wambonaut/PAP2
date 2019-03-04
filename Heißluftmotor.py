# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:59:07 2019

@author: jojos
"""

import numpy as np 
import matplotlib.pyplot as plt
c_w=4180
Durchfluss=np.array([211.3,209.2,211.2,211.8,210.7])/600000
Durchfluss_avg=np.average(Durchfluss)
Durchfluss_Fehler=np.std(Durchfluss)
Drehzahl=286/60
Fehler_Drehzahl=0.1/60
Strom_Heiz=1.03*5
Fehler_Strom_Heiz=0.01*5
Spannung_Heiz=5.23
Fehler_Spannung_Heiz=0.01
Leistung_Heiz=Strom_Heiz*Spannung_Heiz/Drehzahl
Fehler_Leistung_Heiz=Leistung_Heiz*np.sqrt((Fehler_Spannung_Heiz/Spannung_Heiz)**2+(Fehler_Strom_Heiz/Strom_Heiz)**2+(Fehler_Drehzahl/Drehzahl)**2)
print("Leistung_Heiz=", Leistung_Heiz, "+-", Fehler_Leistung_Heiz, "Watt")
Spannung_Motor=24
Fehler_Spannung_Motor=0.1
Strom_Motor=1.65
Fehler_Strom_Motor=0.05
Leistung_Motor=Strom_Motor*Spannung_Motor/Drehzahl
Fehler_Leistung_Motor=Leistung_Motor*np.sqrt((Fehler_Spannung_Motor/Spannung_Motor)**2+(Fehler_Strom_Motor/Strom_Motor)**2+(Fehler_Drehzahl/Drehzahl)**2)
Fehler_Diskrepanz=np.sqrt((Fehler_Leistung_Motor)**2+(Fehler_Leistung_Heiz)**2)
print("Leistung_Motor=", Leistung_Motor, "+-", Fehler_Leistung_Motor, "Watt")
print("Diskrepanz=", Leistung_Motor-Leistung_Heiz,"+-",Fehler_Diskrepanz, "Watt")

Masse_Wasser=1
T2=510
T1=320
dT=T2-T1
Fehler_dT=np.sqrt(2)*10
Schmelzwärme=335
Fehler_Schmelzwärme=0.01*Schmelzwärme
Leistung=Schmelzwärme/dT/Drehzahl
Fehler_Leistung=Leistung*np.sqrt((1/Schmelzwärme*Fehler_Schmelzwärme)**2+(Fehler_dT/dT)**2+(Fehler_Drehzahl/Drehzahl)**2)
print("Leistung=", Leistung, "+-", Fehler_Leistung, "Watt")

Länge_Zaum=0.25
dT_Kühlwasser=23.8-17.9
Fehler_dT_Kühlwasser=1.5
Kraft=np.array([0,0.2,0.4,0.6,0.8])
V_kühlwasser=208
V_kühlwasser_error=5
Fehler_Kraft=np.array([0,0.1,0.1,0.1,0.1])
Heizspannung=np.array([10.79,10.73,10.73,10.73,10.73])
Error_Heizspannung=0.05
Heizstrom=2.35
Error_Heizstrom=0.01
Frequenzen=[[304.5,304.5,306],[305,304,303],[266,267,265],[241,240,239],[200,199,200]]
Fehler_Frequenzen=1
Frequenzen_avg=np.array([np.average(Frequenzen[n])/60. for n in range(5)])
Fehler_Frequenzen_avg=np.array([np.std(Frequenzen[n])/60. for n in range (5)])
Intbereiche=[[16908,17751,16986],[19198,19314,18928],[21297,21322,20919],[23686,23351,23278],[24822,24921,24879]]
Intbereich_avg=np.array([np.average(Intbereiche[n])*10**(-4) for n in range(5)])
Fehler_Intbereiche_avg=np.array([np.std(Intbereiche[n])*10**(-4) for n in range(5)])

Q_el=Heizspannung*Heizstrom/Frequenzen_avg
Q_el_error=Q_el*np.sqrt((Error_Heizspannung/Heizspannung)**2+(Error_Heizstrom/Heizstrom)**2+(Fehler_Frequenzen_avg/Frequenzen_avg)**2)
Q_ab=c_w*dT_Kühlwasser*Durchfluss_avg/Frequenzen_avg
Fehler_Q_ab=Q_ab*np.sqrt((Fehler_dT_Kühlwasser/dT_Kühlwasser)**2+(Durchfluss_Fehler/Durchfluss_avg)**2+(Fehler_Frequenzen_avg/Frequenzen_avg)**2)
P_el=Heizspannung*Heizstrom
Fehler_P_el=P_el*np.sqrt((Error_Heizspannung/Heizspannung)**2+(Error_Heizstrom/Heizstrom)**2)
P_ab=Q_ab*Frequenzen_avg
Fehler_P_ab=P_ab*np.sqrt((Fehler_Q_ab/Q_ab)**2+(Fehler_Frequenzen_avg/Frequenzen_avg)**2)
P_pv=Intbereich_avg*Frequenzen_avg
Fehler_P_pv=P_pv*np.sqrt((Fehler_Intbereiche_avg/Intbereich_avg)**2+(Fehler_Frequenzen_avg/Frequenzen_avg)**2)
Q_pv=P_pv/Frequenzen_avg
Fehler_Q_pv=Q_pv*np.sqrt((Fehler_P_pv/P_pv)**2+(Fehler_Frequenzen_avg/Frequenzen_avg)**2)
n_th=Intbereich_avg/Q_el
Fehler_n_th=n_th*np.sqrt((Fehler_Intbereiche_avg/Intbereich_avg)**2+(Q_el_error/Q_el)**2)
print ("Q_el=", Q_el,"+-",Q_el_error) 
print ("P_el=", P_el,"+-",Fehler_P_el) 
print ("P_ab=", P_ab,"+-",Fehler_P_ab)  
print ("Q_ab=", Q_ab,"+-",Fehler_Q_ab)
print ("P_pv=", P_pv,"+-",Fehler_P_pv)
print ("Q_pv=", Q_pv,"+-",Fehler_Q_pv)
print ("n_th=", n_th,"+-",Fehler_n_th)
print ("f=", Frequenzen_avg,"+-",Fehler_Frequenzen_avg)

Q_V=Q_el-Q_ab-Intbereich_avg
Error_Q_V=np.sqrt((Q_el_error)**2+(Fehler_Q_ab)**2+(Fehler_Intbereiche_avg)**2)

print("Q_V=", Q_V , "+-", Error_Q_V)

W_D=2*np.pi*Länge_Zaum*Kraft
Error_W_D=W_D/Kraft*Fehler_Kraft
n_eff=W_D/Q_el
Fehler_n_eff=n_eff*np.sqrt((Error_W_D/W_D)**2+(Q_el_error/Q_el)**2)

plt.errorbar(Frequenzen_avg,n_th,yerr=Fehler_n_th,xerr=Fehler_Frequenzen_avg,label='n_th')
plt.errorbar(Frequenzen_avg,n_eff,yerr=Fehler_n_eff,xerr=Fehler_Frequenzen_avg,label='n_eff')
plt.xlabel("Frequenz/ 1/s")
plt.ylabel("n")
plt.legend(loc="best")
plt.title("n in Abhängigkeit von f")
plt.show()

