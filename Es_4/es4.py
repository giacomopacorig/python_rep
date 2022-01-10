#CSVFile = open('D:\File\WorkSpace\Python\Es_2\shampoo_sales.csv', 'r');

#Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in 
#modo che converta automaticamente a numero tutte le colonne tranne
#la prima (della data).
#Poi, aggiungete questi due campi al file “shampoo_sales.csv”: 
# 01-01-2015, 
# 01-02-2015,ciao
#e gestite gli errori che verranno generati in modo che le linee vengano saltate 
#senza bloccare il programma ma che venga stampato a schermo l’errore

class CSVFile : # PROVA DI UN GIT
    
    def __init__(self, name) : # Costruttore.

        self.name = name;
        self.can_read = True;

        try : # Apertura del file.

            my_file = open(self.name, 'r');
            my_file.readline();
        except Exception as e :

            self.can_read = False;
            print('Errore in apertura del file: "{}"'.format(e));

#--------------------------------------------------------------------------------------------------
    
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

#==================================================================================================

class NumericalCSVFile(CSVFile) : # Estensione della classe CSVFile.

    def get_data(self) :

        string_data = super().get_data();
        numerical_data = [];

        for string_row in string_data :

            numerical_row = [];

            for i, element in enumerate(string_row) :

                if i == 0 :

                    numerical_row.append(element);

                else :

                    try :
                        numerical_row.append(float(element));
                    except Exception as e :
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e));
                        break;
    
            if len(numerical_row) == len(string_row) :
                numerical_data.append(numerical_row)

        return numerical_data

#==================
# Main.
#==================

file = CSVFile(name = 'D:\File\WorkSpace\Python\python_rep\Es_4\shampoo_sales.csv'); # Assegnazione dell'attributo name.
print('Nome del file: "{}"'.format(file.name));
print('Dati contenuti nel file: "{}"'.format(file.get_data())); 

numerica_file = NumericalCSVFile(name = 'D:\File\WorkSpace\Python\python_rep\Es_4\shampoo_sales.csv');
print('Nome del file: "{}"'.format(numerica_file.name));
print('Dati contenuti nel file: "{}"'.format(numerica_file.get_data()));