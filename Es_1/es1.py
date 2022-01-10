def sumList(lista) :
    somma = 0;
    for index in lista:
        somma = somma + index;
    return somma;

def output(somma) :
    print("SOMMA ELEMENTI LISTA: ", somma);

lista = [1, 5, 3, 4];
somma = sumList(lista);
output(somma);
#ciaociao