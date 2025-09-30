import math
import random

# Space Library Functions
def distance_between_planets(planet1_distance, planet2_distance):
    """Calculates the distance between two planets in space."""
    return abs(planet1_distance - planet2_distance)

def spacecraft_speed(time, distance):
    """Estimates the speed of a spacecraft."""
    if time > 0:
        return distance / time
    else:
        return "Time cannot be zero"

# Robotics Library Functions
def move_forward(speed, time):
    """Makes the robot move forward at a given speed and time."""
    distance = speed * time
    return f"Robot moved forward {distance} meters."

def pick_up_object(object_name):
    """Simulates the robot picking up an object."""
    return f"Robot picked up the {object_name}."

# Games Library Functions
def calculate_score(base_score, multiplier):
    """Calculates the final score in a game."""
    return base_score * multiplier

def roll_dice(sides=6):
    """Simulates rolling a dice with a specified number of sides."""
    return random.randint(1, sides)

# Space Explorer Library Functions
def escape_velocity(mass, radius):
    """Calculates the escape velocity of a planet."""
    G = 6.67430e-11  # Gravitational constant
    return math.sqrt((2 * G * mass) / radius)

def travel_time(distance, speed):
    """Estimates the travel time to a destination in space."""
    if speed > 0:
        return distance / speed
    else:
        return "Speed must be greater than zero."

# Robot Control Library Functions
def turn_left(angle):
    """Makes the robot turn left by a given angle."""
    return f"Robot turned left by {angle} degrees."

def stop():
    """Stops the robot."""
    return "Robot stopped."
