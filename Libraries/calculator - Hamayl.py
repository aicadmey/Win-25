class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def add(self, x):
        self.value += x
        return self.value

    def subtract(self, x):
        self.value -= x
        return self.value

    def multiply(self, x):
        self.value *= x
        return self.value

    def divide(self, x):
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.value /= x
        return self.value

    def clear(self):
        self.value = 0
        return self.value

    def __str__(self):
        return f"Current Value: {self.value}"


