import datetime
import time

class ExamException(Exception) : # Classe per le eccezioni.
    pass

###################################################################################################

class CSVFile :
    
    def __init__(self, name) : # Costruttore.
        pass

    #----------------------------------------------------------------------------------------------
    
    def get_data(self) : # Funzione per estrazione dei dati in una list.
        pass

###################################################################################################

class CSVTimeSeriesFile(CSVFile) : # Classe per apertura e lettura del file con controllo dei dati contenuti.

    def __init__(self, name) : # Costruttore.
            
        self.name = name # Dichiarazione del nome del file.      

#--------------------------------------------------------------------------------------------------

    def get_data(self) : # Apertura e lettura del file riga per riga.

        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False

        if self.name[-4:] != '.csv' :
            raise Exception("ExamException: file is not a CSV file!") # Eccezione se il file non è di tipo CSV.
            
        if not self.can_read : # Condizione di file non leggibile o non apribile. 
            
            raise ExamException("ExamException: file not open or unreadable")
             
            return None

        else: # Condizione di file leggibile
            
            data = [] # Lista per la memorizzazione dei dati.
        
            my_file = open(self.name, 'r') # Apertura del file.

            prev_date = time.strptime("0001-01", "%Y-%m")
            check_date = prev_date

            for line in my_file : # Lettura del file riga per riga.
                    
                elements = line.split(',')
                    
                elements[-1] = elements[-1].strip()
                    
                if elements[0] != 'date' : # Controllo se l'elemento processato è l'intestazione.

                    if elements[1] == '' or elements[1] == None : # Aggiunta dell'elemento alla lista.
                        elements[1] = 0
                    # print(elements[0])

                    year = elements[0].split('-')[0]
                    month = elements[0].split('-')[1]

                    # Controllo delle eccezioni.
                    if int(month) < 0 or int(month) > 12 :
                        raise ExamException("ExamException: invalid month in file")

                    try :
                        current_date = time.strptime(elements[0], "%Y-%m")
                        # if isinstance(int(elements[1]), int) == False :
                        #     elements[1] = 0
                        if not elements[1].isdigit() or int(elements[1]) < 0 : 
                            elements[1] = 0
                        data.append([elements[0] , int(elements[1])])
                    except Exception as e :
                        #data.append(0, 0)
                        data.append([0, 0])

                    count_date = count_element(current_date, 0, data, len(data))
                    
                    if not current_date > prev_date :
                        raise ExamException("ExamException: file is not sorted by date")

                    if count_date > 1 :
                        raise ExamException("ExamException: duplicated date in file!")

                    if current_date < check_date :
                        raise ExamException("ExamException: negative date in file")

                    prev_date = current_date

            my_file.close() # Chiusura del file
                
            return data # Ritorno dei dati

###################################################################################################

