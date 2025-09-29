#conditions
#if
#Example1:
age = int(input("Enter your age: "))
if age > 18:
    print("You are adult")
#Example2:
Marks = int(input("Enter your marks: "))
if Marks > 60:
    print("You are pass")
#Example3:
age = int(input("Enter your age: "))
if age < 18:
    print("Discount") 
#Example4:
size = int(input("Enter the size of shoes: ")) 
if size <20:
    print("These are childern's shoes: ")       
#Example5: 
number =  input("Enter the num1: ") 
if number > 0 :
    print("Positive number") 
#Example6:
username = input("Enter a username: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters") 
#Example7:  
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("The number is even")
#Example8:
price = int(input("Enter the price of the pizza: "))
if price > 1000:
    print("You order large pizza! ")
#Example9:
size = int(input("Enter the size of pant: ")) 
if size <20:
    print("These are childern's pant: ")   
#Example10:
age = int(input("Enter your age: "))
if age < 18:
    print("You are student")


#else
#Example1:
age = int(input("Enter your age: "))
if age > 18:
    print("You are adult")
else:
    print("You are not adult")
#Example2:
Marks = int(input("Enter your marks: "))
if Marks > 60:
    print("You are pass")
else :
    print("You are fail")    
#Example3:
age = int(input("Enter your age: "))
if age < 18:
    print("Discount") 
else:
    print("No Discount")
#Example4:
size = int(input("Enter the size of shoes: ")) 
if size <20:
    print("These are childern's shoes: ")  
else :
    print("Thses are adult's shoes")     
#Example5: 
number =  input("Enter the num1: ") 
if number > 0 :
    print("Positive number") 
else:
    print("Negative number")
#Example6:
username = input("Enter a username: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters") 
else:
    print(f"Welcome {username}")
#Example7:  
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#Example8:
price = int(input("Enter the price of the pizza: "))
if price > 1000:
    print("You order large size pizza! ")
else:
    print("You order medium size pizza")    
#Example9:
size = int(input("Enter the size of pant: ")) 
if size <20:
    print("These are childern's pant: ")  
else:
    print("These are adult's size pants") 
#Example10:
age = int(input("Enter your age: "))
if age < 18:
    print("You are student") 
else:
    print("You are not student")  


#if elif else
#Example1:
age = int(input("Enter your age: "))
if age < 18:
    print("You are not adult")
elif age>18:
    print("You are  adult")
else:
    print("You die")
#Example2:
Marks = int(input("Enter your marks: "))
if Marks > 60:
    print("You have good numbers")
elif Marks == 50:
    print("You have average numbers")
else :
    print("You are fail")    
#Example3:
age = int(input("Enter your age: "))
if age < 18:
    print("Discount") 
elif age <30:
    print("10% Discount")
else:
    print("No Discount")
#Example4:
size = int(input("Enter the size of shoes: ")) 
if size <20:
    print("These are childern's shoes: ")  
elif size >30:
     print("Thses are adult's shoes")
else :
    print("Thses are for old's man shoes")     
#Example5: 
number =  input("Enter the num1: ") 
if number > 0 :
    print("Positive number") 
elif number < 0:
    print("Negative number")
else:
    print("zero")
#Example6:
username = input("Enter a username: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters") 
elif not username.isalpha():
    print("username can't contain integers")
else:
    print(f"Welcome {username}")
#Example7:  
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#Example8:
price = int(input("Enter the price of the pizza: "))
if price > 1000:
    print("You order large size pizza! ")
elif price ==900:
    print("You order medium size pizza")  
else:
    print("You order small size pizza")    
#Example9:
size = int(input("Enter the size of pant: ")) 
if size <20:
    print("These are childern's pants: ")  
elif size <30:
     print("Thses are adult's pants")
else :
    print("Thses are for old's man pants")  
#Example10:
age = int(input("Enter your age: "))
if age < 18:
    print("You are student") 
elif age <40:
    print("You are employee")
else:
    print("You are not student") 