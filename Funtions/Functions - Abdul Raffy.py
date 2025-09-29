'''  1- Write 5 functions without parameters. '''

# 1. Function to print a greeting
def greet():
    print("Hello, welcome to the program!")

greet()

# 2. Function to calculate factorial
def calculate_factorial():
    num = int(input("Enter a number to find its factorial: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")

calculate_factorial()

# 3. Function to print a motivational quote
def motivational_quote():
    print("Believe in yourself and all that you are!")
    
motivational_quote()

# 4. Function to calculate the square of a fixed number (e.g., 5)
def square_of_five():
    print(f"The square of 5 is {5**2}")

square_of_five()

# 5. Function to print the user's lucky number
def lucky_number():
    print(f"Your lucky number is {a}!")

a = int(input("enter your number: "))
lucky_number()



''' 2- Write 5 functions with using two parameters. '''

# 1. Function to Add Two Numbers
def add_two_numbers(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

# 2. Function to Subtract Two Numbers
def subtract_two_numbers(a, b):
    print(f"The difference between {a} and {b} is {a - b}")

# 3. Function to Multiply Two Numbers
def multiply_two_numbers(a, b):
    print(f"The product of {a} and {b} is {a * b}")

# 4. Function to Divide Two Numbers
def divide_two_numbers(a, b):
    if b != 0:
        print(f"The division of {a} by {b} is {a / b}")
    else:
        print("Cannot divide by zero")

# 5. Function to Find the Power of a Number
def power_of_number(base, exponent):
    print(f"{base} raised to the power of {exponent} is {base ** exponent}")


# if Calling the functions with sample arguments
# add_two_numbers(10, 5)
# subtract_two_numbers(10, 5)
# multiply_two_numbers(10, 5)
# divide_two_numbers(10, 5)
# power_of_number(2, 3)



''' 3- Write 5 functions using default value of parameters. '''

# 1. Function to add two numbers
def add_numbers(a = 3 ,b = 4):
    print (a + b)

add_numbers()


# 2. Function to multiply two numbers
def multiply_numbers(num1 = 5, num2 = 93):
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")

multiply_numbers()

# 3. Function to calculate the area of a rectangle
def area_of_rectangle(length = 5, width = 7):
    print (f"area of rectangle is {length * width}")

area_of_rectangle()

# 4. Function to calculate the power of a number
def power(base  = 4, exponent = 3):
    print (base ** exponent)

power()

# 5. Function to concatenate two strings
def concatenate_strings(string1 = "Abdul", string2 = "Raffy"):
    print (string1 + string2)

concatenate_strings()




'''4- Write 5 functions take inputs from user and pass them as arguments to functions'''

# 1. Function to Add Two Numbers
def add_two_numbers(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

# 2. Function to Subtract Two Numbers
def subtract_two_numbers(a, b):
    print(f"The difference between {a} and {b} is {a - b}")

# 3. Function to Multiply Two Numbers
def multiply_two_numbers(a, b):
    print(f"The product of {a} and {b} is {a * b}")

# 4. Function to Divide Two Numbers
def divide_two_numbers(a, b):
    if b != 0:
        print(f"The division of {a} by {b} is {a / b}")
    else:
        print("Cannot divide by zero")

# 5. Function to Find the Power of a Number
def power_of_number(base, exponent):
    print(f"{base} raised to the power of {exponent} is {base ** exponent}")


# Taking inputs from the user and passing them as arguments to the functions
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

add_two_numbers(a, b)
subtract_two_numbers(a, b)
multiply_two_numbers(a, b)
divide_two_numbers(a, b)

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
power_of_number(base, exponent)

# here i combined all the callings tou confuse na hon regards Raffy

