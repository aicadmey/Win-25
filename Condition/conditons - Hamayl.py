if 0 != 0:
    print(False)
else:
    print(True)

price = int(input("enter PRICE of article"))
if price >= 7000:
    print("your discount is 25%")
else:
    print("discount is 10%")


a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
if a > b:
    print("a is greater")
elif a < b:
    print("b is greater")
else:
    print("they are equal")

if 100 > 28:
    print(True)
else:
    print(False)

score = 89
if score >= 90:
    print("GRADE: A+")
elif score >= 80:
    print("GRADE: B+")
elif score >= 70:
    print("GRADE: C")
elif score >= 60:
    print("GRADE: D")
elif score >= 50:
    print("GRADE: E")
else:
    print("fail")

x = int(input("enter a number: "))
if x > 0:
    print("positive number")
elif x < 0:
    print("negative number")
else:
    print("number is 0")

age = int(input("enter a number: "))
if age > 18:
    print("adult")
elif age < 18:
    print("minor")
else:
    print("alien")

p = int(input("enter a number: "))
q = int(input("enter 2nd number: "))
r = input("enter + _ * / ")

if r == '+':
    print(p + q )
elif r == '-':
    print(p - q)
elif r == '*':
    print(p * q)
elif r == '/':
    print(p / q)

z = int(input("enter a number: "))
if z > 40:
    print("try again")
else:
    print("Pass")
num = int(input("enter a number: "))


if num % 2 == 0:
    print("even number")
else:
    print("odd number")

price = int(input("enter PRICE of article"))
if price >= 7000:
    print("your discount is 25%")
else:
    print("discount is 10%")
