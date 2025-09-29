# FUNCTIONS without PARAMETERS
def greet():
    print("Assalam-o-Alaikum!")


greet()


def counting():
    for i in range(11):
        print(i, end="")


counting()


def hello():
    print("hello,world! ")


hello()


def sq():
    n = 5
    square = n * n
    print("square = ", square)


sq()


def even():
    for i in range(0, 15, 2):
        print(i)


even()


# FUNCTIONS with 2 PARAMETERS

def add(x, y):
    print("sum= ", x + y)


add(2, 5)


def sub(x, y):
    print("sub= ", x - y)


sub(20, 6)


def mult(x, y):
    print("product = ", x * y)


mult(2, 100)


def div(x, y):
    print("division = ", x / y)


div(2, 100)


def modulus(a, b):
    print("mod = ", a % b)


modulus(89, 5)


# FUNCTIONS with default PARAMETERS

def hello(name='Hamayl'):
    print("hello ", name)


hello("Amna")  # call with argument
hello()  # call without argument


def add(x=100, y=100):
    print("sum= ", x + y)


add()
add(89, 487)


def sq(n=15):
    square = n * n
    print("square = ", square)


sq()
sq(12)


def area(lenght=56, width=21):
    print("area = ", lenght * width)


area()
area(34, 45)


def discount(price=4000):
    print("discount is: 25%")


discount()


# FUNCTIONS with userINPUTS


def add(x, y):
    return x + y


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = add(num1, num2)
print("The sum is:", result)


def greet(name):
    print("hy, ", name)


name = input("Enter your name here: ")
greetings = greet(name)
print(greetings)


def sub(x, y):
    return x - y


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

ans = sub(num1, num2)
print("The sum is:", ans)


def even(x):
    if x % 2 == 0:
        print("even number")
    else:
        print("odd number")


num = int(input("Enter a number: "))
even(num)


def discount(price):
    if price >= 7000:
        print("your discount is 25%")
    else:
        print("discount is 10%")


x = int(input("Enter Price of your article: "))
discount(x)
