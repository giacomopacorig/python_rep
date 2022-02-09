import re
import sys

class ExamException(Exception) :
    pass;

###################################################################################################

class ExceptionControl() :

    def ratio_control(self, ratio) :

        if isinstance(ratio, list) == True :
            raise ExamException("ExamException: ratio is a list");

        elif isinstance(ratio, str) == True :
            raise ExamException("ExamException: ratio is a string");

        elif isinstance(ratio, float) == True :
            raise ExamException("ExamException: ratio is a float");

        elif ratio == None :
            raise ExamException("ExamException: ratio is None");

        elif ratio == 0 :
            raise ExamException("ExamException: ratio is zero");

        elif ratio < 0 :
            raise ExamException("ExamException: ratio is negative");

    #----------------------------------------------------------------------------------------------

    def list_control(self, val_list, window_length) :

        if val_list == None :
            raise ExamException("ExamException: ratio is None");

        if isinstance(val_list, list) == False :
            raise ExamException("ExamException: ratio is not a list");

        for item in val_list :
            
            if isinstance(item, int) == False and isinstance(item, float) == False :
                raise ExamException("ExamException: one or more items in val_list are not numbers");

        if len(val_list) < window_length :
            raise ExamException("ExamException: window length is grader than val_list length");

        if len(val_list) < 2 :
            raise ExamException("ExamException: val_list length is minor than 2")

###################################################################################################

class Diff() : 

    def __init__(self, ratio = 1) : # Costruttore.

        if isinstance(ratio, list) == True :
            raise ExamException("ExamException: ratio is a list");

        elif isinstance(ratio, str) == True :
            raise ExamException("ExamException: ratio is a string");

        elif ratio == None :
            raise ExamException("ExamException: ratio is None");

        elif ratio == 0 :
            raise ExamException("ExamException: ratio is zero");

        elif ratio < 0 :
            raise ExamException("ExamException: ratio is negative");

        self.ratio = ratio;

    def compute(self, val_list) :
            
        diff_list = []; # Dichiarazione della lista per la memorizzazione dei risultati delle medie mobili.
        i = 0;
        diff_i = 0;
            
        if self.ratio == None :
            self.ratio = 1;
            
        controller = ExceptionControl();
        controller.list_control(val_list, self.ratio); # Controllo delle eccezioni.

        for i in range(len(val_list) - 1) :
            diff_i = val_list[i + 1] - val_list[i];
            diff_list.append(diff_i);

        for i in range(len(diff_list)) :
            diff_list[i] = diff_list[i]  / self.ratio;

        controller.list_control(val_list, self.ratio);

        return diff_list; # Lista dei risultati delle medie mobili calcolate come valore di ritorno.

###################################################################################################

##----------##
##-- Main --##
##----------##

diff = Diff(2);
#result = diff.compute([2, 4, 8, 16, 32, 64]);
result = diff.compute("ciao")
print(result);
print('-----------------------------------------');