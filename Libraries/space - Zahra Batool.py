import math
pi = math.pi
class Space:
    def orbital_radius(h):
        """calculates orbital radius of object like satellites"""
        R = 6400
        return R+h

    def orbital_velocity(r, T):
        """calculates orbital velocity of satellites"""
        return (2*pi*r)/T
    def escape_velocity(M, r):
        """calculates escape velocity of objects """
        G = 6.67*10**(-11)
        return math.sqrt((2*G*M)/r)