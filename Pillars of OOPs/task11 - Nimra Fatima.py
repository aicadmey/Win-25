#Inheritance Peogram
#Example1:
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("Vehicle is moving")

    def get_info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  
        self.doors = doors

    def move(self):
        print("Car is driving")

    def get_info(self): 
        return f"{super().get_info()}, {self.doors} doors"

my_car = Car("Toyota", "Camry", 4)
my_car.move()
print(my_car.get_info())  

#Example2:
class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color) 
        self.length = length
        self.width = width

    def area(self):  
        return self.length * self.width

# Create object
my_rectangle = Rectangle("blue", 5, 10)

# Demonstrate methods
print(f"Rectangle color: {my_rectangle.get_color()}") 
print(f"Rectangle area: {my_rectangle.area()}")



# Encapsulation program
#example1:
class Counter:
    def __init__(self):
        self._value = 0  

    def increment(self):
        self._value += 1

    def get_value(self):
        return self._value

# Example usage
my_counter = Counter()
my_counter.increment()
my_counter.increment()
my_counter.increment()
print(my_counter.get_value())  

my_counter._value = 11  
print(my_counter.get_value())  

#Example2:
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age    

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        if 0 <= new_age <= 120:  
            self.age = new_age
        else:
            print("Invalid age.")

#For Example 
person1 = Person("Nimra", 20)

print(f"Name: {person1.get_name()}")  
print(f"Age: {person1.get_age()}")    

person1.set_age(140)
print(f"Age: {person1.get_age()}")    

# Ploymorphism program
#Example1:
class Animal:
    def make_sound(self):
        print("Generic animal sounds")

class dog(Animal):
    def make_sound(self):  
        print("Woof!")

class cat(Animal):
    def make_sound(self):  
        print("Meow!")

my_animal = Animal()
my_dog = dog()
my_cat = cat()

my_animal.make_sound()  
my_dog.make_sound()     
my_cat.make_sound()     

#Polymorphism in action with a loop
animals = [my_animal, my_dog, my_cat]
for animal in animals:
    animal.make_sound()

#Example2:
class Shape:
    def draw(self):
        print("Drawing a generic shape")

class Circle(Shape):
    def draw(self):  
        print("Drawing a circle")

class Square(Shape):
    def draw(self):  
        print("Drawing a square")


shapes = [Circle(), Square()]


for shape in shapes:
    shape.draw()

