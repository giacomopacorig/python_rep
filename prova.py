class ExamException(Exception) :
    
    def __init__(self, message) :
        super().__init__(message);

###################################################################################################

class MovingAverage() :

    def __init__(self, window_length) : # Costruttore.

        self.window_length = window_length;

    #----------------------------------------------------------------------------------------------

    def compute(self, val_list) : # Metodo per il calcolo della media mobile.

        average_list = []; # Dichiarazione della lista per la memorizzazione dei risultati delle medie mobili.
        counter = 0; # Variabile contatore.
        array_counter = 0; # Variabile contatore per l'array.
        result = 0; # Variabile per il risultato.

        while array_counter <= len(val_list) : # Ciclo della lista di valori.

            while counter <= self.window_length : # Ciclo per il calcolo della media sulla base della lunghezza della finestra.

                result = (val_list[counter] + val_list[counter + 1]) / (self.window_length); # Calcolo della media.
                counter += 1; # Incremento del contatore.

                average_list.append(result); # Memorizzazione nella lista del risultato della media calcolata.
                        
            array_counter += 1; # Incremento del contatore dell'array.

        return average_list; # Lista dei risultati delle medie mobili calcolate come valore di ritorno.

###################################################################################################

##----------##
##-- Main --##
##----------##
moving_average = MovingAverage(2); # Istanza di MovingAverage().

result = moving_average.compute([2, 4, 8, 16]); # Chiamata al metodo compute() di MovingAverage().
#result = moving_average.compute(None); # Chiamata con lista vuota (eccezione).
print(result); # Stampa del risultato.

print("ERRORE: eccezione di tipo ExamException trovata");
#sys.exit()


    