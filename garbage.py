list_avg_monthly_difference = []
    partial_list = []
    result_list = []
    difference = last_year - first_year
    year = first_year
    month = 1
    cnt = year - ((difference + 11))
    

    # for i in range(difference + 1) :

    #     for j in range(12) :
    #         partial_list.append(time_series[year - cnt][1])
    #         cnt -= 1

    #     list_avg_monthly_difference.append(partial_list)
    #     partial_list = []
    #     print("YEAR: ", year)
    #     print(list_avg_monthly_difference)
    #     print("---------------------------------------------------------------------------")

    #     year += 1
    #     cnt = year - ((difference + 11))
    #     cnt -= 12

    # print(list_avg_monthly_difference)

    # cnt = 0



        # for list in data_list :

        #     if list_index == 0 :
        #         break

        #     sum_element += int(list[list_index][month_index]) - int(list[list_index - 1][month_index])
        #     #sum_element += list[list_index] - list[list_index - 1]
        #     print(list[list_index])

# for list in data_list : # TODO: algoritmo per il calcolo della differenza tra annate

    #     print("MESE: ", month_index)
    #     print("LISTA: ", list_index)
    #     print(result_list)
    #     print("--------------------------------------------------------------")

    #     if month_index == 12 :
    #         break

    #     sum_element += int(data_list[list_index][month_index]) - int(data_list[list_index - 1][month_index])

    #     # for list in data_list :

    #     #     if list_index == 0 :
    #     #         break

    #     #     sum_element += int(list[list_index][month_index]) - int(list[list_index - 1][month_index])
    #     #     #sum_element += list[list_index] - list[list_index - 1]
    #     #     print(list[list_index])


    #     list_index -= 1

    #     if list_index == 0 :
    #         sum_element = sum_element / difference
    #         month_index += 1
    #         list_index = len(data_list) - 1

    #         result_list.append(sum_element)

    class CSVTimeSeriesFile(CSVFile) : # TODO : Rivedere eccezioni file.

#     def __init__(self, name) : # Costruttore.
#         self.name = name
#         self.can_read = True

#         # if name == None :
#         #     raise ExamException("ExamException: file name is None!")
#         # elif name == "" :
#         #     raise ExamException("ExamException: file name is empty!")
#         # elif isinstance(name, str) == False :
#         #     raise ExamException("ExamException: file name is not string!")

#         try : # Apertura del file.

#             my_file = open(self.name, 'r');
#             my_file.readline();

#         except Exception as e : # Eccezione

#             self.can_read = False;
#             print('Errore in apertura del file: "{}"'.format(e));

#     #----------------------------------------------------------------------------------------------

#     def get_data(self) : # Funzione per estrazione di dati in una list.

#         if not self.can_read : # Condizione file non leggibile.

#             print('Errore, file non aperto o illeggibile');
#             return None;
#         else :

#             data = []; # Definizione list.
#             my_file = open(self.name, 'r');

#             for line in my_file :
#                 elements = line.split(',');
#                 elements[-1] = elements[-1].strip();

#                 if elements[0] != '"date' and elements[1] != 'passengers"' :
#                     data.append(elements);

#                 # if len(data) != len(set(data)) :
#                 #     raise ExamException("ExamException: duplicated values in file!")

#                 # if int(str(elements[1])) > int(str(elements[0])) :
#                 #     raise ExamException("ExamException: CSV file is not sorted!")

#             my_file.close();

#             return data;

    def __init__(self, name):
            
        # Setto il nome del file
        self.name = name
            
        # Provo ad aprirlo e leggere una riga
        # self.can_read = True
        # try:
        #     my_file = open(self.name, 'r')
        #     my_file.readline()
        # except Exception as e:
        #     self.can_read = False
            #print('Errore in apertura del file: "{}"'.format(e))
            #raise ExamException('ExamException: "{}"'.format(e))   


# for i in range(0, len(data_list)) : # Trasformazione della lista in una lista di interi.
    #     for j in range(0, 12) :
    #         to_int = data_list[i][j]
    #         to_int = to_int[:len(to_int) - 1]
    #         data_list[i][j] = to_int