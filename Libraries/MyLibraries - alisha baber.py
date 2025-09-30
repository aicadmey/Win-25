# Shape library

import math

def rectangle_area(length,width):
    return length * width

def rectangle_parimeter(length,width):
    return 2 * (length + width)

def circle_circumference(radius):
        return 2 * math.pi * radius




# human library

def introduce(name,age):
         return f"Hi, I'm {name}. I'm {age} years old."

def bmi(weight,height):
        # Body Mass Index = weight (kg) / height^2 (m^2)
        return round(weight / (height ** 2), 2)

def is_adult(age):
        return age >= 18



# string libray
def lowercase(string):
       return string.lower()

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
    
def reverse_string(s):
    return s[::-1]


# animal library 
def make_sound(name, sound):
    return f"{name} goes '{sound}!'"

def describe_animal(name, species, sound):
    return f"{name} is a {species} and it says '{sound}'"

def animal_age_in_human_years(age, species):
    return age * 7    



# Science library
def force(mass, acceleration):
    return mass * acceleration     

def energy(mass):
    c = 3e8  # Speed of light in meters/second
    return mass * (c ** 2)      

def area_of_circle(radius):
    
    return math.pi * radius ** 2