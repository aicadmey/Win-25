import math


class Pythagoras:
    @staticmethod
    def hypotenuse(a, b):
        """Calculate hypotenuse length using the Pythagorean theorem."""
        return math.sqrt(a ** 2 + b ** 2)

    @staticmethod
    def side1(c, a):
        """Calculate side b length using the Pythagorean theorem given hypotenuse c and side a."""
        if c <= a:
            raise ValueError("Hypotenuse must be greater than side a.")
        return math.sqrt(c ** 2 - a ** 2)

    @staticmethod
    def side2(c, b):
        """Calculate side a length using the Pythagorean theorem given hypotenuse c and side b."""
        if c <= b:
            raise ValueError("Hypotenuse must be greater than side b.")
        return math.sqrt(c ** 2 - b ** 2)
