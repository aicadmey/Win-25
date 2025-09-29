# For loop 10 examples
# in programs mn i have used "f string" yai string latest python mn use hoti hai aur print mn it is more convinient

# 1. Multiplication Table
number = int(input("Enter your number for the table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
print("\n")

# 2. Print Even Numbers
print("Print Even Numbers:")
for i in range(2, 21, 2):
    print(i)
print("\n")

# 3. Sum of First N Natural Numbers
N = int(input("Enter a number: "))
sum = 0
for i in range(1, N + 1):
    sum += i
print(f"Sum of first {N} numbers is: {sum}")
print("\n")

# 4. Reverse Countdown
print("Reverse Countdown:")
for i in range(10, 0, -1):
    print(i)
print("Blast off!\n")

# 5. Factorial of a Number
N = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1, N + 1):
    factorial *= i
print(f"Factorial of {N} is: {factorial}")
print("\n")

# 6. Count Digits of a Number
num = int(input("Enter a number: "))
count = 0
for digit in str(num):
    count += 1
print(f"Number of digits: {count}")
print("\n")

# 7. Print Multiples of a Number
num = int(input("Enter a number: "))
print("Multiples of the number:")
for i in range(1, 11):
    print(num * i)
print("\n")

# 8. Print Odd Numbers
print("Print Odd Numbers:")
for i in range(1, 21, 2):
    print(i)
print("\n")

# 9. Grade Calculation
scores = [90, 75, 65, 45, 80]  # Example scores
for score in scores:
    if score >= 90:
        print(f"Score: {score} - Grade: A")
    elif score >= 70:
        print(f"Score: {score} - Grade: B")
    elif score >= 50:
        print(f"Score: {score} - Grade: C")
    else:
        print(f"Score: {score} - Grade: F")
print("\n")

# 10. Guess the Secret Number
secret = 7
print("Guess the Secret Number (1-10):")
for _ in range(100):  
    guess = int(input("Enter your guess: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
        break
print("\n")
