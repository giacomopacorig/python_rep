import unittest
from es1 import Classe
from math import pi

class TestClass (unittest.TestCase) :
    # def test_output(self) :
    #     lista = ["stringa", 11, 33.5];
    #     lista2 = ["stringa", 11, 33.5];
    #     listaInteri = [1, 2, 2, 2, 2];
    #     self.assertEqual(Classe.output(["stringa", 11, 33.5]), ["stringa", 11, 33.5]);

    def test_somma(self) :
        self.assertEqual(Classe.somma(1,1), 8)

