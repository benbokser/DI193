
# Daily Challenge - Circle

# Last Updated: November 5th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll learn

#     Object-Oriented Programming (OOP)
#     Dunder (Magic) Methods in Python


# Instructions

# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.
import math

class Circle:
    def __init__(self, radius=0, diameter=0):
        # We prioritize radius if both are provided, 
        # otherwise we calculate radius from diameter.
        if radius:
            self.radius = radius
        elif diameter:
            self.diameter = diameter
        else:
            self.radius = 0

    @property
    def radius(self):
        """Query the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius directly."""
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self):
        """Query the diameter (calculated from radius)."""
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        """Set the diameter (updates the internal radius)."""
        if value < 0:
            raise ValueError("Diameter cannot be negative.")
        self.radius = value / 2
# test:
# print(c1.diameter)
# Abilities of a Circle Instance
# Your Circle class should be able to:
#     ✅ Compute the circle’s area.

    def area(self):
        return math.pi * (self.radius**2)
#     ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
    def __str__(self):
        return f'Circle of radius {self.radius}, diameter {self.diameter}'
    
    def __repr__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

#     ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).

    def __add__(self, other: Circle):
        if not isinstance(other, Circle):
            raise TypeError('Wrong type.')
        return Circle(radius = self.radius + other.radius)

#     ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
    def __gt__(self, other):
        return self.radius > other.radius
    def __lt__(self, other):
        return self.radius < other.radius
#     ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
    def __eq__(self, other):
        return self.radius == other.radius
#     ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

#test:
c1= Circle(radius=5)
c2= Circle(radius=10)
print(c1.diameter)
print(c1.area())
print(c1)
print(repr(c1))
print(c1 + c2)
circles = [Circle(radius=5), Circle(radius=2), Circle(radius=8), Circle(radius=1)]
print(sorted(circles))
# Bonus Challenge (Optional)

# If you want an extra challenge:

#     Install the Turtle module (pip install PythonTurtle)
#     Draw the sorted circles visually on the screen!


