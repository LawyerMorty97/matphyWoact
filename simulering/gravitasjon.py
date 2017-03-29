#!/usr/bin/python3

from geometri2D import punkt2D,vektor2D,forflytning
from figur import figur

# MER ELLER MINDRE TILFELDIG VALGTE VERDIER
STEGLENGDE = 0.1
G = 0.02
M1 = 1
M2 = 1
O = punkt2D(0,0)

X0 = punkt2D(3,0)
V0 = vektor2D(0,0.1)

# NEWTONS GRAVITASJONSLOV
def sentralGravitasjon(pos):
    d = forflytning(O,pos)
    r = d.lengde()
    return -G*M1*M2/r**3*d

    
# SIMULERINGSSTEG, MED KONSTANT AKSELERASJON
def neste(x,v,m = M1,kraft = sentralGravitasjon,h = STEGLENGDE):
    kraft = sentralGravitasjon(x)
    a = 1.0/m*kraft
    nyV = v+h*a
    nyX = x + h*v + 0.5*h**2*a
    return nyX,nyV


# KJØRING AV MANGE STEG MED GENERATOR.
def simulering(n):
    x,v = X0,V0
    yield x
    for i in range(n):
        x,v = neste(x,v)
        yield x


if __name__=='__main__':
    fig = figur(800,800)
    fig.xmin,fig.xmax,fig.ymin,fig.ymax = -10,10,-10,10
    O.tegn(fig)
    for x in simulering(100000):
        x.tegn(fig)
    fig.vis()

