import math
class Physics:
    def kinetic_energy(m, v):
        """finds out kinetic energy of objects"""
        return math.sqrt(m*v**2)

    def potential_energy(m, g, h):
        """finds out potential energy of objects"""
        g = 10
        return m*g*h
    def density(m, V):
        """finds out density of objects"""
        return m/V