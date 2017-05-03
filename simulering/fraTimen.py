#!/usr/bin/python3

from animasjon import animasjon
from figur import figur
from geometri3D import vektor3D as vec

G = 2.959122e-4


xJord = vec(-7.3423e-1,-6.8292e-1,-1.1499e-4)
vJord = vec(1.1456e-2,-1.2634e-2,-5.7432e-8)

distJordSol = xJord.lengde()

# EKSEMPEL PÅ ALTERNATIV KRAFTLOVER
def dagligdagsGravitasjon(posisjon):
    return vec(0,0,-9.81)

def fjærkraftIOrigo(posisjon):
    K = 0.1 # Fjærkonstant
    return -K*posisjon




def solGravitasjon(posisjon):
    #Regn ut gravitasjon
    return akselerasjon




# Eksempel på simulering uten kraft, d.v.s. rettlinjet bevegelse
def testSimulering(n):
    h = 6*1.0/24 # Steglengde, målt i antall døgn
    x = xJord
    v = vJord
    for i in range(n):
        yield [x] # Liste av posisjoner
        x += h*v


# Eksempel på simulering med ubegrenset tid:
# Kan ikke brukes med statisk figur
def testSimuleringUbegrenset():
    h = 6*1.0/24 # Steglengde, målt i antall døgn
    x = xJord
    v = vJord
    while(True):
        yield [x] # Liste av posisjoner
        x += h*v





if __name__=='__main__':
    
    # Statisk figur 
    simulering = [p for p in testSimulering(1000)]
    xData = (p[0][0] for p in simulering)
    yData = (p[0][1] for p in simulering)

    fig = figur()
    fig.xmin,fig.ymin,fig.xmax,fig.ymax = -1.5,-1.5,1.5,1.5
    fig.kurve(xData,yData)
    fig.vis()

    # Animasjon
    animasjon(testSimuleringUbegrenset())

    

