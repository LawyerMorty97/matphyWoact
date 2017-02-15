#!/usr/bin/python3

# Her foreslår jeg å representere punkter og vektorer med 2-tupler, altså par av tall.
# For å kunne teste løsningen med den angitte main-metoden, er man nødt til å
# følge det valget.

# MULIG NYTTIG HJELPEMETODE?
def forflytning(A,B):
    return tuple((b-a for a,b in zip(A,B)))

def trekantAreal(A,B,C):
    """Returnerer det orienterte arealet av trekanten A,B,C.
    Forutsetter at A,B,C er lister eller tupler med 2 komponenter.
    """
    return 0

def areal(punkter):
    """Returnerer det orienterte arealet av polygonet representert
    av parameteren `punkter`. `punkter` er en liste som inneholder
    punktene som utgjør polygonet. 
    """
    if (len(punkter) < 3): 
        return 0 # Hvis polygonet har færre enn 3 kanter, kan det ikke omslutte et areal
    # TODO: Fyll inn det som mangler.
    return 0


def main():
    A,B,C = (-1,-1), (1,-1),(0,1)  # Fin test-case: Har areal 2

    print("Beregnet areal av trekant[",A,B,C,"] = ",trekantAreal(A,B,C))
    print("Forventet resultat: 2")

    enhetsKvadrat = [(0,0),(1,0),(1,1),(0,1)] # Fin test-case: Har areal 1
    print("Beregnet areal av kvadrat",enhetsKvadrat," = ",areal(enhetsKvadrat) )
    print("Forventet resultat: 1")

    polygon = [(0,0),(4,0),(4,1),(2,2),(0,1)] # Test case: areal = 6
    print("Beregnet areal av polygon",polygon," = ",areal(polygon) )
    print("Forventet resultat: 6")
    

if __name__=='__main__':
    main()
