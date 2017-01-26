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

    def _coords():
        x, y,z = 0,0,0 # TODO: FYLL INN DET SOM MANGLER
        return x,y,z


def geodetiskAvstand(A,B):
    """ Returnerer avstanden langs en storsirkel mellom to posisjoner på jordkloden, 
    representert ved `posisjon`-objekter A og B
    """
    # TODO: FYLL INN DET SOM MANGLER
    return 0 


if __name__=="__main__":
    oslo = posisjon(59.95,10.75)
    london = posisjon(51.50,0.0)
    print("Storsirkelavstanden mellom Oslo og London er ifølge dette scriptet",geodetiskAvstand(oslo,london),"kilometer.")
    print("Ifølge distancecalculator.net er den korrekte avstanden på omtrent 1153 kilometer")
