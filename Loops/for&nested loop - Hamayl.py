                             # FOR LOOP

for i in range(3):
    print("I AM BUSY")

for number in range( 5, 15):
    print(number)


for i in range (6): #0 to 5
    print(i)

name = input("write your name:  ")  # name
for i in name:
    print(i)

for i in range(10):   # even numbers
    if i % 2 == 0:
        print(i)

color =  "black"
for i in color:
    print(i)

for i in range(2,20):  # odd numbers
    if i%2 != 0:
        print(i)

for i in range (0 ,30,3):  # 0 to  30 with jumps of 3
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for number in range( 5, 15):
    print(number)


                     #  nested loop

for i in range(2):
    for j in range(5):
        print("hy there ,its Hamayl")


for i in range(1, 3):
    for j in range(1, 3):
        print(i*j,)
    print()


for i in range(2):
    for j in range(3):
        print("/", end=" ")
    print(" ")


for i in range(2):
    for j in range(5):
        if j% 2 == 0:
            print(j)
    print(0)


for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()


for i in range(2):
    for j in range(0,5,2):
        print("##" ,end=" " )


for i in range(3):
    for j in range(2):
        print (i ,j ,end=" ")


for i in range(1, 6):
    for j in range(1, 6):
        if j > i:
            print(j, end=" ")
    print()


for i in range(3):
    for j in range(3):
        print(i + j ,end=" ")
    print(" ")


for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print(" ")

