"""
turtle.py: A turtle object that draws a circle
By: Dillon S.
9/24/26
"""

import math
import turtle

class Circle:
    """
    A basic circle with a radius and center
    """
    def __init__(self, radius:int, center):
        self.__radius = radius
        self.__center = center

    # Prints the Circle object, containing the center and area
    def __str__(self):
        area = (math.pi * self.__radius) ** 2
        return f"Circle Center: {self.__center}\nCircle Area: {area}"

    # Draws a circle from a turtle object
    def draw_circle(self, t:turtle):
        pass

    # Getters
    def get_radius(self):
        return self.__radius

    def get_center(self):
        return self.__center

    # Setters
    def set_radius(self, center):
        self.__center = center

    def set_center(self, center):
        self.__center = center

def main():
    pass

# Run main method
if __name__ == "__main__":
    main()