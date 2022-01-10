# ***** INTRO & VARIABILI ***** #
print("Ciao a tutti"); #Output di una stringa.
print(42); #Output di un numero.
print(4 * 5); #Output di un prodotto.
print("Ciao" * 5); #Stringa ripetuta 5 volte.

intero = 10 + 2; #Assegnazione valore intero variabile.
decimale = 10.2; #Assegnazione valore decimale variabile.
booleana = True; #Assegnazione valore booleano variabile.
stringa = "Ciao a tutti"; #Assegnazione stringa variabile.
print(intero, stringa); #Stampa di due variabili.
print(type(intero)); #Stampa del tipo della variabile specificata.

a = 10;
b = 20;
t = 4;
print((a + b) / t); #Output operazione.

###################################################################################################

# ***** STRINGHE ***** #
print(stringa[0]); #Stampa della prima lettera della stringa.
print(stringa[0:2]); #Stampa dalla prima alla lettera 1.
print(stringa[:3]); #Stampa dall'inizio alla lettera 2.
print(stringa[3:]); #Stampa dalla lettera 3 alla fine.
print(stringa[-3]); #Stampa del terz'ultimo carattere.
print(stringa[:-3]); #Stampa dall'inizio senza gli ultimi 3 caratteri.
print(stringa[-3:]); #Stampa degli ultimi 3 caratteri.

###################################################################################################

# ***** OPERAZIONI SU STRINGHE ***** #
parola = "ciao a tutti";
a1 = parola[:4];
a2 = parola[4:6];
a3 = parola[7:];
print(a1, a2, a3);

citta1 = "Torino";
citta2 = "Moncalieri";
print("Io abito a {} vicino a {}".format(citta1, citta2)); #Stampa con inserimento di variabili nella stringa.
print(stringa.upper); #Stampa in maiuscolo.
print(stringa.lower); #Stampa in minuscolo.
print(stringa.capitalize); #Stampa con solo la prima lettera in maiuscolo.
print(stringa.find("Ciao")); #Restituisce il valore -1 se la parola non viene trovata oppure restituisce la posizione di inizio della parola.
print(stringa.replace("Ciao", "Buongiorno")); #Sostituisce la parola data con un'altra data.
print("Ciao" in stringa); #Resituisce un valore booleano dalla ricerca di una parola in una stringa.
print("Ciao", "Buongiorno", 1) #Sostituisci la parola Ciao con Buongiorno solo 1 volta.

###################################################################################################

# ***** IF & ELSE & ELSE IF ***** #
variabile = "Gino";
if variabile == "Gino":
    print("Frase dentro la condizione IF");

print("Frase fuori la condizione IF");

if variabile == "Gino":
    print("Frase dentro la condizione IF");
elif variabile == "Ciano":
    print("Frase dentro ELIF");
else:
    print("Frase dentro la condizione ELSE");

if variabile == "Gino" and variabile != "Pino":
    print("Condizione AND");
elif variabile == "Gino" or variabile == "Pino":
    print("Condizione OR");

###################################################################################################

# ***** INPUT ***** #
variabile = input("Inserire un nome: ");
print(variabile);
variabile = int(input("Inserire un numero: "));
#variabile = int(variabile); #Conversione in intero post-INPUT.

###################################################################################################

# ***** WHILE ***** #
while variabile == 10:
    print("ciao");

###################################################################################################

# ***** FOR ***** #
for variabile in range(10):
    print(variabile);

for variabile in range (2, 10): #Da 2 a 10.
    print(variabile);

for variabile in range (2, 10, 3): #Da 2 a 10 compiendo un salto di 3 (quindi 2, 5, 8).
    print(variabile);

stringa = "Ciao bello";
for variabile in stringa: #Eseguito per ogni lettera contenuta in stringa.
    if variabile != "t":
        print(variabile);

###################################################################################################

# ***** LISTE ***** #
lista = ["ciao", 22, 22.5];
lista2 = lista.copy(); #Copia di una lista in un'altra.
print(lista); #Stampa tutta la lista.
print(lista[1]); #Stampa il numero 22. Usa le slice con i : come le stringhe.

for indice in lista: #Stampa dei singoli elementi della lista.
    print(lista[indice]);

print("ciao" in lista); #Restituisce il valore booleano in base all'elemento cercato nella lista.
lista.index("ciao"); #Restituisce l'indice del valore specificato.

