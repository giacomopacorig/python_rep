from abc import ABC;
from abc import abstractmethod;

class Figura(ABC) :

    @abstractmethod
    def perimetro() :
        pass;

    #----------------------------------------------------------------------------------------------

    @abstractmethod
    def area() :
        pass;

###################################################################################################

class Triangolo(Figura) :

    def __init__(self, b, l, h) :
        
        self.b = b;
        self.l = l;
        self.h = h;

    #----------------------------------------------------------------------------------------------

    def perimetro(self):
        
        perimetro = self.b + self.l + self.h;

        return perimetro;

    #----------------------------------------------------------------------------------------------

    def area(self):
        
        area = (self.b * self.h) / 2;

        return area;

###################################################################################################

class Circonferenza(Figura) :

    def __init__(self, r) :
        
        self.r = r;

    #----------------------------------------------------------------------------------------------

    def perimetro(self) :
        
        perimetro = self.r * 2 * 3.14;

        return perimetro;

    #----------------------------------------------------------------------------------------------

    def area(self) :

        area = (self.r * self.r) * 3.14;

        return area;

###################################################################################################

# Main #

triangolo = Triangolo(3, 4, 4);
print('\nPerimetro del triangolo ', triangolo.perimetro(),'');
print('\nArea del triangolo ', triangolo.area(),'');

circonferenza = Circonferenza(6);
print('\nPerimetro della circonferenza ', circonferenza.perimetro(),'');
print('\nArea della circonferenza ', circonferenza.area(),'');
