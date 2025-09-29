class Student:
    def __init__(self):
        self.name = None
        self.marks = None

    class TopStudent:

        def __init__(self):
            self.position = None
            self.marks = None


hamayl = Student.TopStudent()
hamayl.marks = 99
print(hamayl.position)
print(hamayl.marks)



# 2 classes



class Fruits:
    def __init__(self):
        self.name = None
        self.quantity = None

    def eat(self):
        print("they were yummy ,so we finished them")

    class citrusfruit:
        def __init__(self):
            self.name = None
            self.quantity = None

    class Sweetfruit:
        def is_ripen(self):
            print("sweet fruits are ripen ")


class Vegetable:
    def __init__(self):
        self.name = None
        self.quantity = 12

    class GreenVeg:
        def __init__(self):
            self.name = None
            self.isripen = True

    class RootVeg:
        def is_ripen(self):
            print("yes")


apple = Fruits.citrusfruit()
tomato = Vegetable.GreenVeg
apple.name = "apple"
apple.quantity = "1 dozen"

print(apple.quantity)



# 3 classes



class Vehicle:
    def __init__(self):
        self.model = "xfy5"
        self.year = None

    class Car:
        def __init__(self):
            self.model = None
            self.year = None

    class Motocycle:
        def working(self):
            print("working properly")

    class Airplane:
        def __init__(self):
            self.model = "xfy5"
            self.year = None


def fun():
    print("mobile func")


class Device:
    def __init__(self):
        self.name = None
        self.model = None

    class Mobile:
        def __init__(self):
            self.name = None


    class Computer:
        def __init__(self):
            self.name = None
            self.model = None

    class Notebook:
        def __init__(self):
            self.name = None
            self.model = None

class Building:
    def __init__(self,):
        self.location = None
        self.price = "1 lac"

    class Industrial:
        def __init__(self, ):
            self.location = None
            self.price = "1 lac"

    class Commercial:
        def __init__(self, ):
            self.location = None
            self.price = "5 lac"

    class Residential :

        def __init__(self, ):
            self.location = None
            self.price = "7 lac"


honda = Vehicle.Car()
honda.model = 2022
print(honda.year)

iphone = Device
iphone.name = "iphone 16"
print(iphone.name)

autoshop = Building.Commercial()
print(autoshop.price)


# 4 classes



class Ocean:
    def __init__(self):
        self.name = None
        self.location= None

    class Arctic:
        def __init__(self):
            self.name = None
            self.location = None

    class Pacific:
        def __init__(self):
            self.name = None
            self.location = None

    class Atlantic:
        def fun1(self):
            print("atlantic fun")

    class Indian:
        def fun2(self):
            print(" Indian fun")

class Weather:
    def __init__(self):
        self.location = "bwp"
        self.condition = None

    class Sunny:
        def __init__(self):
            self.location = "bwp"
            self.condition = None

    class Rainy:
        def __init__(self):
            self.location = "LHR"

    class Snowy:
        def __init__(self):
            self.location = "Muree"
            self.condition = None

    class Cloudy:
        def __init__(self):
            self.location = "haroonabd"

class Bio:
    def __init__(self):
        self.field = None
        self.kingdom = None

    class Zoology:
        def __init__(self):
            self.field = "Zoology"
            self.kingdom = None

    class Botany:
        def botfun(self):
            print("subclass of bio")

    class Mamalia:
        def __init__(self):
            self.field = "Mamals"
            self.kingdom = None

    class Humans:
        def __init__(self):
            self.species = "Homo sapiens"


class Iub:
    def __init__(self):
        self.name = None
        self.location = None

    class Ai:
        def __init__(self):
            self.sems = 4
            self.section = "M2"

    class IT:
        def __init__(self):
            self.sems = None
            self.section = None

    class Biotechnology:
        def __init__(self):
            self.sems = None
            self.section = None

    class Physics:
        def study(self):
            print("phy func")


asma = Iub.Biotechnology()
asma.sems = 4
hamayl = Bio.Humans()
rain = Weather.Rainy()
atlantic = Ocean.Atlantic()
print(atlantic.fun1())
print(rain.location)
print(hamayl.species)
print(asma.sems)



# 5 classes



class Shape:
    def __init__(self):
        self.color = None
        self.area = "2m per sq"

    class circle:
        def __init__(self):
            self.color = None

    class Rectangle:
        def recfun(self):
            print("subclass of shape")

    class Triangle:
        def __init__(self):
            self.color = None

    class Square:
        def __init__(self):
            self.color = None

    class Oval:
        def ovalfun(self):
            print("subclass of shape")

class Color:
    def __init__(self):
        self.name = None
    class Black:
        def fav(self):
            print("fav color ")
    class Red:
        def fav2(self):
            print("hy ,i am red ")

    class Blue:
        def fav3(self):
            print("hy ,i am blue ")

    class White:
        def fav4(self):
            print("hy ,i am white ")

    class Orange:
        def fav5(self):
            print("hy ,i am orange ")


class Country:
    def __init__(self):
        self.name = None
        self.population = None

    class Usa:
        def __init__(self):
            self.name = "USA"
            self.population = None

    class korea:
        def __init__(self):
            self.name = "Korea"
            self.population = None

    class Saudia:
        def __init__(self):
            self.name = "saudia"
            self.population = None

    class Thailand:
        def __init__(self):
            self.name = "THAI LAND"
            self.population = None

    class Canada:
        def __init__(self):
            self.name = "Canada"
            self.population = None

class Sport:
    def __init__(self):
        self.name = None
        self.player = None

    class Cricket:
        def __init__(self):
            self.name = None
            self.player = None

        def win(self):
            print("Pak Won")

    class Football:
        def __init__(self):
            self.name = None
            self.player = None

    class Tennis:
        def __init__(self):
            self.name = None
            self.player = None

    class Swimming:
        def __init__(self):
            self.name = None
            self.player = None

    class Basketball:
        def __init__(self):
            self.name = None
            self.player = None

class Planets:
    def __init__(self):
        self.name = None

    class Earth:
        def subfunc1(self):
            print("planet subclass earth")

    class Mars:
        def subfunc2(self):
            print("planet subclass MARS")

    class Jupiter:
        def subfunc3(self):
            print("planet subclass Jupiter")

    class Sun:
        def subfunc4(self):
            print("planet subclass sun")

    class Venus:
        def subfunc(self):
            print("planet subclass VENUS")





aliens = Planets.Mars()
babar = Sport.Cricket()
seoul = Country.korea()
shirt = Color.White()
egg = Shape.Oval()
print(egg.ovalfun())
print(shirt.fav4())
print(seoul.name)
print(babar.win())
print(aliens.subfunc2())