lista.append("valore da aggiungere"); #Aggiunta di un valore alla lista.
lista.insert(7, "valore in una determinata posizione"); #Aggiunta di un valore ad un indice specificato.
lista.remove("elemento da rimuovere"); #Rimozione di un elemento dalla lista.
lista.clear(); #Cancellazione totale della lista.
lista.count(22); #Conteggio valore specificato.
lista.sort(); #Ordinamento alfabetico lista.
lista.reverse(); #Ordinamento alfabetico inverso.

###################################################################################################

# ***** TUPLE ***** #
# N.B. Le tuple non possono essere modificate (non esiste append e simili).
tupla = ("ciao belli", "buonasera", "helo");
print(tupla);
tupla.count();
tupla.index();

###################################################################################################

# ***** DIZIONARI ***** #
# N.B. Utilizzati per l'archiviazione di dati, come tuple/liste ma non con indice numerico ma indice mnemonico

dizionario = {"nome":"gianni", "cognome":"rossi", "eta":44};
print(dizionario["nome"]); #Stampa dell'indice nome.
print(dizionario.get("nome")); #Metodo alternativo al precedente.

dizionario["indirizzo"] = "Via Galilei"; #Aggiunta di un elemento al dizionario.

###################################################################################################

# ***** SPLIT ***** #
parola = "ciao a tutti quanti";
lista = parola.split("tutti"); #La parola "tutti" viene esclusa dalla lista.
lista = parola.split(" "); #Esclude gli spazi.

###################################################################################################

# ***** FUNZIONI ***** #
def nomeFunzione() : #Definizione funzione.
    print("Output dentro la funzione");

def nomeFunzione2(c) :
    return c;

nomeFunzione(); #Chiamata funzione.

###################################################################################################

# ***** GESTIONE ERRORI ***** #
try:
    numero = int(input("Inserire un numero: "));
    print(numero * 3);
except: #Seguita dal tipo di errore (ValueError, ZeroDivisionError, ecc.).
    print("Errore nell'inserimento");

###################################################################################################

# ***** FILE ***** #
file = open("nome.txt", "w"); #Specifica del file da creare e della modalità di collegamento (w = write).
file.write("Testo da scrivere");
file = open("nome.txt", "a"); #Append.
file.write("\nTesto aggiunto in append");
file.close();

file = open("nome.txt", "r"); #Lettura.
x = file.read(); #Lettura totale del file, per leggere riga per riga utilizzare readLine che crea una lista dove ogni elemento è una riga del file.
print(x);
file.close();

###################################################################################################

# ***** OGGETTI ***** #
class NomeClasse :
    
    def metodo() :
        print("Output metodo classe");

alfa = NomeClasse;
alfa.metodo();

beta = NomeClasse;
beta.metodo();

class Veicoli :

    def __init__(self, marca, modello, colore): #Costruttore.
        self.marca = marca;
        self.modello = modello;
        self.colore = colore;

    def scheda(self) :
        x = "Ho una {} modello {} di colore {}".format(self.marca, self.modello, self.colore);
        return x;

veicolo = Veicoli("Ford", "Fiesta", "Rosso");
print(veicolo.scheda());

class Auto(Veicoli) : #Estensione di un oggetto.

    def __str__(self) :
        return 'Auto "{} {}"'.format(self.marca, self.modello);
    
    def accendi(self) :
        print('Broom broom {} {}'.format(self.marca, self.modello));

###################################################################################################

# ***** EREDITARIETA' ****** #
class Auto(Veicoli) :

    def __init__(self, marca, modello, colore, cilindrata):
        super().__init__(marca, modello, colore);
        self.cilindrata = cilindrata;

    def scheda(self) :
        x = " con cilindrata {}".format(self.cilindrata);
        return super().scheda() + x;

class Bici(Veicoli) :
    pass; #Passa alla prossima istruzione saltando questa istruzione.

auto = Auto("Fiat", "Panda", "Verde", "1300");
print(auto.scheda);

###################################################################################################

# ***** MODULI ***** #
# N.B. Per vedere i moduli di Python disponibili e relative funzionalità consultare il sito ufficiale.

import calendar; #Import del modulo calendar.
calendar.prmonth(2020, 1); #Stampa di un dato mese in un dato anno (gennaio 2020).

import calendar as cc; #Import di calendari chiamato "cc".
cc.prmonth(2020, 1);

from calendar import *; #Import dal modulo calendar di tutti i metodi.
print(prmonth(2020, 1));

#Creazione di un modulo per calcolo area e perimetro rettangolo. Creare nuovo file (Rettangolo.py).
from rettangolo import *;
print("L'area del rettangolo è: " + area_ret(11, 22));

###################################################################################################