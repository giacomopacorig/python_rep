import re
import sys

class ExamException(Exception) :
    pass;

###################################################################################################

class ExceptionControl() :

    def window_length_control(self, window_length) :

        if isinstance(window_length, list) == True :
            raise ExamException("ExamException: window_length is a list");

        elif isinstance(window_length, str) == True :
            raise ExamException("ExamException: window_length is a string");

        elif window_length == None :
            raise ExamException("ExamException: window_length is None");

        elif window_length == 0 :
            raise ExamException("ExamException: window is zero");

        elif window_length < 0 :
            raise ExamException("ExamException: window_length is negative");

        elif isinstance(window_length, float) == True :
            raise ExamException("ExamException: window_length is a float");

    #----------------------------------------------------------------------------------------------

    def list_control(self, val_list, window_length) :

        if val_list == None :
            raise ExamException("ExamException: val_list is None");

        if isinstance(val_list, list) == False :
            raise ExamException("ExamException: val_list is not a list");

        for item in val_list :
            
            if isinstance(item, int) == False and isinstance(item, float) == False :
                raise ExamException("ExamException: one or more items in val_list are not numbers");

        if len(val_list) < window_length :
            raise ExamException("ExamException: window length is grader than val_list length");

###################################################################################################

class MovingAverage() :

    def __init__(self, window_length) : # Costruttore.

        controller = ExceptionControl();
        controller.window_length_control(window_length);

        self.window_length = window_length;

    #----------------------------------------------------------------------------------------------

    def compute(self, val_list) : # Metodo per il calcolo della media mobile.

        average_list = []; # Dichiarazione della lista per la memorizzazione dei risultati delle medie mobili.
        i = 0;
        avg_i = 0;
        
        controller = ExceptionControl();
        controller.list_control(val_list, self.window_length); # Controllo delle eccezioni.

        for i in range(len(val_list) - self.window_length + 1) :
            avg_i = sum(val_list[i:i+self.window_length]) / self.window_length;
            average_list.append(avg_i);

        controller.list_control(val_list, self.window_length);

        return average_list; # Lista dei risultati delle medie mobili calcolate come valore di ritorno.

###################################################################################################

##----------##
##-- Main --##
##----------##

# result = moving_average.compute([2, 4, 8, 16]); # Chiamata al metodo compute() di MovingAverage().
# moving_average = MovingAverage(3); # Istanza di MovingAverage().
# # result = moving_average.compute([2, 4, 8, 16, 32]);
# # result = moving_average.compute([2, 4]);
# result = moving_average.compute(None); # Chiamata con lista vuota (eccezione).
# print(result); # Stampa del risultato.
# print("----------------------------------------------------------------------------------------");
# sys.exit()

