#!/usr/bin/python3
#
# Skjelettkode for oppgave 2 d)
#

import math


# Kan komme til nytte?
def dot(u,v):
    return 0

# Dette handler oppgaven om 
def dekomposisjon(u,v):
    # SKRIV INN KODE HER
    return [0 for ui in u],[0 for vi in v] # Denne linjen må naturligvis også endres




if __name__=="__main__":
    u = [3,4,3]
    v = [4,3,2]

    vParallell, vPerp = dekomposisjon(u,v)


    print(vParallell,vPerp)
