# Implementare una classe Automobile che presenta i seguenti attributi: casa automo, modello,
# numero posti, targa.
# Inoltre, la presente classe deve comprendere i seguenti metodi:
#  init , metodo per inizializzare una istanza della classe;
#  str , metodo che stampa tutte le informazioni associate ad una specifica istanza (aka
# oggetto) della classe Automobile;
#  parla, metodo che stampa a schermo ”Broom Broom”;
#  confronta, metodo che, data in ingresso un’altra istanza di Automobile, determina se i
# due oggetti hanno le stesse informazioni (eccetto per la targa che `e univoca!).

class Automobile() :

    def __init__(self, casaAuto, modello, numeroPosti, targa) :
        
        self.casaAuto = casaAuto;
        self.modello = modello;
        self.numeroPosti = numeroPosti;
        self.targa = targa;
    
    #----------------------------------------------------------------------------------------------

    def str(self) :
        
        return print('\nDettagli veicolo: \nCASA AUTOMOBILISTICA ', self.casaAuto,'\nMODELLO ', self.modello,'\nNUMERO POSTI ', self.numeroPosti,'\nTARGA ', self.targa);

    #----------------------------------------------------------------------------------------------

    def parla(self) :
        
        return print('\nBroom Broom');
    
    #----------------------------------------------------------------------------------------------

    def contronta(self, auto) :

        # auto = __init__("Audi", "R8", "2", "AA111AA");
        # auto = Automobile("Audi", "R8", "2", "AA222AA");

        if self.casaAuto == auto.casaAuto :
            if self.modello == auto.modello :
                if self.numeroPosti == auto.numeroPosti :

                    return print('\nI due veicoli sono equivalenti');
                
        else :

            return print('\nI due veicoli non sono equivalenti');

###################################################################################################

class Transformer(Automobile) :

    def __init__(self, nome, generazione, grado, reparto) :
        
        self.nome = nome;
        self.generazione = generazione;
        self.grado = grado;
        self.reparto = reparto;

        Automobile.__init__(self, "Chevrolet", "Camaro", "4", "CC333CC");

    def scheda_militare(self) :
        
        return print('\nDati militari: \nNOME: ', self.nome,'\nGENERAZIONE: ', self.generazione,'\nGRADO: ', self.grado,'\nREPARTO: ', self.reparto,'');

# Main

auto = Automobile("Audi", "A4", "4", "AA111AA");
auto2 = Automobile("BMW", "M5", "4", "BB222BB");
transformer = Transformer("Gino", "2", "Soldato semplice", "Fanteria");
print(auto.str());
auto.parla();
auto.contronta(auto2);
transformer.scheda_militare();




        