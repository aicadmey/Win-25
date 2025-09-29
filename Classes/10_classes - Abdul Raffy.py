#  10 classes with two objects each


class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Phone: {self.brand}, Model: {self.model}"

phone1 = Phone("Apple", "iPhone 14")
phone2 = Phone("Samsung", "Galaxy S22")

print(phone1.display())
print(phone2.display())

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Phone: {self.brand}, Model: {self.model}"

phone1 = Phone("Apple", "iPhone 14")
phone2 = Phone("Samsung", "Galaxy S22")

print(phone1.display())
print(phone2.display())


class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def display(self):
        return f"Animal: {self.species}, Sound: {self.sound}"

animal1 = Animal("Dog", "Bark")
animal2 = Animal("Cat", "Meow")

print(animal1.display())
print(animal2.display())


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        return f"Student: {self.name}, Grade: {self.grade}"

student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

print(student1.display())
print(student2.display())


class Laptop:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

    def display(self):
        return f"Laptop: {self.brand}, Processor: {self.processor}"

laptop1 = Laptop("Dell", "i7")
laptop2 = Laptop("HP", "Ryzen 5")

print(laptop1.display())
print(laptop2.display())


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"Book: '{self.title}' by {self.author}"

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print(book1.display())
print(book2.display())


class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def display(self):
        return f"City: {self.name}, Country: {self.country}"

city1 = City("Lahore", "Pakistan")
city2 = City("Tokyo", "Japan")

print(city1.display())
print(city2.display())


class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def display(self):
        return f"Movie: '{self.title}', Genre: {self.genre}"

movie1 = Movie("Inception", "Sci-Fi")
movie2 = Movie("Titanic", "Romance")

print(movie1.display())
print(movie2.display())


class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        return f"Flower: {self.name}, Color: {self.color}"

flower1 = Flower("Rose", "Red")
flower2 = Flower("Sunflower", "Yellow")

print(flower1.display())
print(flower2.display())


class Planet:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        return f"Planet: {self.name}, Size: {self.size}"

planet1 = Planet("Earth", "Medium")
planet2 = Planet("Jupiter", "Large")

print(planet1.display())
print(planet2.display())
