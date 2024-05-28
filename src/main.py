from calculator import Calculator

def choose_operation():
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square root")
    print("7. Power")
    print("8. Factorial")
    print("9. Is prime")
    print("10. Fibonacci")
    print("11. Is even")
    print("12. Is odd")
    print("13. Is palindrome")
    print("14. Is positive")
    print("15. Is negative")
    print("16. Is zero")
    print("17. Is divisible")
    print("18. Is multiple")
    print("-1. Exit")
    print("Enter operation number:")
    return int(input())

def main():
    calculator = Calculator()
    while True:
        operation = choose_operation()
        if operation == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(calculator.add(a, b))
        elif operation == 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(calculator.subtract(a, b))
        elif operation == 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(calculator.multiply(a, b))
        elif operation == 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(calculator.divide(a, b))
        elif operation == 5:
            a = float(input("Enter number: "))
            print(calculator.square(a))
        elif operation == 6:
            a = float(input("Enter number: "))
            print(calculator.squareRoot(a))
        elif operation == 7:
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print(calculator.power(a, b))
        elif operation == 8:
            a = int(input("Enter number: "))
            print(calculator.factorial(a))
        elif operation == 9:
            a = int(input("Enter number: "))
            print(calculator.isPrime(a))
        elif operation == 10:
            a = int(input("Enter number: "))
            print(calculator.fibonacci(a))
        elif operation == 11:
            a = int(input("Enter number: "))
            print(calculator.isEven(a))
        elif operation == 12:
            a = int(input("Enter number: "))
            print(calculator.isOdd(a))
        elif operation == 13:
            a = input("Enter string: ")
            print(calculator.isPalindrome(a))
        elif operation == 14:
            a = float(input("Enter number: "))
            print(calculator.isPositive(a))
        elif operation == 15:
            a = float(input("Enter number: "))
            print(calculator.isNegative(a))
        elif operation == 16:
            a = float(input("Enter number: "))
            print(calculator.isZero(a))
        elif operation == 17:
            a = float(input("Enter number: "))
            b = float(input("Enter divisor: "))
            print(calculator.isDivisible(a, b))
        elif operation == 18:
            a = float(input("Enter number: "))
            b = float(input("Enter multiple: "))
            print(calculator.isMultiple(a, b))
        elif operation == -1:
            break
        else:
            print("Invalid operation")

if __name__ == "__main__":
    main()