class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    
    def square(self, a):
        return a ** 2
    
    def squareRoot(self, a):
        if a < 0:
            raise ValueError("Square root of negative number")
        return a ** 0.5
    
    def power(self, a, b):
        return a ** b
    
    def factorial(self, a):
        if a < 0:
            raise ValueError("Factorial of negative number")
        if a == 0:
            return 1
        return a * self.factorial(a - 1)
    
    def isPrime(self, a):
        if a < 2:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    
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
    