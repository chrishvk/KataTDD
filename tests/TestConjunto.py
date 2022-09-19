import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacia_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

