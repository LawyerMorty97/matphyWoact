#!/usr/bin/python3

from dekomposisjon import dekomposisjon as dekomp
import random

def dot(u,v):
    return sum( ui*vi for (ui,vi) in zip(u,v) )

def add(u,v):
    return [ ui+vi for (ui,vi) in zip(u,v)]

def erLike(u,v):
    return all( abs(ui-vi) < 1e-10 for (ui,vi) in zip(u,v) )

def erParallelle(u,v):
    return abs(dot(u,v)**2 - dot(u,u)*dot(v,v)) < 1e-10

def erOrtognoale(u,v):
    return abs(dot(u,v)) < 1e-10


def testDecomp():
    n = random.randint(0,10)
    rand = lambda : random.uniform(-1,1)
    u = [rand() for i in range(n)]
    v = [rand() for i in range(n)]

    print("Test-vektorer:\n{}\n{}".format(u,v))

    
    vPerp,vParallell = dekomp(u,v)

    assert erLike(add(vPerp,vParallell) , v), "Dekomposisjonen summerer seg ikke opp til den gitte vektoren"
    assert erOrtogonale(vPerp,u) , "vPerp står ikke vinkelrett på u"
    assert erParallelle(vParallell,u), "vParallell er ikke parallell med u"


if __name__=="__main__":
    testDecomp()
