

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
name1 = input("Enter your name: ")
age2 = input("Enter how old you are: ")
space = input("Enter what is space: ")
space1 = input("Enter first level of space: ")
space2 = input("Enter second level of space: ")
space3 = input("Enter third level of space: ")


first_name, last_name = input("Enter your first and last name: ").split()
weight = input("Enter your weight in kilograms: ")


patient_name = input("Enter name of patient: ")
hospital_name = input("Enter hospital name" )
school_name = input("Enter school name: ")
project_name = input("What is your project: ")
project_title = input("Enter project title: ")
ward_name = input("Enter ward name: ")
ward_num = input("Enter ward number: ")

assistant_name = input("Enter assistant name: ")
doctor_name = input("Enter doctor name: ")
lab_name = input("Enter lab name: ")
test_name = input("Enter test name: ")

game_name = input("Enter name of game: ")
company_name = input("Enter company name: ")
company_ceo = input("Who is the CEO? ")
company_owner = input("Enter company owner name: ")
hr_name = input("Enter HR name: ")

your_post = input("Enter your post: ")
your_income = input("Enter your income: ")
your_gender = input("Input your gender: ")

# Type casting examples
num = 3.14
str_num = "42"
int_num = int(str_num)
bool_value = True
int_value = int(bool_value)
float_num = 7.89
int_num = int(round(float_num))

num = 42
float_num = float(num)
num = -5
float_num = float(num)
num = 1000000000
float_num = float(num)
num = 7
float_num = float(num + 3.5)
num = 42.7
int_num = int(num)
num = -3.14
int_num = int(num)
num = 100.0
int_num = int(num)
num = 4.7
int_num = int(round(num))
num1 = 5.8
num2 = 2.2
result = int(num1 + num2)
int1 = 5
int2 = 3
result = float(int1 / int2)
num1 = 8
num2 = 3
division_result = float(num1 / num2) 

# Printing collected inputs
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Name1: {name1}")
print(f"Age2: {age2}")
print(f"Space: {space}")
print(f"First level of space: {space1}")
print(f"Second level of space: {space2}")
print(f"Third level of space: {space3}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Weight: {weight}")
print(f"Patient Name: {patient_name}")
print(f"Hospital Name: {hospital_name}")
print(f"School Name: {school_name}")
print(f"Project Name: {project_name}")
print(f"Project Title: {project_title}")
print(f"Ward Name: {ward_name}")
print(f"Ward Number: {ward_num}")
print(f"Assistant Name: {assistant_name}")
print(f"Doctor Name: {doctor_name}")
print(f"Lab Name: {lab_name}")
print(f"Test Name: {test_name}")
print(f"Game Name: {game_name}")
print(f"Company Name: {company_name}")
print(f"Company CEO: {company_ceo}")
print(f"Company Owner: {company_owner}")
print(f"HR Name: {hr_name}")
print(f"Your Post: {your_post}")
print(f"Your Income: {your_income}")
print(f"Your Gender: {your_gender}")

# Printing the results of type casting
print(f"Float {num} as int: {int_num}")
print(f"String '{str_num}' as int: {int_num}")
print(f"Boolean {bool_value} as int: {int_value}")
print(f"Boolean {bool_value} as int: {int_value}")
print(f"Rounded float {float_num} as int: {int_num}")
print(f"Integer {num} as float: {float_num}")
print(f"Integer {num} as float: {float_num}")
print(f"Integer {num} as float: {float_num}")
print(f"Integer {num} with 3.5 added, as float: {float_num}")
print(f"Float {num} as int: {int_num}")
print(f"Float {num} as int: {int_num}")
print(f"Float {num} as int: {int_num}")
print(f"Float {num} rounded to int: {int_num}")
print(f"Sum of {num1} and {num2} as int: {result}")
print(f"String '{str_num}' as int: {int_num}")
print(f"Boolean {bool_value} from comparison (5 > 3) as int: {int_value}")
print(f"Result of division: {result}")
print(f"Result of {num1} divided by {num2}: {division_result}")