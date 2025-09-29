#loops 
# while loop
#Example1:
i = 1
while i < 5 :
    print(i)
    i = i+ 1
#Example2:   
num = int(input("Enter the number: "))
i = 1
while i < num :
    print(i)
    i = i+ 1
#Example3:   
num = int(input("Enter the number: "))
i = 0
sum = 0
while i < num :
    sum = sum +i
    i = i+ 1  
print(sum)  

#Example4:
num = int(input("Enter the number: "))
product = 1
i = 1

while i <= num:
    product = product * i
    i += 1
print(product)
#Example5:
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old!") 
#Example6:
food = input("Enter a food you like(q to quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter another food you like(q to quit): ")

print("bye")
#Example7:
num = int(input("Enter a # between  1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # 1 - 10: "))

print(f"Your number is {num}")
#Example8:
name = input("Enter your name: ")

while not len(name) == 5:
    print("Write alphabet less then 12")
    name = input("Enter your name: ")

print(f"The username is{name}" )
#Example9:
num = int(input("Enter your integer: "))

while num % 2 == 0 :
    print("The integer is even")
    num = input("Enter your integer: ")

print("The integer is odd" )
#Example10:
i = 10

while i>= 1:
    print(i)
    i -= 1