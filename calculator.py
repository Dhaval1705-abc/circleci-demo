class Calculator:
    """A simple calculator with multiple operations"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


if _name_ == "_main_":
    calc = Calculator()
    print("5 + 3 =", calc.add(5, 3))
    print("10 - 7 =", calc.subtract(10, 7))
    print("6 × 4 =", calc.multiply(6, 4))
    print("20 ÷ 5 =", calc.divide(20, 5))
    print("Factorial of 5 =", calc.factorial(5))
