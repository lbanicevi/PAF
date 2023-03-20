import matplotlib.pyplot as plt
import numpy as np
v0=int(input("Unesi početnu brzinu"))
kut=int(input("unesi kut otklona"))
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
