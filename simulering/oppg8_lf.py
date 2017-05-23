#!/usr/bin/python3

from animasjon import animasjon
from figur import figur
from geometri3D import vektor3D as vec

G = 2.959122e-4

xSol = vec(0,0,0)
vSol = vec(0,0,0)
mSol = 1

xJord = vec(-7.3423e-1,-6.8292e-1,-1.1499e-4)
vJord = vec(1.1456e-2,-1.2634e-2,-5.7432e-8)
mJord = 3e-6*mSol

xMåne = vec(-7.3611e-1,-6.8121e-1,-1.6369e-4)
vMåne = vec(1.033e-2,-1.3049e-2,-5.0483e-5)
mMåne = 3.7e-8*mSol

xJupiter = vec(-5.1236,-1.8557,0.1223)
vJupiter = vec(2.4814e-3,-6.7369e-3,-2.7515e-5)
mJupiter =  9.546e-4*mSol #Her hadde det sneket seg inn et galt tall i oppgaveteksten.

def oppgaveA():
    def solGravitasjon(posisjon):
        dist = posisjon.lengde()
        return -G/dist**3*posisjon
    return solGravitasjon

solGravitasjon = oppgaveA()

def oppgaveB():
    def gravitasjon(posA,posB,masseB):
        relativPosisjon = posA-posB
        dist = relativPosisjon.lengde()
        return -G*masseB/dist**3*relativPosisjon
    return gravitasjon

gravitasjon = oppgaveB()

def oppgaveC():
    print()
    print("OPPGAVE C")
    print("Solens tiltrekning på jorda gir en akselerasjon på",solGravitasjon(xJord),"AU/døgn**2")
    print("Jordens tiltrekning på månen gir en akselerasjon på",gravitasjon(xMåne,xJord,mJord),"AU/døgn**2")
    print("Solens tiltrekning på månen gir en akselerasjon på",solGravitasjon(xMåne),"AU/døgn**2")
    print("Den samlede virkningen av Solen og Jorden gir Månen en akselerasjon på",solGravitasjon(xMåne)+gravitasjon(xMåne,xJord,mJord),"AU/døgn**2")
    print()


#
# Eulers metode
###########################
def eulerStep(x,v,a,h):
    nyX = x+h*v + 0.5*h**2*a
    nyV = v+h*a
    return nyX,nyV


#
# Størmers metode
######################
def stormerStep(xNow,xPrev,a,h):
    xNext = 2*xNow-xPrev+h**2*a
    return xNext,xNow

# Simulering av første steg i størmers metode.
def stormerStart(x,v,h):
    return x+0.5*h*v,x-0.5*h*v 




def oppgaveD():

    def simulation(h):
        x = xJord
        v = vJord

        while True:
            yield [x]
            x,v = eulerStep(x,v,solGravitasjon(x),h)

    def antallDøgnIÅr():
        h = 1.0/24/4 # 1 steg =1/4 time
        signChangeCount = -1
        timeCount = 0
        signFlag = 1 if xJord[0] > 0 else -1
        N = 10
        
        for x in simulation(h):
            if (x[0][0]*signFlag < 0):
                signChangeCount+=1
                signFlag*=-1

            if (0 <= signChangeCount):
                timeCount+=h

            if (signChangeCount >= 2*N):
                break
        
        return timeCount/N

    print("Vi anslår at det er",antallDøgnIÅr(),"døgn i ett år")
    return simulation


def oppgaveE():
    def simulation(h):
        xJ = xJord
        vJ = vJord
        xM = xMåne
        vM = vMåne

        while True:
            yield (xJ,xM)
            aJ = solGravitasjon(xJ)
            aM = gravitasjon(xM,xJ,mJord)
            xJ,vJ = eulerStep(xJ,vJ,aJ,h)
            xM,vM = eulerStep(xM,vM,aM,h)

    def antallDøgnIMåned():
        h = 1.0/24/4 # 1 steg =1/4 time
        signChangeCount = -1
        timeCount = 0
        signFlag = 1 if xJord.prikk(xMåne-xJord) > 0 else -1
        N = 10
        
        for xJ,xM in simulation(h):
            if (xJ.prikk(xM-xJ)*signFlag < 0): # Kontrollerer når skalarproduktet mellom vektoren Sol-Jord og vektoren Jord-Måne endrer fortegn.
                signChangeCount+=1
                signFlag*=-1

            if (0 <= signChangeCount):
                timeCount+=h

            if (signChangeCount >= 2*N):
                break

            if (timeCount > N*50):
                return -1
        
        return timeCount/N

    #print("Vi anslår at det er",antallDøgnIMåned(),"døgn i en måne-måned")
    return simulation


