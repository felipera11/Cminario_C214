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
        self.assertEqual(res,-5)
    
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
        with self.assertRaises(ValueError):
            self.calculator.divide(1,0)

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
        with self.assertRaises(ValueError):
            self.calculator.squareRoot(-9)

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
        with self.assertRaises(ValueError):
            self.calculator.factorial(-1)

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
        with self.assertRaises(ValueError):
            self.calculator.factorial(-1)

    def test_fib(self):
        res = self.calculator.fibonacci(6)
        self.assertEqual(res,8)



class TestPar(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_evenFalse(self):
        res = self.calculator.fibonacci(3)
        self.assertFalse(res)

    def test_evenTrue(self):
        res = self.calculator.isEven(6)
        self.assertTrue(res)


class TestImpar(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_evenFalse(self):
        res = self.calculator.fibonacci(100)
        self.assertFalse(res)

    def test_evenTrue(self):
        res = self.calculator.isEven(999)
        self.assertTrue(res)


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_Palind(self):
        res = self.calculator.isPalindrome("socorram me subi no onibus em marrocos")
        self.assertFTrue(res)

    @unittest.expectedFailure
    def test_naoPalind(self):
        res = self.calculator.isEven("hello world")
        self.assertTrue(res)






'''   
    
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