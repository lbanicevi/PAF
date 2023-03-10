def koordinate():
    x1=int(input("Unesi x koordinatu"))
    y1=int(input("Unesi y koordinatu"))
    x2=int(input("unesi x koordinatu"))
    y2=int(input("unesi y koordinatu"))
    print((x1,y1),(x2,y2))
    a=(y2-y1)/(x2-x1)
    b=-a*x1+y1
    print(a,b)
    print(" y={}*x + {}".format(a,b))
koordinate()