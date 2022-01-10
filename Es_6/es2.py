from abc import ABC;
from abc import abstractmethod;
import datetime;

class Viaggio(ABC) :

    @abstractmethod
    def __init__(self, nomeViaggio, dataPartenza, dataRitorno, localita, resort, prezzo, partecipanti, responsabile) :

        self.nomeViaggio = nomeViaggio;
        self.dataPartenza = dataPartenza;
        self.dataRitorno = dataRitorno;
        self.localita = localita;
        self.resort = resort;
        self.prezzo = prezzo;
        self.partecipanti = partecipanti;
        self.responsabile = responsabile;

    #----------------------------------------------------------------------------------------------

    @abstractmethod
    def stampa(self) :
        return 'INFO VIAGGIO: \nNOME ', self.nomeViaggio,'\nDATA PARTENZA ', self.dataPartenza,'\nDATA RITORNO ', self.dataRitorno,'\nLOCALITA ', self.localita,'\nRESORT ', self.resort,'\nPREZZO ', self.prezzo,'\nPARTECIPANTI ', self.partecipanti,'\nRESPONSABILE ', self.responsabile,'';

    #----------------------------------------------------------------------------------------------

    @abstractmethod
    def periodo(self) :
        periodo = self.dataRitorno - self.dataPartenza;
        return periodo;

    #----------------------------------------------------------------------------------------------

    @abstractmethod
    def guadagno(self) :
        guadagno = self.prezzo - (self.prezzo * 47) / 100;
        return guadagno;

###################################################################################################

class VacanzaInvernale(Viaggio) :

    def __init__(self, nomeViaggio, dataPartenza, dataRitorno, localita, resort, prezzo, partecipanti, responsabile, skipass, impianti) :
        self.skipass = skipass;
        self.impianti = impianti;
        super().__init__(nomeViaggio, dataPartenza, dataRitorno, localita, resort, prezzo, partecipanti, responsabile);

    #----------------------------------------------------------------------------------------------

    def stampa(self):
        details = '\nSKIPASS: ', self.skipass, '\nIMPIANTI: ', self.impianti, '';
        return super().stampa() + details;

    #----------------------------------------------------------------------------------------------

    def periodo(self):
        return super().periodo();

    #----------------------------------------------------------------------------------------------

    def guadagno(self):
        return super().guadagno();

###################################################################################################

class VacanzaEstiva(Viaggio) :

    def __init__(self, nomeViaggio, dataPartenza, dataRitorno, localita, resort, prezzo, partecipanti, responsabile, distanza, escursioniMarine) :
        self.distanza = distanza;
        self.escursioniMarine = escursioniMarine;
        super().__init__(nomeViaggio, dataPartenza, dataRitorno, localita, resort, prezzo, partecipanti, responsabile);

    #----------------------------------------------------------------------------------------------

    def stampa(self):
        details = '\nDISTANZA: ', self.distanza, '\nESCURSIONI MARINE: ', self.escursioniMarine, '';
        return super().stampa() + details;

    #----------------------------------------------------------------------------------------------

    def periodo(self):
        return super().periodo();

    #----------------------------------------------------------------------------------------------

    def guadagno(self):
        return super().guadagno();

###################################################################################################

# Main #
impianti = ["Lussari", "Montebianco", "Monterosa"];
vacanzaInvernale = VacanzaInvernale("Invernale", datetime.datetime(2021, 1, 26), datetime.datetime(2021, 1, 28), "Tarvisio", "Hotel al Cervo", 499.99, 12, "Pino", 9.99, impianti);
print("\nVACANZA INVERNALE: ", vacanzaInvernale.stampa());
print("\nPERIODO: ", vacanzaInvernale.periodo());
print("\nGUADAGNO: ", vacanzaInvernale.guadagno());

print('--------------------------------------------------------------------------------------------');

escursioniMarine = ["Abissi blu", "Barriera corallina", "Costiera amalfitana"];
vacanzaEstiva = VacanzaEstiva("Estiva", datetime.datetime(2021, 6, 22), datetime.datetime(2021, 6, 24), "Napoli", "Hotel Vesuvio", 299.99, 2, "Ciro", 200, escursioniMarine);
print("\nVACANZA ESTIVA: ", vacanzaEstiva.stampa());
print("\nPERIODO: ", vacanzaEstiva.periodo());
print("\nGUADAGNO: ", vacanzaEstiva.guadagno());


