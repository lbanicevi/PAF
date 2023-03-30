import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]  #proizvoljno uzete točke
y=[11,12,11,14,15,16,17,18,19,20]
sumax=sum(x) #zbroj svih članova u listama
sumay=sum(y)
arthx=sumax/len(x) #artimetička sredina je zbroj svih članova kroz broj koliko ih ima
arthy=sumay/len(y)
print(arthx)
print(arthy)

n=10 #uzelo se 10 točaka
devx=0
dev1=[]
a=0
for el in x: # svaki član iz liste uvrsti u formulu
    a+=((el-arthx)**2)/n*(n-1) #formula za devijaciju
    devx=np.sqrt(a)   #formula za devijaciju
    dev1.append(devx)
print(dev1)

b=0
devy=0
dev2=[]
for el in y:
    b+=((el-arthy)**2)/n*(n-1)
    devy=np.sqrt(b)
    dev2.append(b)
print(dev2)

plt.scatter(dev1,dev2)
plt.show()
