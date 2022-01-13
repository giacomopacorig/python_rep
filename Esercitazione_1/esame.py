import re
import sys

class ExamException(Exception) :
    pass;

###################################################################################################

class NonIntegerValue(ExamException) :
    pass;

###################################################################################################

class NoneValue(ExamException) :
    pass;

###################################################################################################

class EmptyList(ExamException) :
    pass;

###################################################################################################

class NegativeValue(ExamException) :
    pass

###################################################################################################

class InvalidList(ExamException) :
    pass

###################################################################################################

class FloatValue(ExamException) :
    pass;

###################################################################################################

class WindowList(ExamException) :
    pass;

###################################################################################################

class ZeroValue(ExamException) :
    pass;

###################################################################################################

class ExceptionControl() :

    def control(self, window, val_list) :

        if isinstance(window, list) == True :
            raise WindowList;

        elif isinstance(window, str) == True :
            raise NonIntegerValue;

        elif window == None :
            raise NoneValue;

        elif window == 0 :
            raise ZeroValue;

        elif window < 0 :
            raise NegativeValue;

        elif val_list == None :
            raise EmptyList;

        elif isinstance(window, float) == True :
            raise FloatValue;

        for item in val_list :
            
            if isinstance(item, int) == False :
                raise EmptyList;

###################################################################################################

class MovingAverage() :

    def __init__(self, window_length) : # Costruttore.

        self.window_length = window_length;

    #----------------------------------------------------------------------------------------------

    def compute(self, val_list) : # Metodo per il calcolo della media mobile.

        average_list = []; # Dichiarazione della lista per la memorizzazione dei risultati delle medie mobili.
        counter = 0; # Variabile contatore.
        i = 0;
        array_counter = 0; # Variabile contatore per l'array.
        result = 0; # Variabile per il risultato.
        exceptionControl = ExceptionControl();
        
        exceptionControl.control(self.window_length, val_list);

        while array_counter <= len(val_list) : # Ciclo della lista di valori.

            counter = 0;
            i += 1;

            if (i == len(val_list)) :
                break;

            while counter <= self.window_length : # Ciclo per il calcolo della media sulla base della lunghezza della finestra.
                result = (val_list[i - 1] + val_list[i]) / (self.window_length); # Calcolo della media.
                counter += 1; # Incremento del contatore.

            average_list.append(result); # Memorizzazione nella lista del risultato della media calcolata.         
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
    #sys.exit()

except NonIntegerValue :
    print("ExamException: Valore della finestra non numerico");

except NoneValue :
    print("ExamException: Valore della finestra None");

except InvalidList :
    print("ExamException: valori della lista non validi")

except EmptyList :
    print("ExamException: Lista dei valori vuota");

except NegativeValue :
    print("ExamException: valore della finestra negativo");

except FloatValue :
    print("ExamException: Valore della finestra decimale");

except WindowList :
    print("ExamException: la finestra è una lista");

except ZeroValue :
    print("ExamException: Valore della finestra uguale a 0")

except ExamException :
    print("ExamException: eccezione di tipo ExamException trovata");

except Exception :
    raise ExamException;