def compute_avg_monthly_difference(time_series, first_year, last_year) : # Funzione per il calcolo della differenza media del numero di passeggeri mensile tra anni consecutivi

    # Controllo delle eccezioni.
    if isinstance(time_series, list) == False : 
        raise ExamException("ExamException: time_series must be a list!") # Se time_series non è una lista.

    if time_series == None :
        raise ExamException("ExamException: time_series must not be None!") # Se time_series è None.
    
    if time_series == [] :
        raise ExamException("ExamException: time_series must not be empty!") # Se time_series è vuota.

    if len(time_series) <= 1 :
        raise ExamException("ExamException: time_series's length is too small!") # Se time_series è troppo piccola.
    
    if isinstance(first_year, str) == False or isinstance(last_year, str) == False :
        raise ExamException("ExamException: first_year and last_year must be string!") # Se gli estremi dell'intervallo da valutare non sono stringhe.

    if not first_year.isdigit() or not last_year.isdigit() :
        raise ExamException("ExamException: first_year and last_year are not valid!") # Se gli estremi dell'intervallo da valutare non sono validi.

    if int(first_year) < 0 or int(last_year) < 0 :
        raise ExamException("ExamException: first_year and last_year must be positive!") # Se i valori interi degli estremi dell'intervallo sono minori di 0.

    if first_year == None or last_year == None :
        raise ExamException("ExamException: first_year and last_year must not be None!") # Se i gli estremi dell'intervallo sono None.

    if first_year == "" or last_year == "" :
        raise ExamException("ExamException: first_year and last_year must not be empty!") # Se i gli estremi dell'intervallo sono vuoti.

    if int(last_year) <= int(first_year) :
        raise ExamException("ExamException: last_year must be greater than first_year!") # Se l'ultimo anno dell'intervallo è minore o uguale del primo.
    
    list_avg_monthly_difference = [] # Lista per la memorizzazione delle differenze mensili
    data_list = [] # Lista per la memorizzazione dei soli dati sul numero di passeggeri
    partial_list = [] # Lista di passaggio.
    first_year = int(str(first_year)) # Valore intero del primo anno dell'intervallo.
    last_year = int(str(last_year)) # Valore intero dell'ultimo anno dell'intervallo.
    difference = last_year - first_year # Differenza tra l'ultimo e il primo anno (= lunghezza dell'intervallo da esaminare).
    year = first_year # Variabile contatore per l'anno esaminato settata come punto di partenza al primo anno dell'intervallo.

    year_month = str(year) + "-01"
    year_month_index = search_index(year_month, time_series) # Ricerca del primo mese per il primo anno considerato.

    for i in range(difference + 1) : # Memorizzazione dei dati relativi al numero di passeggeri in una lista.

        for j in range(12) : 

            partial_list.append(time_series[year_month_index][1]) # Memorizzazione nella lista di passaggio del dato sul numero di passeggeri per una certa data.
            year_month_index += 1 # Incremento dell'indice relativo alla data.
        
        data_list.append(partial_list) # Trasferimento della lista di passaggio in un'altra lista.
        partial_list = [] # Cancellazione del contenuto della lista di passaggio.

    sum_element = 0 # Variabile per la somma degli elementi
    list_index = len(data_list) - 1 # Indice per l'esaminazione delle liste.
    month_index = 0 # Indice per l'esaminazione dei mesi delle liste.

    for i in range(0, len(data_list)) : # Ciclo per il controllo dei dati esaminati.
        for j in range(0, 12) :
            if isinstance(data_list[i][j], int) == False or data_list[i][j] < 0 and data_list[i][j] == None and data_list[i][j] == "" : # Se il numero di passeggeri esaminato non è un intero, è minore di zero, è None oppure è vuoto...
                data_list[i][j] = 0 # ...il dato esaminato viene settato a 0 se non valido.

    while(month_index < 12) : # Ciclo per il calcolo delle differenze medie tra mesi.

        if month_index == 12 :
            break

        missing_data = count_element(0, month_index, data_list, len(data_list)) # Controllo del numero di dati mancanti per un dato mese.

        if difference == 1 and missing_data > 0 : # Se gli anni esaminati sono 1 e manca un dato per un dato mese.
            sum_element = 0
        elif difference > 1 and missing_data > 2 : # Se gli anni esaminati sono più di 2 e mancano più di due dati per un dato mese. 
            sum_element = 0
        else : # Se gli anni esaminati sono più di 2 e mancano meno di due dati per un dato mese. 
            sum_element += int(data_list[list_index][month_index]) - int(data_list[list_index - 1][month_index])

        list_index -= 1 # Decremento dell'indice per le liste.

        if list_index == 0 : # Se l'indice delle liste è arrivato a zero...
            sum_element = sum_element / difference # Calcolo della media dividendo la somma calcolata per la lunghezza dell'intervallo.
            month_index += 1 # Incremento dell'indice per il mese (= passaggio al calcolo del mese successivo).
            list_index = len(data_list) - 1 # Ri-settaggio dell'indice delle liste al punto di partenza.
            list_avg_monthly_difference.append(sum_element) # Memorizzazione dei dati ottenuti nella lista precedentemente dichiarata.
            sum_element = 0 # Settaggio della somma a 0.

    #print(list_avg_monthly_difference) # Stampa di prova della lista.

    return list_avg_monthly_difference # Ritorno della lista ottenuta.

###################################################################################################

def count_element(element_to_count, index, list_to_examinate, length) : # Metodo per il conteggio di un dato elemento in una data lista.

    cnt = 0 # Contatore settato a 0.
    element_counter = 0 # Contatore per il conteggio dell'elemento settato a 0.

    while cnt < length : # Ciclo per il conteggio.
        if list_to_examinate[cnt][index] == element_to_count : # Se l'elemento cercato è uguale all'elemento corrente della lista. 
            element_counter += 1 # Incremento del contatore per le apparizioni dell'elemento.
        cnt += 1 # Incremento del contatore.
    
    return element_counter # Ritorno del numero di apparizioni dell'elemento.

###################################################################################################

def search_index(element_to_search, list_to_examinate) : # Metodo per la ricerca dell'indice di un dato elemento in una data lista.

    element_in_list = False # Variabile booleana setta a False per il controllo della presenza dell'elemento o meno.

    for list in list_to_examinate : # Ciclo per la verifica di un elemento in lista.
        if element_to_search in list : # Se l'elemento è in lista...
            element_in_list = True # ...settaggio della variabile booleana a True.

    if element_in_list == False : # Se l'elemento non è presente in lista...
        raise ExamException("ExamException: value not in list") # ...viene sollevata un eccezione.
    
    index = [(i, list_to_examinate.index(element_to_search)) for i, list_to_examinate in enumerate(list_to_examinate) if element_to_search in list_to_examinate] # Memorizzazione dell'indice dell'elemento in una variabile.
    index = int(index[0][0]) # Memorizzazione del primo elemento della prima lista (= in questo caso una data).

    return index # Valore di ritorno.

###################################################################################################

# ---- #
# Main #
# ---- #

# time_series_file = CSVTimeSeriesFile(name = 'data.csv')
# time_series = time_series_file.get_data()
# compute_avg_monthly_difference(time_series, "1949", "1951")