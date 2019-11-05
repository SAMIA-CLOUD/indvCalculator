import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add(self):
        test_data = CsvReader("Tests/Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    # def test_subtract_method_calculator(self):
    #     self.assertEqual(self.calculator.subtract(2, 2), 0)
    #     self.assertEqual(self.calculator.result, 0)

    def test_subtract(self):
        test_data = CsvReader("Tests/Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply(self):
        test_data = CsvReader("Tests/Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide(self):
        test_data = CsvReader("Tests/Division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_root(self):
        test_data = CsvReader("Tests/SquareRoot.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square_root(row['Value 1']), round(result,8))
        # self.assertEqual(self.calculator.square_root(row['Value 1']), result)
        # self.assertEqual("nan", self.calculator.square_root(-4))

    # def test_square_root_method_calculator(self):
    #     self.assertEqual(2, self.calculator.square_root(4))
    #     self.assertEqual(0, self.calculator.square_root(0))
    #    self.assertEqual("nan", self.calculator.square_root(-4))

    def test_square(self):
        test_data = CsvReader("Tests/Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()
