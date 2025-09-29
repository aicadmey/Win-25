# == operator

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
if a == b:
    print("they are equal")
else:
    print("they are not equal")

x = int(input("enter a number: "))
y = int(input("enter 2nd number: "))
if x == y:
    print("they are equal")
else:
    print("they are not equal")

if 7 == 0:
    print("they are equal")
else:
    print("they are not equal")

if 2 == 2:
    print("they are equal")
else:
    print("they are not equal")

p = int(input("enter a number: "))
q = int(input("enter 2nd number: "))
if p == q:
    print("they are equal")
else:
    print("they are not equal")

# !=

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
if a != b:
    print("they are not  equal")
else:
    print("they are equal")

x = int(input("enter a number: "))
y = int(input("enter 2nd number: "))
if x != y:
    print("they are  not equal")
else:
    print("they are equal")

if 7 != 0:
    print("they are not equal")
else:
    print("they are equal")

if 2 != 2:
    print("they are not equal")
else:
    print("they are equal")

p = int(input("enter a number: "))
q = int(input("enter 2nd number: "))
if p != q:
    print("they are not equal")
else:
    print("they are equal")

#  >=
a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))

print(a >= b)

x = int(input("enter a number: "))
y = int(input("enter 2nd number: "))

print(x >= y)

p = int(input("enter a number: "))
q = int(input("enter 2nd number: "))

print(p >= q)

s = int(input("enter a number: "))
t = int(input("enter 2nd number: "))

print(s >= t)

print(8 >= 2)

# <=
print(9 >= 6)
print(99 >= 634)
print(10 >= 70)
print(45 >= 6)
print(89 >= 900)

# >
print(9 > 5)
print(2 > 59)
print(23 > 90)
print(876 > 900)
print(77 > 52)

# <
print(9 < 5)
print(2 < 59)
print(23 < 90)
print(876 < 900)
print(77 < 52)

# AND

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(a > b and a > 40)

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(b < a and a >= 40)

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(a > b and a > 40)

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(b > a and b > 40)

x = int(input("enter a number: "))
y = int(input("enter 2nd number: "))
print(x > y and x > 40)

p = int(input("enter a number: "))
q = int(input("enter 2nd number: "))
print(p > q and x > 40)

# NOT
a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(not (a > b and a > 100))

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(not (b < a and a >= 100))

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(not (a > b and a > 40))

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(not (b > a and b > 40))

x = int(input("enter a number: "))
y = int(input("enter 2nd number: "))
print(not (x > y and x > 40))

p = int(input("enter a number: "))
q = int(input("enter 2nd number: "))
print(not (p > q and x > 40))

# 0R

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(a > b and a > 1)

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(b < a or a >= 24)

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(a > b or a > 1)

a = int(input("enter a number: "))
b = int(input("enter 2nd number: "))
print(b > a or b > 5)

x = int(input("enter a number: "))
y = int(input("enter 2nd number: "))
print(x > y or x > 40)

p = int(input("enter a number: "))
q = int(input("enter 2nd number: "))
print(p > q or x > 9)