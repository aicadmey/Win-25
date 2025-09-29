class Fruit:
    def __init__(self):
        self.quality = None
        self.quantity = None
        self.is_ripe= True

    def ripen(self):
        print("fruits are ripen ")

mango = Fruit()
pineapple = Fruit()


mango.quantity= "2 dozen"
pineapple.quantity = "1 dozen"


print(mango.is_ripe)
print(mango.quantity)
print(pineapple.quantity)


class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.height = None
        self.favourite = None

    def func(self):
        print(" I am busy")


# objects
hamayl = Person()
eesha = Person()

hamayl.age = 99
hamayl.favourite = "black"

hamayl.func()
print(hamayl.age)


class Car():
    def __init__(self):
        self.model = None
        self.year = 2023
        self.color = None

    def condition(self):
        print(" pretty good")


civic = Car()
Honda = Car()
civic.model = '5XBII'
Honda.color = 'black'

print(civic.model)
Honda.condition()


class Cats:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.age = None

    def meow(self):
        print("meow")


kitty = Cats('kitty', 'white')
kitty.age = 5


print(f"name of cat is {kitty.name}")
print(kitty.age)
kitty.meow()


class celestialbody:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def greet(self):
        print(f"greetings from me")


sun = celestialbody('sun', 'huge')
print(sun.name)
sun.greet()
Earth = celestialbody("earth", "small")
print(Earth.mass)


class Student():
    def __init__(self):
        self.marks = None
        self.field = None
        self.age = 19

    def hobby(self):
        return


stu_1 = Student()
stu_2 = Student()
stu_1.marks = 79
stu_1.field = "IT"
stu_2.marks = 94
stu_2.field = "AI"

print(f"marks of 1st student are: {stu_1.marks}")

print(f"marks of 2nd student are: {stu_2.marks}")


class Website:
    def __init__(self):
        self.name = None
        self.type = None
        self.traffic = None
        self.url = "/http:dfh/dfg/.com"

    def load_page(self):
        print("page is loading ...PLZ WAIT")


facebook = Website()
instagram = Website()
facebook.type = "social media"
facebook.name = "Facebook"
instagram.name = "Instagram"

facebook.load_page()
print(instagram.name)


class Game:
    def __init__(self):
        self.playerNo = 2
        self.name = None
        self.difficulty = None

    def check_win(self):
        print("you WON")


chess = Game()  # objects
ludo = Game()

ludo.name = 'ludo'
ludo.difficulty = 'medium'

print(ludo.playerNo)
chess.check_win()


class Shape:
    def __init__(self):
        self.color = None
        self.name = None
        self .area = "2cm per square"

    def calculate_area(self):
        print("find area of the shape : ")

circle = Shape()
rectangle = Shape()

circle.color = "red"
circle.name = "circle"
rectangle.color = "Blue"

print(circle.color)
print(circle.name)
rectangle.calculate_area()



