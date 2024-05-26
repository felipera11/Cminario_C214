import unittest
from calculator import Calculator

class TestAdd(unittest.TestCase):
    def test_sumPos(self):
        res = Calculator.add(3,5)
        self.assertEqual(res,8)
    
    def test_sumNeg(self):
        res = Calculator.add(4,-1)
        self.assertEqual(res,3)



class TestSub(unittest.TestCase):
    def test_subPrimMenor(self):
        res = Calculator.subtract(3,8)
        self.assertEqual(res,-2)
    
    def test_subSegMenor(self):
        res = Calculator.subtract(7,3)
        self.assertEqual(res,4)
    
    def test_subSegundoNeg(self):
        res = Calculator.subtract(30,-5)
        self.assertEqual(res,35)



class TestMul(unittest.TestCase):
    def test_porZero1(self):
        res = Calculator.multiply(0,8)
        self.assertEqual(res,0)

    def test_porZero2(self):
        res = Calculator.multiply(4,0)
        self.assertEqual(res,0)
    
    def test_doisNeg(self):
        res = Calculator.multiply(-3,-5)
        self.assertEqual(res,15)

    def test_umNeg(self):
        res = Calculator.multiply(-3,5)
        self.assertEqual(res,-15)
