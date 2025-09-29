#function
#program without parameters
#Example1:
def print_msg():
    print("Hello World")
print_msg()
#Example2:
def sport():
    print("Cricket")
sport()
#Example3:
def sum():
    num = 2 + 3
    print(num)
sum()  
#Example4:  
def food():
    print("Briyani")
food()
#Example5:
import random
def random_number():
    num = random.randint(1,100)
    print(num)
random_number()


#program with parameters
#Example1:
def add_numbers(a, b):
    return a+b
result = add_numbers(3, 6)
print(result)
#Example2:
def intro(name, age):
    print(f"My name is {name} and my age is {age}")

intro("nimra", 20)  
# Example3:
def distance(a):
    print(f"The distance between bahawalpur and lodrah is {a}km. ")  

distance(26)
# Example4:
def subtract(a, b):
    return a-b
result = subtract(5, 3)
print(result)
# Example5:
def calculate_area(lenght, width):
    return lenght* width
result = calculate_area(5, 3)
print(result)


#program using default value of parameters
# Example1:
def intro(name, age = 20):
    print(f"My name is {name} and my age is {age}. ")

intro("noor")
intro("john", 27)
# Example2:
def calculate_area(lenght, width = 3):
    return lenght* width
print(calculate_area(5))
print( calculate_area(8, 2))
# Example3:
def msg(x, prefix = "Hello"):
    print(f"{x} {prefix}")
msg("World") 
# Example4:
def sum(a , b = 4):
    return a+b
print(sum(6)) 
print(sum(3, 7)) 
# Example5:
def celsius_to_fahrenheit(celsius = 0):
    return (celsius * 9/5) +32
fahreheit = celsius_to_fahrenheit()
print(fahreheit)
fahreheit = celsius_to_fahrenheit(32)
print(fahreheit)


# program by taking inputs from user as arguments
# Example1:
def sum(num1,num2):
    return num1 + num2
num1 = float(input("Enter the number1: "))
num2 = float(input("Enter the number2: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")
# Example2:
def intro(name, age):
    print(f"My name is {name} and my age is {age}.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
intro(name, age)
# Example3:
def calculate_area(length, width):
    return length* width
   
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
result = length* width
print(f"The area is {result}")
calculate_area(length, width)
# Example4:
def check_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
num = float(input("Enter the number: "))
result = check_even_or_odd(num)
print(f"The number {num} is {result}")
# Example5:
def number_pos_or_neg(num):
    if num > 0:
        return "positive"
    else:
        return "negative"
    
num = float(input("Enter the number: "))
result = number_pos_or_neg(num)
print(f"The number {num} is {result}")