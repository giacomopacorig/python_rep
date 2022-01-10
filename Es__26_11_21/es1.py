# Esercizio 1
# Realizzare un programma con le seguenti funzioni per la manipolazione di liste:
# - stampa, una funzione che stampa il contenuto di una lista passata come argomento;
# - statistiche, una funzione che riceve una lista e, se `e una lista di interi, ne determina la
# somma, la media, il minimo ed il massimo degli elementi;
# - somma vettoriale, una funzione che riceve in ingresso due liste, determina se sono due
# liste di interi, se hanno la stessa dimensione e ne calcola la somma vettoriale, poi ritornata
# come lista, altrimenti ritorna una lista vuota;
# Testare le funzioni passandogli in input diverse liste.
# Nota. Potete usare la funzione built-in type per verificare se una certa variabile `e un (oggetto)
# int oppure no (es: type(var int) == int → true). Non serve importare alcun modulo.

import re;
import unittest;

class Classe () :

    def output(lista) : # Output della lista passata come argomento.

        print(lista);
    
    def somma(a, b) :
        return a+b;

# -------------------------------------------------------------------------------------------------

    def statistics(lista) : # Controllo se la lista è composta da interi, in caso di esito positivo, calcolo delle statistiche.

        somma = 0;
        cnt = 0;
        max = lista[0];
        min = lista[0];
        flag = False;

        for index in lista :

            try :
                num = int(index);
                flag = True;
            except :
                print('La lista non è composta da soli interi');
                flag = False;

            if flag == True :
                somma = somma + index;
                cnt = cnt + 1;
                
                if max < index :
                    max = index;
                
                if min > index :
                    min = index;

            else :
                flag = False;
                break;
        
        if flag == True :

            media = somma / cnt;
            print('Media: "{}"'.format(media));
            print('Somma: "{}"'.format(somma));
            print('Massimo: "{}"'.format(max));
            print('Minimo: "{}"'.format(min));

    # -------------------------------------------------------------------------------------------------

    def vetSum(list_1, list_2) :

        sum = [];
        i = 0; cnt_1 = 0; cnt_2 = 0;
        
        for index_1 in list_1 :

            cnt_1 = cnt_1 + 1;

            try :
                n = int(index_1);
                flag = True;
            except :
                print('La prima lista non è composta da soli interi');
                flag = False;

        for index_2 in list_2 :
            
            cnt_2 = cnt_2 + 1;

            try :
                n = int(index_2);
                flag = True;
            except :
                print('La seconda lista non è composta da soli interi');
                flag = False;

        if flag == True :
            if cnt_1 == cnt_2 :
                print('Le liste hanno la stessa dimensione');

                for i in range(len(list_1)) :
                    sum.append(list_1[i] + list_2[i]);

            else :
                print('Le liste hanno dimensioni diverse');
        
        print(sum);

# =================================================================================================

# ==========
# Main
# ==========

lista = ["stringa", 11, 33.5];
listaInteri = [12, 23, 33, 11, 2];
#listaInteri1 = [12, 23, 33, 11, 2];
#listaInteri2 = [22, 32, 56, 34, 55];
#Classe.output(lista);
#TestClass.testOutput();
#Classe.statistics(listaInteri);
#Classe.vetSum(listaInteri1, listaInteri2);
