#variable 1

n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("The factorial of ",n ,"is " ,factorial)

 #variable 2

correct_number = 7
while True:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == correct_number:
        print("Congratulations! You guessed it right.")
        break
    else:
        print("Try again!")
    
#variable 3

total = 0
i = 2
while i <= 20:
    total += i
    i += 2
print(total)

#variable 4

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop has finished")

#variable 5
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input == 'exit':
        break
    print("You typed:", user_input)

#variable 6
i = 1
while i <= 5:
    print(i)
    i += 1

#variable 7
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

#variable 8
numbers = [1, 2, 3, 4, 5, 3, 6, 3]
count = 0
i = 0
while i < len(numbers):
    if numbers[i] == 3:
        count += 1
    i += 1
print("The number 3 appears", count, "times.")

#variable 9
i = 1
while i <= 100:
    if i % 7 == 0:
        print("The first number divisible by 7 is:",i)
        break
    i += 1

#variable 10
text = "Hello, world!"
index = 0
while index < len(text):
    print(text[index])
    index += 1
