import re
import sys

class ExamException(Exception) :
    
    def __init__(self, message) :
        super().__init__(message);

###################################################################################################

class MovingAverage() :

    def __init__(self, window_length) : # Costruttore.

        self.window_length = window_length;

    #----------------------------------------------------------------------------------------------

    def compute(self, val_list) : # Metodo per il calcolo della media mobile.

        message = "";
        average_list = []; # Dichiarazione della lista per la memorizzazione dei risultati delle medie mobili.
        counter = 0; # Variabile contatore.
        i = 0;
        array_counter = 0; # Variabile contatore per l'array.
        result = 0; # Variabile per il risultato.
        temp = self.window_length
        #it_is = re.match(num_format, self.window_length)

        # if it_is: print("True")
        # else: print("False")
        for item in val_list :
            
            if isinstance(item, int) == False :
                raise ExamException(message);
                

        if isinstance(temp, int) == False :
            raise ExamException(message);
        elif self.window_length == None :
            raise ExamException(message);
        elif self.window_length <= 0 :
            raise ExamException(message);
        elif val_list == None :
            raise ExamException(message);

        while array_counter <= len(val_list) : # Ciclo della lista di valori.
            counter = 0;
            i += 1;
            if (i == len(val_list)) :
                break;

            while counter <= self.window_length : # Ciclo per il calcolo della media sulla base della lunghezza della finestra.
                result = (val_list[i - 1] + val_list[i]) / (self.window_length); # Calcolo della media.
                counter += 1; # Incremento del contatore.

                #average_list.append(result); # Memorizzazione nella lista del risultato della media calcolata.

            average_list.append(result);        
            array_counter += 1; # Incremento del contatore dell'array.

        return average_list; # Lista dei risultati delle medie mobili calcolate come valore di ritorno.

###################################################################################################

##----------##
##-- Main --##
##----------##
moving_average = MovingAverage(2); # Istanza di MovingAverage().

try :
    #result = moving_average.compute([2, 4, 8, 16]); # Chiamata al metodo compute() di MovingAverage().
    result = moving_average.compute([2, 4, 8, 16, 32]);
    #result = moving_average.compute(None); # Chiamata con lista vuota (eccezione).
    print(result); # Stampa del risultato.
except ExamException :
    print("ERRORE: eccezione di tipo ExamException trovata");
    #sys.exit()
except ValueError :
    raise ExamException("");
except TypeError :
    raise ExamException("");