def oppgaveF():
    def simulation(h):
        xJ = xJord
        vJ = vJord
        xM = xMåne
        vM = vMåne

        while True:
            yield (xJ,xM)
            aJ = solGravitasjon(xJ)
            aM = gravitasjon(xM,xJ,mJord) + solGravitasjon(xM)
            xJ,vJ = eulerStep(xJ,vJ,aJ,h)
            xM,vM = eulerStep(xM,vM,aM,h)

    def antallDøgnIMåned():
        h = 1.0/24 # 1 steg =1/4 time
        signChangeCount = -1
        timeCount = 0
        signFlag = 1 if xJord.prikk(xMåne-xJord) > 0 else -1
        N = 10
        
        for xJ,xM in simulation(h):
            if (xJ.prikk(xM-xJ)*signFlag < 0): # Kontrollerer når skalarproduktet mellom vektoren Sol-Jord og vektoren Jord-Måne endrer fortegn.
                signChangeCount+=1
                signFlag*=-1

            if (0 <= signChangeCount):
                timeCount+=h

            if (signChangeCount >= 2*N):
                break

            if (timeCount > N*50):
                return -1
        
        return timeCount/N

    #print("Vi anslår at det er",antallDøgnIMåned(),"døgn i en måne-måned")
    return simulation

def tegnOppgF(N):
    # Statisk figur: Oppgave F
    simuleringF = oppgaveF()
    simulering = [p for p in takeFromGenerator(simuleringF(1),N)]
    xDataJ = (p[0][0] for p in simulering)
    yDataJ = (p[0][1] for p in simulering)
    xDataM = (p[1][0] for p in simulering)
    yDataM = (p[1][1] for p in simulering)

    fig = figur()
    fig.xmin,fig.ymin,fig.xmax,fig.ymax = -6,-6,6,6
    fig.kurve(xDataJ,yDataJ)
    fig.kurve(xDataM,yDataM)
    fig.vis()


def oppgaveG():

    def simulation(h):
        xJn,xJp = stormerStart(xJord,vJord,h)
        xMn,xMp = stormerStart(xMåne,vMåne,h)
        xJUPn,xJUPp = stormerStart(xJupiter,vJupiter,h)

        while True:
            yield (xJn,xMn,xJUPn)
            aJ = solGravitasjon(xJn) + gravitasjon(xJn,xMn,mMåne) + gravitasjon(xJn,xJUPn,mJupiter)
            aM = gravitasjon(xMn,xJn,mJord) + solGravitasjon(xMn) + gravitasjon(xMn,xJUPn,mJupiter)
            aJUP = solGravitasjon(xJUPn)

            xJn,xJp = stormerStep(xJn,xJp,aJ,h)
            xMn,xMp = stormerStep(xMn,xMp,aM,h)
            xJUPn,xJUPp = stormerStep(xJUPn,xJUPp,aJUP,h)

    def antallDøgnIÅr():
        h = 1.0/24/4 # 1 steg =1/4 time
        signChangeCount = -1
        timeCount = 0
        signFlag = 1 if xJord[0] > 0 else -1
        N = 3
        
        for x in simulation(h):
            if (x[0][0]*signFlag < 0):
                signChangeCount+=1
                signFlag*=-1

            if (0 <= signChangeCount):
                timeCount+=h

            if (signChangeCount >= 2*N):
                break
        
        return timeCount/N

    print("Vi anslår at det er",antallDøgnIÅr(),"døgn i ett år (Med Størmers metode)")

    def antallDøgnIMåned():
        h = 1.0/24 # 1 steg =0.5 minutt
        signChangeCount = -1
        timeCount = 0
        signFlag = 1 if xJord.prikk(xMåne-xJord) > 0 else -1
        N = 3
        
        for xJ,xM,_ in simulation(h):
            if (xJ.prikk(xM-xJ)*signFlag < 0): # Kontrollerer når skalarproduktet mellom vektoren Sol-Jord og vektoren Jord-Måne endrer fortegn.
                signChangeCount+=1
                signFlag*=-1

            if (0 <= signChangeCount):
                timeCount+=h

            if (signChangeCount >= 2*N):
                break

            if (timeCount > N*1000):
                return -1
        
        return timeCount/N

    print("Vi anslår at det er",antallDøgnIMåned(),"døgn i en måne-måned")
    return simulation


