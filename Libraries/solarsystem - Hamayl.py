class Solarsystem:

    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass  # in kg
        self.radius = radius  # in meters

    def get_surface_gravity(self):
        G = 6.6743e-11  # Gravitational constant
        return (G * self.mass) / (self.radius ** 2)

    def __str__(self):
        return f"{self.name} (Mass: {self.mass:.2e} kg, Radius: {self.radius:.2e} m)"


# library no.3

class Earth(Solarsystem):

    def __init__(self, name, mass, radius):
        """Initializes the Earth with its known properties."""
        super().__init__(name, mass, radius)
        self.name = "Earth"
        self.mass = 5.972e24  # kg
        self.radius = 6.371e6  # meters
        self.orbital_period = 365.25  # Earth days
        self.has_moon = "1 moon "
        self.num_continents = 7
        self.average_surface_temperature = 15  # Celsius

    def get_surface_gravity(self):
        G = 6.6743e-11  # Gravitational constant
        return (G * self.mass) / (self.radius ** 2)

    def describe(self):
        description = f"Name: {self.name}\n"
        description += f"Mass: {self.mass:.2e} kg\n"
        description += f"Radius: {self.radius:.2e} m\n"
        description += f"Has a Moon: {self.has_moon}\n"
        description += f"Number of Continents: {self.num_continents}\n"

        return description

    def __str__(self):
        return f"{self.name} (Mass: {self.mass:.2e} kg, Radius: {self.radius:.2e} m)"
