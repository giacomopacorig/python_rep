def setList(values) :

    for line in myFile :
        elements = line.split(',');

        if elements[0] != 'Date' :
            date = elements[0];
            value = elements[1];
            values.append(float(value));

def sumList(values) :

    somma = 0;

    for index in values:
        somma = somma + index;

    return somma;

def output(somma) :

    print("SOMMA PREZZI: ", somma);


values = [];
somma = 0;
myFile = open('D:\File\WorkSpace\Python\Es_2\shampoo_sales.csv', 'r');

setList(values);
somma = sumList(values);
output(somma);