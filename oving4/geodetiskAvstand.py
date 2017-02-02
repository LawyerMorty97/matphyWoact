#!/usr/bin/python3
#
# Utgangspunkt for løsning av øving 4
# Studenten skal lage en metode som regner ut storsirkelavstanden
# mellom punkter på jordkloden utifra angitt bredde- og lengdegrad.
#
# Ingredienser: Sfæriske polarkoordinater, skalarprodukt, buelengde langs sirkelbuer.
#


RADIUS_I_KILOMETER= 6371 # KILOMETER


class posisjon:

    def __init__(self,breddegrad,lengdegrad):
        self._lat = breddegrad 
        self._lon = lengdegrad
        # MRK: Enkel underscore i '_lat' indikerer at jeg ønsker at 
        # '_lat' skal behandles som en privat variabel. 
        # Det er opp til utvikleren om man vil respektere dette,
        # i og med at python ikke har noen innebygget mekanisme for
        # private variabler.

    def koordinater():
        x, y,z = 0,0,0 # TODO: FYLL INN DET SOM MANGLER
        return x,y,z


def geodetiskAvstand(A,B):
    """ Returnerer avstanden langs en storsirkel mellom to posisjoner på jordkloden, 
    representert ved `posisjon`-objekter A og B
    """
    # TODO: FYLL INN DET SOM MANGLER
    return 0 


def main():
    oslo = posisjon(59.911,10.761)
    london = posisjon(51.481,0.0)
    print("Storsirkelavstanden mellom Oslo og London er ifølge dette scriptet",geodetiskAvstand(oslo,london),"kilometer.")
    print("Ifølge distancecalculator.net er den korrekte avstanden på omtrent 1153 kilometer")


if __name__=="__main__":
    main()
