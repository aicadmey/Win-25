import theorem
import shapes
import physics
import space
import string_functions

# FROM THEOREM LIBRARY
a = 35
b = 89
c = theorem.Pythagoras.hypotenuse(a, b)
print("Length of hypotenuse of right angle triangle is", c, "m")

c = 23
a = 10
g = theorem.Pythagoras.side1(c, a)
print("length of side1 of right angle triangle is ", g, "m")


# FROM SHAPES LIBRARY
radius = 45
d = shapes.Sphere.area(radius)
print("Area of sphere is", d, "m^2")

side = 15
v = shapes.Cube.volume(side)
print("Volume of cube is", v, "m^3")


# FROM PHYSICS LIBRARY

mass = 12
velocity = 6
potential = physics.Physics.kinetic_energy(mass, velocity)
print("Potential energy of object is ", potential, "J")

mass1 = 66
volume = 9
density = physics.Physics.density(mass1, volume)
print("Density of object is ", density, "kg/m^3")


# FROM SPACE LIBRARY

height = 67
orbitalRadius = space.Space.orbital_radius(height)
print("Orbital radius of object", orbitalRadius, "km")

m = 67
r = 6400
escapeVelocity = space.Space.escape_velocity(m, r)
print("escape velocity of object", escapeVelocity, "km/s")


# FROM STRING_FUNCTION LIBRARY

python = "Python is a programming language used for ML, AI."
k = string_functions.String.to_uppercase(python)
print(k)

x = "Pakistan is our country."
y = string_functions.String.count_vowels(x)
print(y)