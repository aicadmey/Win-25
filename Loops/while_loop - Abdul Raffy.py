# Write 10 examples of While loop.

# 1. Any Multiplication Table
Number = int(input("enter your nmuber for table: "))
i = 1

while i <= 10:
    print(Number,"X", i, "=", Number * i )
    i +=1


# 2. Print Even Numbers
print("Print Even Numbers")
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
    

# 3. Sum of First N Natural Numbers
print("Sum of First N Natural Numbers")
N = int(input("Enter a number: "))
i = 1
sum = 0
while i <= N:
    sum += i
    i += 1
print("Sum of first", N, "numbers is:", sum)
print("\n")


# 4. Reverse Countdown
print("Reverse Countdown")
i = 10
while i > 0:
    print(i)
    i -= 1
print("Blast off!\n")


# 5. Factorial of a Number
print("Factorial of a Number")

N = int(input("Enter a number to find factorial: "))
i = 1
factorial = 1
while i <= N:
    factorial *= i
    i += 1
print("Factorial of", N, "is:", factorial)
print("\n")


# 6. Count Digits of a number

num = int(input("Enter a number: "))
count = 0

while num != 0:
    num = num // 10
    count += 1

print("Number of digits:", count)



# 7. Print Multiples of a Number
print("Print Multiples of a Number")
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num * i)
    i += 1
print("\n")

# 8. Print even numbers
print("print odd nmubers")
i = 1
while i <= 20:
    print(i)
    i += 2 


# 9. Grade
score = int(input("Enter the score (0-100): "))

while score >= 0 and score <= 100:
    if score >= 90:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    else:
        print("Grade: F")
    
    score = int(input("Enter the score (0-100): "))



# 10. Guess the Secret Number
print(" Guess the Secret Number")
secret = 7
guess = -1
while guess != secret:
    guess = int(input("Guess the secret number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
print("\n")
