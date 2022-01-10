class Calcolatrice() :

    def somma(self, a, b) :

        ris = a + b;
        return ris;

    def sottrazione(self, a, b) :

        ris = a - b;
        return ris;

    def moltiplicazione(self, a, b) :

        ris = a * b;
        return ris;

    def divisione(self, a, b) :

        try :
            ris = a / b;
        except ZeroDivisionError :
            ris = "ERRORE: divisore uguale a 0";

        return ris;

    def potenza(self, a, b) :

        ris = pow(a, b);

        return ris;

    def modulo(self, a, b) :

        ris = a % b;

        return ris;

    def radice(self, a, b) :

        if a < 0 :

            raise Exception("Valore radicando negativo");
        else : 
            
            i = 1 / b;
            ris = pow(a, i);

        return ris;

    def convert_base(self, a) :

        "{0:b}".format(a);
         
        return 0;

class Console() :

    def menu(self) :

        calc = Calcolatrice();

        print("\nInserire un operazione da eseguire:\n1 SOMMA\n2 SOTTRAZIONE\n3 MOLTIPLICAZIONE\n4 DIVISIONE\n5 POTENZA\n6 MODULO\n7 RADICE\n8 CONVERSIONE DI BASE");
        cmd = int(input('Operazione: '));

        if cmd == 1 :

            a = float(input("\nInserire il primo numero: "));
            b = float(input("\nInserire il secondo numero: "));
            ris = calc.somma(a, b);
            print(ris);
        elif cmd == 2 :

            a = float(input("\nInserire il primo numero: "));
            b = float(input("\nInserire il secondo numero: "));
            ris = calc.sottrazione(a, b);
            print(ris);
        elif cmd == 3 :

            a = float(input("\nInserire il primo fattore: "));
            b = float(input("\nInserire il secondo fattore: "));
            ris = calc.moltiplicazione(a, b);
            print(ris);
        elif cmd == 4 :

            a = float(input("\nInserire il dividendo: "));
            b = float(input("\nInserire il divisore: "));
            ris = calc.divisione(a, b);
            print(ris);
        elif cmd == 5 :

            a = float(input("\nInserire la base: "));
            b = float(input("\nInserire l'esponente: "));
            ris = calc.potenza(a, b);
            print(ris);
        elif cmd == 6 :

            a = float(input("\nInserire il dividendo: "));
            b = float(input("\nInserire il divisore: "));
            ris = calc.modulo(a, b);
            print(ris);
        elif cmd == 7 :

            a = float(input("\nInserire il radicando: "));
            b = float(input("\nInserire l'indice della radice: "));
            ris = calc.radice(a, b);
            print(ris);
        elif cmd == 8 :

            a = float(input("\nInserire il numero da convertire da base 10 a base 2: "));
            ris = calc.convert_base(a);
            print(ris);

## Main ##
console = Console();
console.menu();