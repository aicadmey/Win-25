# class programs
#Example1:
class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello,my name is {self.name} and my age is {self.age} years old.")


# Create two objects of the class
object1 = MyClass("Alice", 30)
object2 = MyClass("Bob",22)

object1.greet()
object2.greet()

#Example2:
class Animals:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def animal(self):
        print(f"The {self.name} are {self.species}" )

# Create two objects of the class
object1 = Animals("Dogs","barking")
object2 = Animals("Cats","Meow Meow")

object1.animal()
object2.animal()

#Example3:
class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return   self.num1 + self.num2
    
# Create two objects of the class
object1 = Calculator(15 , 4)
object2 = Calculator(56 , 34)

print(object1.add()) 
print(object2.add())

#Example4:
class Book:
    def __init__(self,title,auther,publication_year):
        self.title = title
        self.auther = auther
        self.publication_year = publication_year

    def display_info(self):
        print(f"Title:{self.title}")
        print(f"Auther:{self.auther}")    
        print(f"Publication Year:{self.publication_year}") 

# Create two objects of the class
object1 = Book("The lord of the Rings", "J.R.R. Tolkin", 1954)
object2 = Book("Pride and Prejusdice", "Jane Austen", 1813)

object1.display_info()
object2.display_info()

#Example5:
class Cars:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def display(self):
        print(f"I have {self.name} of {self.model} model") 

# Create two objects of the class
object1 = Cars("Honda CR-V", 7)
object2 = Cars("Toyota Camry", 11)  

object1.display()
object2.display()

#Example6:
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self):
       
        print(f"account_number: { self.account_number}. New balance: {self.balance}")

# Create two objects of the class
object1 = BankAccount(12345-87655-876, 100000)
object2 = BankAccount(34567-5432-76654, 6000)  

object1.deposit()
object2.deposit()       

#Example7:
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print(f"Starting the {self.year} {self.make} {self.model}")
    def stop(self):
        print(f"Stoping the {self.year} {self.make} {self.model}")

# Create two objects of the class
object1 = Car("Toyota", "Camry",2020)
object2 = Car("Honda", "Civic", 2019)  

object1.start()
object2.stop()

#Example8:
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_resturant(self):
        print(f"Restaurant Name: {self.name}")
        print(f" Cuisine: {self.cuisine}")

# Create two objects of the class
object1 = Restaurant("Pizza Palance", "Italian")
object2 = Restaurant("Thai Kitchen", "Thai")  

object1.describe_resturant()
object2.describe_resturant() 

#Example9:
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def bark(self):
         print(f"{self.name} says Woof!")   
    def fetch(self):
        print(f"{self.name} is fetching the ball!") 

# Create two objects of the class
object1 = Dog("Buddy", "Golden Retriver", 3)
object2 = Dog("Max", "Labrador",2)  

object1.bark()
object1.fetch()
object2.bark()   
object2.fetch()                

#Example10:
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def study(self):
        print(f"{self.name} is styding hard.")

# Create two objects of the class
object1 = student("Alice", 15, 10)
object2 = student("Max", 14,11)  

object1.study()
object2.study()        