def iteracija(broj):
    a = 5 # definiram broj od kojeg oduzimam i zbrajam
    for i in range(broj): # za svaki broj u nizu, dodajem 1/3 broju 5 odnosno a
        a += (1/3)
    for i in range(broj): #za svaki broj u nisu oduzimam 1/3 broju 5
        a -= (1/3)
    print(a)

iteracija(200)
iteracija(2000)
iteracija(20000)

