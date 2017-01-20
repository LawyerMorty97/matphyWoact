#!/usr/bin/python3

import math

class punkt2D:
    """Representerer 2D-punkter"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self,):
        return "({0}, {1})".format(self.x,self.y)
    
    def posVektor(self):
        return vektor2D(self.x,self.y)        

    def tegn(self,fig):
        fig.punkt(self.x,self.y)

        
class vektor2D:
    """Representerer 2D-punkter"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "[{0}, {1}]".format(self.x,self.y)
    
    def __add__(self,other):
        """Definerer vektoraddisjon"""
        return vektor2D(self.x+other.x,self.y+other.y)
        
    def __rmul__(self,skalar): 
        """Skalering av vektorer"""
        return vektor2D(self.x*skalar,self.y*skalar)

    def __sub__(self,other):
        """Vektorsubtraksjon"""
        return self+(-1)*other

    def prikk(self,other):
        """Skalarproduktet / (dot-product)"""
        return self.x*other.x+self.y*other.y
    
    def lengde(self):
        """ Lengden til vektoren. Bygger på Pythagoras' teorem"""
        return math.sqrt(self.x*self.x+self.y*self.y)
        
    def vinkel(self,other):
        """ Regner ut vinkelen mellom to vektorer, i grader
        u = vektor2D(1,3)
        v = vektor2D(3,1)
        vinkel = u.vinkel(v)
        """
        vinkelIRadianer = math.acos(0) # OBS: DENNE ER IKKE KORREKT!! MÅ IMPLEMENTERES PÅ EN SKIKKELIG MÅTE!
        vinkelIGrader = math.degrees(vinkelIRadianer)
        return vinkelIGrader
    
    def tegn(self,fig):
        """ Tegner vektoren på figuren `fig` med utgangpunkt i origo """
        fig.pil(0,0,self.x,self.y)
    
    def tegnFra(self,punkt,fig):
        """ Tegner vektoren på figuren `fig` med utgangpunkt i `punkt`"""
        fig.pil(punkt.x, punkt.y, punkt.x + self.x, punkt.y + self.y)




if __name__=='__main__':
    from figur import figur
    A = punkt2D(-6,-4)
    print("A = {0}".format(A))
    print("posisjonsvektor = ",A.posVektor())
    
    b = vektor2D(5,6)
    c = vektor2D(5,-3)
 
    d = vektor2D(-43.3,10)
    
    print('vektoren b+3*c-d = ',b+3*c-d)
    
    print('lengden til b = ',b.lengde())
    
    print('skalarprodukt mellom b og d = ',b.prikk(d)) 


    #BRUK AV FIGURER
    fig = figur(500,500)
    fig.settRekkevidde(-10,10,-10,10)
    b.tegnFra(A,fig)
    fig.linje(0,0,100,100)
    fig.punkt(300,300)

    fig.vis()
