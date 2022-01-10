import random;

class Automa() : 
    
    def __init__(self, biancheria, calzini, maglia, pantaloni, calzatura) :
        
        self.biancheria = biancheria;
        self.calzini = calzini;
        self.maglia = maglia;
        self.pantaloni = pantaloni;
        self.calzatura = calzatura;

    def indossa_biancheria(self) :

        n = random.randint(0, 1);

        if n == 1 :
            self.biancheria = True;

        return n;

    def indossa_calzini(self) :

        n = random.randint(0, 1);

        if n == 1 :
            self.calzini = True;

        return n;

    def indossa_maglia(self) :

        n = random.randint(0, 1);

        if n == 1 :
            self.maglia = True;

        return n;

    def indossa_pantaloni(self) :

        n = random.randint(0, 1);

        if n == 1 :
            self.pantaloni = True;

        return n;

    def indossa_calzatura(self) :

        n = random.randint(0, 1);

        if n == 1 :
            self.calzatura = True;

        return n;


## Main ##

automa = Automa(False, False, False, False, False);
capi_vestiario = ["biancheria", "calzini", "maglia", "pantaloni", "calzatura"];
ordine = ["biancheria", "calzini", "maglia", "pantaloni", "calzatura"];
vestito = False;
capo = "";
i = 0;

def esegui(capo) :

    n = 0;

    if capo == "biancheria" :
        n = automa.indossa_biancheria();
    elif capo == "calzini" :
        n = automa.indossa_calzini();
    elif capo == "maglia" :
        n = automa.indossa_maglia();
    elif capo == "pantaloni" :
        n = automa.indossa_pantaloni();
    elif capo == "calzatura" :
        n = automa.indossa_calzatura();

    return n;

while vestito == False :

    while capo != ordine[i] :

        capo = random.choice(capi_vestiario);

    i = i + 1;

    n = esegui(capo);

    if n == 1: 
        print(capo + " : OPERAZIONE COMPLETATA\n");
    else :
        print(capo + " : ERRORE FATALE\n");
        break;

    if i >= 5 :
        vestito = True;

if vestito == True :
    print("Automa vestito correttamente\n");
elif vestito == False :
    print("Errore nell'automa\n");
    


