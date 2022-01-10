# Esercizio 2
# Implementare una funzione (simile a quella creata le lezioni precedenti) che ritorni una lista i
# cui elementi saranno le date delle vendite del file shampoo sales.csv.
# Attenzione: Avevate usato la funzione float per convertire i prezzi da stringhe a valori numerici. Questa volta dovrete usare un’altra funzione:
# from datetime import datetime
# ...
# my date = datetime.strptime (elements[0],’%d-%m-%Y’)
# 1
# Questa conversione vi permetter`a di eseguire operazioni con le date (come trovare la data pi`u
# lontana, quella pi`u vicina, la conversione in mesi, ecc ecc..). Stampando la lista per`o, vederete
# degli oggetti di tipo DateTime. Se volete stampare le date in modo pi`u leggibile, i comandi
# sono i seguenti:
# for data in date_vendite:
# print(data.strftime(’%d-%m-%Y’))

from datetime import datetime;
import re;

class Classe() :

    def readFile() :

        file = open("D:\File\WorkSpace\Python\shampoo_sales.csv", "r");
        text = file.read();
        dates = re.findall(r'(\d+/\d+/\d+)',text);

        for index in dates :
            print("DATA: ", index, "\n");


Classe.readFile();