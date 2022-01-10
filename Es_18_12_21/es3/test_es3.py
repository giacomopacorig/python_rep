import unittest;
from es3 import CSVFile;
from es3 import Console;

class Test(unittest.TestCase) :

    #file = open("D:\File\WorkSpace\Python\shampoo_sales.csv", "r");

    def test_sum(self) :

        csv = CSVFile();
        file = open("D:\File\WorkSpace\Python\shampoo_sales.csv", "r");
        readFile = file.read();

        self.assertEqual(csv.get_data(1, 37), csv.get_data(None, None));
