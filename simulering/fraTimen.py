#!/usr/bin/python3

from animasjon import animasjon
from geometri3D import vektor3D as vec

G = 2.959122e-4


xJord = vec(-7.3423e-1,-6.8292e-1,-1.1499e-4)
vJord = vec(1.1456e-2,-1.2634e-2,-5.7432e-8)

distJordSol = xJord.lengde()


def solGravitasjon(posisjon):
    #Regn ut gravitasjon
    return akselerasjon



if __name__=='__main__':
    
    data = [ ( (0.01*i,0.02*i), (0,0) ) for i in range(100) ]

    animasjon(data)


