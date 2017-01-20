#!/usr/bin/python3
#
# Kommer antageligvis kun til å inneholde
# metoden `abc` for løsning av andregradsligninger.
#

import math


def abc(a,b,c):
    """ 
    Løser annengradsligningen a*x**2 + b*x + c = 0
    ved å bruke abc-formelen.

    Returnerer et tuppel med 0,1 eller 2 elementer,
    avhengig av antallet løsninger av ligningen.
    """
    d = -0.5*b/a
    diskriminant = b*b-4*a*c

    if diskriminant < 0:
        return ()
    if diskriminant == 0:
        return (d,)

    e = 0.5*math.sqrt(diskriminant)/a

    x1 = (d+e) if (d*e > 0) else (d-e) 
    x2 = c/a/x1

    return (x1,x2) if (x1 < x2) else (x2,x1)


if __name__=='__main__':
    print('løsning av x**2+2x-3 = 0: ',abc(1,2,-3), '(Korrekt svar skal være (-3.0,1.0))')
