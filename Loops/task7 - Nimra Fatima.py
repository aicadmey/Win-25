# For loop 
#Example1:
for i in range(5):
    print(i)
#Example2:
for i in range(1,11):
    print(i)
#Example3:
for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)
#Example4:        
num = int(input("Enter your range: "))
 
for i in range(num):
    print(i)
#Example5: 
languages = [ 'R', 'Python', 'Scala', 'Java']

for index in range(len(languages)):
    print("Current language:", languages[index])
#Example6:
for i in range(5):
    print("Thank you")
#Example7:
import time

my_time = int(input("Enter the time in seconds: "))
for x in range( my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}.{minutes:02}.{seconds:02}")
    time.sleep(1)
print("TIME'S UP!")
#Example8:
for i in range(5):
    print("Pizza")
#Example9:
fruits = ["apple", "banana","cherry"]

for fruit in fruits:
    print(fruit)
#Example10:
name = "John Doe"
for char in name:
     print(char)




# nested loop
#Example1:
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for x in range(columns):
      print(symbol, end="")
    print()
#Example2:
for i in range(4):
    print("Fastfood")
    j = 1
    while j<5:
        print("Pizza")
        j = j +1
#Example3:
num = 2

while num < 5 :
    while num % 2 == 0:
        print("The num  " + str(num)+ " is even")
        num = num + 1
#Example4:
for i in range(6):
    print("Hello")
    for j in range(3):
        print("Hey")
#Example5:
for number in range(3):
    print("-------------")
    print("Outer loop")
    for another_number in range(5):
        print("**************")
        print("inner loop iteration" + str(another_number))
#Example6:
for i in range(1,3):
    for j in range(1,4):
        print( i * j)
#Example7:
num1 = int(input("Enter the # of num1: "))
num2 = int(input("Enter the # of num2: "))

for x in range(num1):
    for x in range(num2):
      print(num1 * num2)
    print()
#Example8:
for x in range(3):
    print("----------")
    for y in range(1):
        print("name")
        print("age")
        print("gender")
#Example9:
for i in range(3):
    for j in range(3):
        print(i,j)
# Example10:
for i in range(4):
    for j in range(4):
        print(f"({i},{j})" , end = "\t")
        print()