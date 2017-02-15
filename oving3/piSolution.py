#!/usr/bin/python3

#
# Konvensjoner: 
# - Punkt = 2-tuppel = par, f.eks. P = (2,3)
# - Polygon = liste av punkter
# - Areal = Orientert areal. Positivt areal <-> orientering mot klokka
#

import math

def halvvering(A,B):
    """Regner ut midtpunktet mellom A og B og skalerer
    slik at punktet ligger på enhetssirkelen"""
    x = A[0]+B[0]
    y = A[1]+B[1]
    l = math.sqrt(x**2+y**2)
    return (x/l,y/l)


def forfining(subPolygon):
    """Gjør om et polygon av n punkter på enhetssirkelen
    til et polygon av 2*n punkter på enhetssirkelen
    ved å legge inn halvveringspunkter"""
    sp = subPolygon 
    output = []
    k = len(sp)
    for i in range(k):
        output.append(sp[i])
        output.append(halvvering(sp[i],sp[(i+1)%k]))
    return output

def polygon(n):
    """ Returnerer et regulært polygon med 2**n
    hjørner, der hjørnene ligger på enhetssirkelen"""
    current = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(n):
        current = forfining(current)
    return current



def skaleringsfaktor(indrePolygon):
    """Regner ut hvordan et polygon 
    må skaleres for at det skal ligge nøyaktig på utsiden
    av enhetssirkelen. 
    (Forutsetter at `indrePolygon` omfatter origo)
    """
    def midtpunkt(A,B):
        return tuple((0.5*(a+b) for a,b in zip(A,B)))

    def dist(P):
        return math.sqrt(sum(a**2 for a in P))

    ipoly = indrePolygon
    k = len(ipoly)

    midtpunkter = (midtpunkt(ipoly[i],ipoly[(i+1)%k]) for i in range(k))
    return 1/min(dist(m) for m in midtpunkter)


# Denne er litt kryptisk. Bruker generatorer. 
# For en mindre kryptisk variant, se listShift nedenfor
def shift(iterator):
    """Syklisk ombytting av elementene i iteratoren"""
    try:
        start = next(iterator)
    except TypeError as e:
        iterator = iter(iterator)
        start = next(iterator)

    yield from iterator
    yield start

# Mindre kryptisk variant av shift
def listShift(liste):
    """ Syklisk ombytting av liste """
    out = liste[1:] # Lager en ny liste som inneholder list[1],list[2],....
    out.append(liste[0]) # Legger liste[0] bakerst i listen out.
    return out


def areal(polygon):
    """Regner ut det orienterte arealet av polygonet 
    representert av punktene i listen `polygon`"""
    return 0.5*sum( (xi*yj-yi*xj for ((xi,yi),(xj,yj)) in zip(polygon,shift(polygon) )) )


# TEST 
def main():
    for i in range(10):
        indrePolygon = polygon(i)
        indreAreal = areal(indrePolygon)

        s = skaleringsfaktor(indrePolygon)
        ytrePolygon = [tuple((s*x for x in p)) for p in indrePolygon]
        ytreAreal = areal(ytrePolygon)

        print(indreAreal,"\t< pi < \t",ytreAreal ,"\tgyldig?",indreAreal < math.pi < ytreAreal,"\t\t(øvre estimat) - (nedre estimat) =",ytreAreal-indreAreal,"\t math.pi - gjennsomsnitt =",math.pi - 0.5*(indreAreal+ytreAreal))




def lagFigur():
    def unzip(lst):
        return zip(*lst)
    try:
        import figur
        fig = figur.figur(1500,1500)
        fig.xmin,fig.ymin,fig.xmax,fig.ymax = -1.1,-1.1,1.1,1.1
        poly = polygon(2)
        fig.polygon(*unzip(poly))
        fig.sirkel(0,0,1)
        fig.vis()
    except ImportError as e:
        print("!!!\n!!!\n!!! Pakken figur.py er ikke tilgengelig. Den kan gjøres tilgjengelig ved å legge filen figur.py i programmets arbeidskatalog\n!!!\n!!!\n\n") 


if __name__=='__main__':
    lagFigur()
    main()
