# Estendere la classe CSVFile che avete creato la scorsa lezione, aggiungendo i seguenti metodi:
#  get date vendite(): questa funzione ritorner`a una lista con le date delle vendite. (Hint:
# usare la funzione creata nell’esercizio 2);
#  str (): questa funzione ritorner`a l’intestazione (header) del file CSV.

import datetime;
import re;

class CSVFile :
    
    def __init__(self, name) : # Costruttore.

        self.name = name;
        self.can_read = True;

        try : # Apertura del file.

            my_file = open(self.name, 'r');
            my_file.readline();
        except Exception as e :

            self.can_read = False;
            print('Errore in apertura del file: "{}"'.format(e));

    #----------------------------------------------------------------------------------------------
    
    def get_data(self) : # Funzione per estrazione dei dati in una list.

        if not self.can_read : # Condizione file non leggibile.

            print('Errore, file non aperto o illeggibile');
            return None;
        else :

            data = []; # Definizione list.
            my_file = open(self.name, 'r');

            for line in my_file:

                elements = line.split(',');
                elements[-1] = elements[-1].strip();

                if elements[0] != 'Date' :

                    data.append(elements);

            my_file.close();

            return data;

    #----------------------------------------------------------------------------------------------
    
    def get_date_vendite(self) :

        if not self.can_read : # Condizione file non leggibile.

            print('Errore, file non aperto o illeggibile');
            return None;
        else :

            listDate = []; # Definizione list.
            my_file = open(self.name, 'r');

            text = my_file.read();
            listDate = re.findall(r'(\d+-\d+-\d+)',text);

            my_file.close();

            return listDate;

    #----------------------------------------------------------------------------------------------

    def str(self) :

        if not self.can_read : # Condizione file non leggibile.

            print('Errore, file non aperto o illeggibile');
            return None;
        else :

            data = []; # Definizione list.
            my_file = open(self.name, 'r');

            for line in my_file:

                elements = line.split(',');
                elements[-1] = elements[-1].strip();

                if elements[0] == 'Date' :

                    data.append(elements);

            my_file.close();

            return data;

###################################################################################################

# Main.

file = CSVFile(name = 'D:\File\WorkSpace\Python\Es_2\shampoo_sales.csv'); # Assegnazione dell'attributo name.
print('\nNome del file: "{}"'.format(file.name));
print('\nDati contenuti nel file: "{}"'.format(file.get_data())); 
print('\nDate delle vendite del file: "{}"'.format(file.get_date_vendite()));
print('\nIntestazione del file: "{}"'.format(file.str()));