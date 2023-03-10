import matplotlib.pyplot as plt
x1=int(input("Unesi x koordinatu"))
y1=int(input("Unesi y koordinatu"))
x2=int(input("unesi x koordinatu"))
y2=int(input("unesi y koordinatu"))
x=[x1,x2]
y=[y1,y2]
plt.plot(x,y)
pitanje=input("unesite 1 za spremanje kao pdf; i 0 za pokazivanje na ekranu ")
if pitanje==1:
    plt.savefig("zdk5.pdf")
else:
    plt.show()
