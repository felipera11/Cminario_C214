import unittest
from src.calculator import Calculator

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_sumPos(self):
        res = self.calculator.add(3,5)
        self.assertEqual(res,8)
    
    def test_sumNeg(self):
        res = self.calculator.add(4,-1)
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


class TestDiv(unittest.TestCase):
    def test_porZero(self):
        self.assertRaises(Exception,Calculator.divide(1,0))

    def test_div(self):
        res = Calculator.divide(150,30)

class TestSquare(unittest.TestCase):
    def test_quadrado(self):
        res = Calculator.square(8)
        self.assertEqual(res,64)

class TestDiv(unittest.TestCase):
    def test_raizNeg(self):
        self.assertRaises(Exception,Calculator.squareRoot(-9))

    def test_raiz(self):
        res = Calculator.squareRoot(9)
        self.assertEqual(res,3)


class TestPot(unittest.TestCase):
    def test_potencia(self):
        res = Calculator.power(3,3)
        self.assertEqual(res,27)


class TestFatorial(unittest.TestCase):
    def test_fatNeg(self):
        self.assertRaises(Exception,Calculator.factorial(-1))

    def test_fat(self):
        res = Calculator.factorial(5)
        self.assertEqual(res,120)

class TestPot(unittest.TestCase):
    @unittest.expectedFailure
    def test_primo(self):
        res = Calculator.power(1)
        self.assertTrue(res)


class TestFibonacci(unittest.TestCase):
    def test_fibNeg(self):
        self.assertRaises(Exception,Calculator.factorial(-1))

    def test_fib(self):
        res = Calculator.fibonacci(6)
        self.assertEqual(res,5)


''' 
    
    def fibonacci(self, a):
        if a < 0:
            raise ValueError("Fibonacci of negative number")
        if a == 0:
            return 0
        if a == 1:
            return 1
        return self.fibonacci(a - 1) + self.fibonacci(a - 2)
    
    def isEven(self, a):
        return a % 2 == 0
    
    def isOdd(self, a):
        return a % 2 != 0
    
    def isPalindrome(self, a):
        return str(a) == str(a)[::-1]
    
    def isPositive(self, a):
        return a > 0
    
    def isNegative(self, a):
        return a < 0
    
    def isZero(self, a):
        return a == 0
    
    def isDivisible(self, a, b):
        return a % b == 0
    
    def isMultiple(self, a, b):
        return b % a == 0
'''