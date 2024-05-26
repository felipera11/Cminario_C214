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
    def setUp(self):
        self.calculator = Calculator()
    def test_subPrimMenor(self):
        res = self.calculator.subtract(3,8)
        self.assertEqual(res,-2)
    
    def test_subSegMenor(self):
        res = self.calculator.subtract(7,3)
        self.assertEqual(res,4)
    
    def test_subSegundoNeg(self):
        res = self.calculator.subtract(30,-5)
        self.assertEqual(res,35)



class TestMul(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_porZero1(self):
        res = self.calculator.multiply(0,8)
        self.assertEqual(res,0)

    def test_porZero2(self):
        res = self.calculator.multiply(4,0)
        self.assertEqual(res,0)
    
    def test_doisNeg(self):
        res = self.calculator.multiply(-3,-5)
        self.assertEqual(res,15)

    def test_umNeg(self):
        res = self.calculator.multiply(-3,5)
        self.assertEqual(res,-15)


class TestDiv(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_porZero(self):
        self.assertRaises(ValueError,self.calculator.divide(1,0))

    def test_div(self):
        res = self.calculator.divide(150,30)


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_quadrado(self):
        res = self.calculator.square(8)
        self.assertEqual(res,64)


class TestDiv(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_raizNeg(self):
        self.assertRaises(ValueError,self.calculator.squareRoot(-9))

    def test_raiz(self):
        res = self.calculator.squareRoot(9)
        self.assertEqual(res,3)


class TestPot(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_potencia(self):
        res = self.calculator.power(3,3)
        self.assertEqual(res,27)


class TestFatorial(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()  

    def test_fatNeg(self):
        self.assertRaises(ValueError,self.calculator.factorial(-1))

    def test_fat(self):
        res = self.calculator.factorial(5)
        self.assertEqual(res,120)

class TestPot(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    @unittest.expectedFailure
    def test_primo(self):
        res = self.calculator.power(1)
        self.assertTrue(res)


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_fibNeg(self):
        self.assertRaises(ValueError,self.calculator.factorial(-1))

    def test_fib(self):
        res = self.calculator.fibonacci(6)
        self.assertEqual(res,8)


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