import math
pi = math.pi
class Cube:
    def area(s):
        """computes area of cube """
        return 6*s**2
    def volume(s):
        """evaluates volume of cube """
        return s**3


class Cylinder:
    """deduces area and volume of cylinder"""
    def area(r, h):
        return 2*pi*r(h+r)

    def volume(r, h):
        return pi*h*r**2

class Sphere:
    """counts area and volume of sphere"""
    def area(r):
        return 4*pi*r**2

    def volume(r):
        return math.Cbrt(4*pi*r**3)