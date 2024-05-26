import unittest
from calculator import Calculator

class TestSoma(unittest.TestCase):
    def test_sumPos(self):
        soma = sum(3,5)
        self.assertEqual(soma,8)
    
    def test_sumNeg(self):
        soma = sum(-3,-1)
        self.assertEqual(soma,-4)


