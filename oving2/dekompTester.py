#!/usr/bin/python3

from dekomposisjon import dekomposisjon as dekomp
import random

def dot(u,v):
    return sum( ui*vi for (ui,vi) in zip(u,v) )

def add(u,v):
    return [ ui+vi for (ui,vi) in zip(u,v)]

def erLike(u,v):
    return all( ui==vi for (ui,vi) in zip(u,v) )

def erParallelle(u,v):
    return dot(u,v)**2 - dot(u,u)*dot(v,v) == 0

def testDecomp():
    n = random.randint(0,10)
    rand = lambda : random.uniform(-1,1)
    u = [rand() for i in range(n)]
    v = [rand() for i in range(n)]

    print("Test-vektorer:\n{}\n{}".format(u,v))

    
    vPerp,vParallell = dekomp(u,v)

    assert erLike(add(vPerp,vParallell) , v), "Dekomposisjonen summerer seg ikke opp til den gitte vektoren"
    assert dot(vPerp,u) == 0, "vPerp står ikke vinkelrett på u"
    assert erParallelle(vParallell,u), "vParallell er ikke parallell med u"


if __name__=="__main__":
    testDecomp()
