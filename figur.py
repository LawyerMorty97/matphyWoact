#!/usr/bin/python3

import tkinter as tk
import math

class figur:
    """Klasse for å lage enkle figurer

    Eksempel på bruk:

        fig = figur(1200,800) # vindu med størrelse 1200 x 800

        fig.settRekkevidde(-1.5,1.5,-1.5,1.5)
        fig.inverterYretning()

        fig.rektangel(0.5,0.5,0.9,0.7)
        fig.punkt(.4,.5)

        fig.linje(-1,0,1,0)

        xs = ( math.sin(0.01*i) for i in range(629) )
        ys = ( math.cos(0.01*i) for i in range(629) )

        fig.polygon(xs,ys)

        fig.sirkel(0.5,0.5,0.5)

        fig.punkt(0,0)

        fig.vis()

    """

    def __init__(self,bredde=1000,høyde=600):
        self.bredde= bredde
        self.høyde = høyde
        self.rot = tk.Tk()

        self.lerret = tk.Canvas(self.rot, width = self.bredde, height = self.høyde)
        self.lerret.pack()
        
        self.xmin, self.xmax = 0,bredde
        self.ymin, self.ymax = 0,høyde
        


    def _remap(t,a,b,A,B):
        """private helper function. Maps the interval [a,b] onto the interval [A,B]"""
        return A + (t-a)/(b-a)*(B-A)  

    def transformasjon(self,x,y):
        return figur._remap(x,self.xmin,self.xmax,0,self.bredde), figur._remap(y,self.ymin,self.ymax,self.høyde,0)
    


    def linje(self,x0,y0,x1,y1,**kwargs):
        """ Tegner en linje fra (x0,y0) til (x1,y1)"""

        x0,y0 = self.transformasjon(x0,y0)
        x1,y1 = self.transformasjon(x1,y1)
        self.lerret.create_line(x0,y0,x1,y1,**kwargs)

    def pil(self,x0,y0,x1,y1):
        """ Tegner en linje fra (x0,y0) til (x1,y1)"""

        x0,y0 = self.transformasjon(x0,y0)
        x1,y1 = self.transformasjon(x1,y1)

        lengde = math.sqrt((x1-x0)**2 + (y1-y0)**2)
        dim = 5
        dx = (x1-x0)/lengde*dim
        dy = (y1-y0)/lengde*dim
        
        self.lerret.create_line(x0,y0,x1,y1)
        self.lerret.create_line(x1,y1,x1-(3*dx-dy),y1-(dx+3*dy))
        self.lerret.create_line(x1,y1,x1-(3*dx+dy),y1-(-dx+3*dy))

    def punkt(self,x,y):
        """Tegner en prikk i punktet (x,y)"""
        x,y = self.transformasjon(x,y)
        self.lerret.create_oval(x-2,y-2,x+2,y+2,fill="black")

    def punkter(self,xs,ys):
        """Tegner prikker i punktene (xs[0],ys[0]), (xs[1],ys[1]) ,...."""
        for x,y in zip(xs,ys):
            self.punkt(x,y);

    # AVHENGER AV linje og punkt
    def polygon(self,xs,ys):
        """Tegner polygonet gjennom gjennom punktene (xs[0],ys[0]), (xs[1],ys[1]) ,...."""
        xs,ys = iter(xs),iter(ys)
        xp,yp= next(xs),next(ys)

        for x,y in zip(xs,ys):
            self.linje(xp,yp,x,y)
            xp,yp = x,y

    # AVHENGER AV polygon
    def rektangel(self,x0,y0,x1,y1):
        """Tegner rektangel der (x0,y0) og (x1,y1) er diagonalt motsatte hjørner"""
        self.polygon((x for x in (x0,x0,x1,x1,x0)),(y for y in (y0,y1,y1,y0,y0)))

    # Avhenger av polygon
    def sirkel(self, x0,y0, r):
        """Tegner sirkel med sentrum i x0,y0 og radius r"""
        self.polygon(( x0+r*math.cos(0.01*i) for i in range(629)),(y0+r*math.sin(0.01*i) for i in range(629)))

    def settRekkevidde(self,xmin,xmax,ymin,ymax):
        """
        Setter grensene for x- og y- verdier i figuren

        xmin = x-verdi til venstre i vinduet
        xmax = x-verdi til høyre i vinduet
        ymin = y-verdi på toppen av vinduet
        ymax = y-verdi nederst i vinduet
        """
        self.xmin  = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def inverterYretning(self):
        self.ymin,self.ymax = self.ymax,self.ymin

    def vis(self):
        self.rot.mainloop();


#
# Uformell enhetstesting
#
if __name__=="__main__":
    fig = figur()

    fig.settRekkevidde(-1.5,1.5,-1.5,1.5)

    fig.rektangel(0.5,0.5,0.9,0.7)
    fig.punkt(.4,.5)

    fig.pil(-1,0,1,1)
    fig.pil(0,0,.5,.5)
    fig.pil(0,0,.5,-.5)

    xs = ( math.sin(0.01*i) for i in range(629) ) # GENERATOR COMPREHENSION SYNTAKS
    ys = ( math.cos(0.01*i) for i in range(629) ) # GENERATOR COMPREHENSION SYNTAKS

    fig.polygon(xs,ys)

    fig.sirkel(0.5,0.5,0.5)

    fig.punkt(0,0)

    fig.vis()



