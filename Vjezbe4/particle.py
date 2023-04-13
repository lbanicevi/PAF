import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v0,fi,x0,y0, dt = 0.001): #fi je kut otklona; x0 i y0 su koordinate početnog položaja
        self.v0=v0
        self.fi=fi
        self.x0=x0
        self.y0=y0
        self.dt = dt
        self.putx = []
        self.puty = []

    def info(self):                             #isprinta mi podatke o čestici
        print("v0:", self.v0)
        print("x0:", self.x0)
        print("y0:", self.y0)
        print("kut:", self.fi)

    def reset(self):                            #funkcija koja vraća se podatke na nulu
        self.v0 = 0
        self.y0 = 0
        self.x0 = 0
        self.fi = 0
        self.putx = []                          #iz liste ova funkcija briše sve podatke
        self.puty = []

    def __move(self, F, m, t):                  #__ znaći da je privatna metoda odnosno da je ne mogu svi koristiti
        
        #pocetni podaci
        t0 = 0
        dt = 0.001
        g = 9.81
        vx0 = self.v0 * np.cos((self.fi / 180) * np.pi)  #formula za x komponentu brzine
        vy0 = self.v0 * np.sin((self.fi / 180) * np.pi)  #formula za y komponentu brzine

        while t0 < t:                      
            self.x0 = self.x0 + vx0 * dt    #fomrula za put x(kosi kitac)
            self.putx.append(self.x0)        
            vy = vy0 - g * dt               #za put po y trebam definirati vy
            self.vy0 = vy
            self.y0 = self.y0 + vy * dt
            self.puty.append(self.y0)
            t0 = t0 + dt

    def range(self):
        #pocetni podaci
        t = 0
        g = 9.81
        vx0 = self.v0 * np.cos((self.fi / 180) * np.pi)     #formula i iznos x komponente brzine
        vy0 = self.v0 * np.sin((self.fi / 180) * np.pi)     #formula i iznos y komponente brzine

        while self.y0 >= 0:                 #domet traje sve dok je y nije nula odnosno sve dok se tijelo ne dodirne tlo

            self.x0 = self.x0 + vx0 * self.dt       #formula za x put
            self.putx.append(self.x0)

            self.y0 = self.y0 + vy0 * self.dt       #fomrula za y put
            self.puty.append(self.y0)
            
            vy0 = vy0 - g * self.dt

            t = t + self.dt

        self.x0 = self.putx[-1]             # numericki domet
        self.y0 = 0                         # da tijelo ne ode ispod nule
        return self.putx[-1]
    
    def plot_trajectory(self):
        plt.plot(self.putx, self.puty)
        plt.show()
        
    def analiticki_domet(self):
        a_domet = ((self.v0)**2 * np.sin(2 * ((self.fi / 180) * np.pi))) / 9.81    #formula za analiticki domet
        return a_domet