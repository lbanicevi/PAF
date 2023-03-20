import matplotlib.pyplot as plt
import numpy as np
def jednoliko_gibanje(F,m):
    a=float(F/m)
    akceleracija=[]
    brzina=[]
    vrijeme=[]
    put=[]
    t=0
    while t<=10:
        akceleracija.append(a)
        vrijeme.append(t)
        t=t+0.01
    
    vrijeme2=[]
    v=0
    t=0
    while t<=10:
        v=v+a*t
        brzina.append(v)
        vrijeme2.append(t)
        t=t+0.01
    
    vrijeme3=[]
    t=0
    s=0
    while t<=10:
        s=s+a*t**2
        put.append(s)
        vrijeme3.append(t)
        t=t+0.01
    
    plt.subplot(1,3,1)
    plt.plot(vrijeme,akceleracija)

    plt.subplot(1,3,2)
    plt.plot(vrijeme2,brzina)

    plt.subplot(1,3,3)
    plt.plot(vrijeme3,put)

    plt.show()

jednoliko_gibanje(4,3)

def kosi_hitac(v0,kut):
    radijani=kut*np.pi/180
    vrijeme=[]
    putx=[]
    t=0
    x=0
    while t<=10:
        x=v0*np.cos(radijani)*t
        putx.append(x)
        vrijeme.append(t)
        t=t+0.001
    vrijeme2=[]
    t=0
    g=9.81
    puty=[]
    while t<=10:
        y=(v0*np.sin(radijani))*t-1/2*g*t**2
        puty.append(y)
        vrijeme2.append(t)
        t=t+0.001

    plt.subplot(1,3,1)
    plt.plot(vrijeme,putx)

    plt.subplot(1,3,2)
    plt.plot(vrijeme,puty)

    plt.subplot(1,3,3)
    plt.plot(putx,puty)

    plt.show()
kosi_hitac(20,45)