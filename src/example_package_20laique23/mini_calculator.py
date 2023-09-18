class MiniCalculator:
    """
    A simple program for a mini calculator that can perform basic arithmetic operations: addition, subtraction, multiplication, and division.
    """
    def add(self, num1, num2):
        """Addition"""
        return num1 + num2

    def subtract(self, num1, num2):
        """Subtraction"""
        return num1 - num2

    def multiply(self, num1, num2):
        """Multiplication"""
        return num1 * num2

    def divide(self, num1, num2):
        """Division"""
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

# Example usage:
if __name__ == "__main__":
    calculator = MiniCalculator()
    
    num1 = 10
    num2 = 5
    
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

