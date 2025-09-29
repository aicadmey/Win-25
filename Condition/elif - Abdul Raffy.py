#  10 examples for elif

# Example 1
x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")

# Example 2
color = "blue"
if color == "red":
    print("The color is red")
elif color == "blue":
    print("The color is blue")

# Example 3
age = 18
if age < 18:
    print("Underage")
elif age == 18:
    print("Exactly 18 years old")

# Example 4
score = 80
if score > 90:
    print("Grade: A")
elif score > 75:
    print("Grade: B")

# Example 5
day = "Tuesday"
if day == "Monday":
    print("It's Monday")
elif day == "Tuesday":
    print("It's Tuesday")

# Example 6
temperature = 30
if temperature > 35:
    print("It's hot")
elif 20 < temperature <= 35:
    print("It's warm")

# Example 7
marks = 40
if marks >= 75:
    print("Excellent")
elif 50 <= marks < 75:
    print("Pass")

# Example 8
speed = 70
if speed > 80:
    print("Over-speeding")
elif  speed < 80:
    print("Safe speed")

# Example 9
grade = input("Enter your grade A or B: ")
if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good")

# Example 10
number = 15
if number % 2 == 0:
    print("Even number")
elif number % 2 == 1:
    print("Odd number")
