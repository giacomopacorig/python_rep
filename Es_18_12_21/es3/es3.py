import itertools;

class CSVFile() :

    def get_data(self, start, end) :

        text_file = open("D:\File\WorkSpace\Python\shampoo_sales.csv", "r");
        lines = [];

        if start != None and end != None : 

            with open("D:\File\WorkSpace\Python\shampoo_sales.csv", "r") as text_file :
                for line in itertools.islice(text_file, start - 1, end) :
                    lines.append(line);
        else :

            with open("D:\File\WorkSpace\Python\shampoo_sales.csv", "r") as text_file :
                for line in text_file :
                    lines.append(line);

        text_file.close();

        return lines;

###################################################################################################

class Console() :

    def menu(self) :

        csv = CSVFile();
        start = input("Inserire riga di inizio (premere . per non assegnare nessun valore): ");
        end = input("Inserire riga di fine (premere . per non assegnare nessun valore): ");

        while start > end :

            print("\nValori non validi: inizio maggiore di fine, riprovare: ");

            start = input("Inserire riga di inizio: ");
            end = input("Inserire riga di fine: ");

        if start != '.' and end != '.' :

            lines = csv.get_data(int(start), int(end));
        else :
            lines = csv.get_data(None, None);

        print(lines);

###################################################################################################

## Main ##

csv = CSVFile();
console = Console();
console.menu();