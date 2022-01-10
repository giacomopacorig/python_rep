#CSVFile = open('D:\File\WorkSpace\Python\Es_2\shampoo_sales.csv', 'r');

#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista 
#di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
#Provatelo sul file “shampoo_sales.csv”.

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

# Main.

file = CSVFile(name = 'D:\File\WorkSpace\Python\Es_2\shampoo_sales.csv'); # Assegnazione dell'attributo name.
print('Nome del file: "{}"'.format(file.name));
print('Dati contenuti nel file: "{}"'.format(file.get_data())); 