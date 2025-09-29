# simple Inheritance
class Vehicle:
    def __init__(self):
        self.model = None
        self.year = None

    def speed(self):
        print("high speed")


class Car(Vehicle):
    pass


honda = Car()
honda.speed()


class Human:
    def __init__(self):
        self.name = None
        self.age = 77


class Student(Human):
    def marks(self):
        print("good")


class Teacher(Human):
    def scale(self):
        print("16 scale")


hamayl = Teacher()
hamayl.name = "hamayl"
print(hamayl.name)
hamayl.scale()





# polymorphism

class Animal:
    def __init__(self, name):
        self.name = name
        self.color = None

    def speak(self):
        print("animal sounds ")


class Dog(Animal):
    def speak(self):  # method overriding
        print(f"{self.name} barks!")


class Cat(Animal):
    def speak(self):  # method overriding
        print(f"{self.name} meow meow!")


# Create an instance of the Dog class
dog = Dog("TOM ")
dog.speak()
cat = Cat("Kitty")
cat.speak()


# Example NO.2
class Vehicle:
    def __init__(self):
        self.name = None
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def start(self):
        print("Car engine started.")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle engine started.")

civic = Car()
civic.name = 'civic'
civic.start()

# encapsulation
class Bank:
    def __init__(self):
        self.__account_number = None  # Private attribute
        self.__balance = None

    def deposit(self):
        print(" deposited!! ")

class HBL(Bank):
    def get_balance(self):
        return self.__balance

hbl = HBL()
hbl.__balance = 123456
print(hbl.__balance)
hbl.deposit()

# Example NO.2

class Employee:
    def __init__(self):
        self.name = None     # public
        self.__salary = None  # private


manager = Employee()
manager.name = "Nimra"
manager.__salary = 800000
print(manager.__salary)
