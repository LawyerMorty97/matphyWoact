#!/usr/bin/python3
#
# Bruk av skalarprodukt til å studere temperaturmålinger
#

import figur
import math


DAG = 0 # første søyle i Osloseries.txt nummerere dagene
AVG_TEMP = 1 # andre søyle i OsloSeries.txt inneholder gjennomsnittstemp.
MIN_TEMP = 2 # tredje søyle inneholder min-temp.
MAX_TEMP = 3 # fjerde søyle inneholder maks-temp.


def dot(u,v):
    return sum(ui*vi for ui,vi in zip(u,v))

def proj(u,v):
    alpha = dot(u,v)/dot(u,u)
    return [alpha*ui for ui in u]

def rows(fileName):
    with open(fileName,"r") as file:
        for line in file:
            try :
                yield tuple(float(x) for x in line.split())
            except ValueError:
                pass

def loadFile(fileName,column):
    for row in rows(fileName):
        yield row[column]



def sinGenerator(xData,periode):
    a = 2*math.pi/periode
    for x in xData:
        yield math.sin(a*x)

def sinVektor(xData,periode):
    return list(sinGenerator(xData,periode))

def plottPolygon(xs,ys):
    fig = figur.figur(1800,500)
    fig.xmin = min(xs)
    fig.xmax = max(xs)
    fig.ymin = min(ys)
    fig.ymax = max(ys)
    fig.linje(fig.xmin,0,fig.xmax,0)
    fig.polygon(xs,ys)
    fig.vis()

def plottPunkter(xs,ys):
    fig = figur.figur(1800,500)
    fig.xmin = min(xs)
    fig.xmax = max(xs)
    fig.ymin = min(ys)
    fig.ymax = max(ys)
    fig.linje(fig.xmin,0,fig.xmax,0)
    fig.punkter(xs,ys)
    fig.vis()



dager = list(loadFile("OsloSeries.txt",DAG))
temperatur = list(loadFile("OsloSeries.txt",MAX_TEMP))
N = len(temperatur)
middeltemp= sum(temperatur)/N
avvikFraMiddel = list( t-middeltemp for t in temperatur )

plottPolygon(dager,avvikFraMiddel)


A = 350
B = 400
PERIODER = range(A,B)
skalarprodukter = list( abs(dot(avvikFraMiddel, sinVektor(dager,i)) ) for i in  PERIODER )

MAKS = max(zip(skalarprodukter,PERIODER))
print(MAKS)

plottPunkter(PERIODER,skalarprodukter)


plottPunkter(dager+dager, proj(sinVektor(dager,365),avvikFraMiddel) + avvikFraMiddel )
