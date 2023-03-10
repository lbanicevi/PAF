x01=input("Unesi x koordinatu")
y01=input("Unesi y koordinatu")
x02=input("unesi x koordinatu")
y02=input("unesi y koordinatu")
if x01.isdigit() and  x02.isdigit() and y01.isdigit() and  y02.isdigit():
    x1=int(x01)
    y1=int(y01)
    x2=int(x02)
    y2=int(y02)
    a=(y2-y1)/(x2-x1)
#y-y1=k*(x-x1)--> y=kx+(-kx1+y1)
    b=-a*x1+y1
    print(" y={}*x + {}".format(a,b))
else:
    print("kriv unos")