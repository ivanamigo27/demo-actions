import unittest
from operaciones import sumar
from operaciones import restar
from operaciones import multiplicar
from operaciones import dividir

class TestOperaciones(unittest.TestCase):
 
    def test_operaciones(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(restar(8, 4), 4)
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(4, 8), -4)
        self.assertEqual(multiplicar(8, 4), 32)
        self.assertEqual(multiplicar(7, 4), 28)
        self.assertEqual(multiplicar(-5, 4), -20)
        self.assertEqual(dividir(8, 4), 2)
        self.assertEqual(dividir(12, 4), 3)
        self.assertEqual(dividir(8, 0), "No se puede dividir por 0")

if __name__ == '__main__':
    unittest.main()