import organism
import calculator
import solarsystem
from solarsystem import Earth
import shapes


class Student:
    def __init__(self, marks):
        self.name = "hamayl"
        self.marks = marks
        self.organism = organism.Organism("hamayl", "animalia")


# organism library used
hamayl = Student(98, )
var = hamayl.organism.alive
print(var)

v1 = hamayl.organism.kingdom
print(v1)

# calculator library used
my_calculator = calculator.Calculator(hamayl.marks)
my_calculator.add(2)

my_calculator.multiply(1.1)

print(f"{hamayl.name}'s final marks: {hamayl.marks}")


class Moon:
    def __init__(self):
        self.location = None
        self.numbers = None
        self.solarsystem = solarsystem.Solarsystem("moon", 7.34767309, 1733)
        self.earth = Earth("Earth", 5.972e24, 6.371e6)
        self.shape = shapes.Circle(3456)


moon = Moon()
var1 = moon.solarsystem  # solarsystem library used
var2 = moon.solarsystem.get_surface_gravity()
print(var1)
print(var2)


var3 = moon.earth.mass  # Earth library used
var4 = moon.earth.has_moon
print(var3)
print(var4)

var5 = moon.shape  # shapes library
var6 = moon.shape.perimeter()
print(var5)
print(var6)
