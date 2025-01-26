class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method that adds two numbers
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method that prints the calculation type and multiplies two numbers
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
from class_static_methods_demo import Calculator

def main():
    # Using the static method to add two numbers
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method to multiply two numbers
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