def tegnOppgG(N):
    # Statisk figur: Oppgave G
    simuleringG = oppgaveG()
    simulering = [p for p in takeFromGenerator(simuleringG(1),N)]
    xDataJ = (p[0][0] for p in simulering)
    yDataJ = (p[0][1] for p in simulering)
    xDataM = (p[1][0] for p in simulering)
    yDataM = (p[1][1] for p in simulering)
    xDataJUP = (p[2][0] for p in simulering)
    yDataJUP = (p[2][1] for p in simulering)

    fig = figur()
    fig.xmin,fig.ymin,fig.xmax,fig.ymax = -7,-7,7,7
    fig.kurve(xDataJ,yDataJ)
    fig.kurve(xDataM,yDataM)
    fig.kurve(xDataJUP,yDataJUP)
    fig.vis()


def takeFromGenerator(generator,N):
    for x,_ in zip(generator,range(N)):
        yield x



def ideerTilMerAvansertLøsning():

    class planet():
        def __init__(self,pos,vel,mass):
            self.pos = pos
            self.vel = vel
            self.acc = None
            self.mass = mass
            self.listOfPlanets = []

        def addPlanet(self,other):
            self.listOfPlanets.append(other);

        def gravitationalAccelerationOn(self,other):
            disp = self.pos-other.pos
            dist = disp.lengde()
            return G*self.mass/dist**3*disp

        def updateState(self,step):
            self.pos += step*self.vel + 0.5*step**2*self.acc
            self.vel += step*self.acc

        def updateAcceleration(self):
            self.acc = sum((planet.gravitationalAccelerationOn(self) for planet in self.listOfPlanets),vec(0,0,0))

        def step(self,step):
            self.updateAcceleration()
            self.updateState(step)


    class planetII():
        def __init__(self,posNow,posPrev,mass):
            self.pos = posNow
            self.posPrev = posPrev
            self.acc = None
            self.mass = mass
            self.listOfPlanets = []

        def addPlanet(self,other):
            self.listOfPlanets.append(other);

        def gravitationalAccelerationOn(self,other):
            disp = self.pos-other.pos
            dist = disp.lengde()
            return G*self.mass/dist**3*disp

        def updateState(self,step):
            self.pos,self.posPrev = 2*self.pos-self.posPrev+step**2*self.acc, self.pos

        def updateAcceleration(self):
            self.acc = sum((planet.gravitationalAccelerationOn(self) for planet in self.listOfPlanets),vec(0,0,0))

        def step(self,step):
            self.updateAcceleration()
            self.updateState(step)


    def solsystemSimulator(h):
        sol = planet(xSol,vSol,mSol)
        jord = planetII(xJord,xJord-h*vJord,mJord)
        måne = planet(xMåne,vMåne,mMåne)
        jupiter = planet(xJupiter,vJupiter,mJupiter)

        planeter = [sol,jupiter,jord,måne]
        

        for p in planeter:
            for q in planeter:
                if (p != q):
                    p.addPlanet(q)

        while True:
            yield tuple(p.pos for p in planeter)
            for p in planeter:
                p.step(h)


    animasjon(solsystemSimulator(1),-6,-6,6,6)


        
        
        




if __name__=='__main__':
    #oppgaveC()
    #simuleringD = oppgaveD()
    #simuleringE = oppgaveE()
    #simuleringF = oppgaveF()
    #simuleringG = oppgaveG()

    #tegnOppgF(10000)
    #tegnOppgG(10000)

    # Animasjon
    #animasjon(oppgaveG()(1))
    ideerTilMerAvansertLøsning()
