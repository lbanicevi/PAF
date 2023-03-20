import matplotlib.pyplot as plt
import numpy as np
F=float(input("Unesi silu (N)"))
m=float(input("unesi masu (kg)"))
a=float(F/m)
akceleracija=[]
vrijeme=[]
brzina=[]
put=[]
#a-t graf
t=0 #definiram početno vrijeme
while t<=10: #sve dok je t manji ili jednak 10
    vrijeme.append(t)  #dodajem u listu vremena
    t=t+0.001     #nakon svakog dodanog povećam t za određeni broj
    akceleracija.append(a)  #sa svakim povećanjem vremena, dodam i akceleraciju u listu

#v-t
v0=0 #definiram početnu brzinu
v=0
t=0
vrijeme2 = []
while t<=10: 
    v=v0+a*t    #formula za brzinu
    brzina.append(v) #sve dok je vrijeme manje ili jednako 10
    vrijeme2.append(t)  #dodajem vremena u listu
    t=t+0.001    #i nakon svakog dodavanja ih povećavam

#s-t
s0=0
s=0
t=0
vrijeme3 = []
while t<=10:
    s=s0+a*t**2
    put.append(s)
    vrijeme3.append(t)
    t=t+0.001

plt.subplot(1,3,1)
plt.xlabel("t(s)")
plt.ylabel("a(m/s**2)")
plt.plot(vrijeme, akceleracija)

plt.subplot(1, 3, 2)
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.plot(vrijeme2, brzina)

plt.subplot(1, 3, 3)
plt.xlabel("t(s)")
plt.ylabel("s(m)")
plt.plot(vrijeme3, put)

plt.show()