import matplotlib.pyplot as plt
import numpy as np


# Define a class for celestial bodies
class CelestialBody:
    def __init__(self, name, distance, radius, color, orbital_speed):
        self.name = name
        self.distance = distance  # Distance from the Sun (in AU)
        self.radius = radius  # Not used in visualization but can be displayed
        self.color = color
        self.orbital_speed = orbital_speed  # Degrees per day
        self.angle = 0  # Initial angle

    def update_position(self, time):
        # Update the angle based on orbital speed and time
        self.angle += self.orbital_speed * time
        self.angle %= 360  # Keep the angle within 0-360 degrees

    def get_position(self):
        # Calculate x, y positions
        x = self.distance * np.cos(np.radians(self.angle))
        y = self.distance * np.sin(np.radians(self.angle))
        return x, y


# Create a SolarSystem class
class SolarSystem:
    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def simulate(self, duration, time_step):
        plt.figure(figsize=(12, 12))
        plt.style.use("dark_background")

        for time in range(0, duration, time_step):
            plt.clf()  # Clear the plot for the next frame
            plt.title("Solar System Simulator", fontsize=16)
            plt.xlabel("X (AU)")
            plt.ylabel("Y (AU)")
            plt.xlim(-2, 2)
            plt.ylim(-2, 2)

            # Plot the Sun
            plt.scatter(0, 0, color="yellow", s=300, label="Sun")

            # Update and plot each celestial body
            for body in self.bodies:
                body.update_position(time_step)
                x, y = body.get_position()
                plt.scatter(x, y, color=body.color, s=50, label=body.name)
                plt.plot([0, x], [0, y], color=body.color, linestyle="--",
                         linewidth=0.5)  # Line to Sun

            plt.legend()
            plt.pause(0.1)  # Pause for animation

        plt.show()


# Initialize the Solar System
solar_system = SolarSystem()

# Add celestial bodies
solar_system.add_body(CelestialBody("Mercury", 0.39, 2439,
                                    "gray", 4.15))
solar_system.add_body(CelestialBody("Venus", 0.72, 6051,
                                    "orange", 1.62))
solar_system.add_body(CelestialBody("Earth", 1.0, 6371,
                                    "blue", 1.0))
solar_system.add_body(CelestialBody("Mars", 1.52, 3389,
                                    "red", 0.53))
solar_system.add_body(CelestialBody("Jupiter", 1.62, 69911,
                                    "cyan", 0.083))
solar_system.add_body(CelestialBody("Saturn", 1.72, 58232,
                                    "Yellow", 0.033))
solar_system.add_body(CelestialBody("Uranus", 1.82, 25362,
                                    "violet", 0.011))
solar_system.add_body(CelestialBody("Neptune", 1.94, 24622,
                                    "indigo", 0.006))

# Simulate the solar system for 365 days with a time step of 10 days
solar_system.simulate(duration=365, time_step=5)
