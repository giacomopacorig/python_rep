import unittest
from es2 import Calcolatrice

class TestSomma (unittest.TestCase) :

    def test_somma(self) : 
        calc = Calcolatrice();
        self.assertEqual(calc.somma(1, 1), 2);

class TestMoltiplicazione (unittest.TestCase) :

    def test_moltiplicazione(self) :
        calc = Calcolatrice();
        self.assertEqual(calc.moltiplicazione(3, 2), 6);

class TestDivisione (unittest.TestCase) :

    def test_divisione(self) :
        calc = Calcolatrice();
        self.assertEqual(calc.divisione(8, 4), 2);

class TestSottrazione (unittest.TestCase) :

    def test_sottrazione(self) :
        calc = Calcolatrice();
        self.assertEqual(calc.sottrazione(8, 1), 7);

    