"""
circle_calculator.py: A turtle object that draws a circle
By: Dillon S.
9/24/26
"""

import math
import turtle

class Circle:
    """
    A basic circle with a radius and center
    """
    def __init__(self, radius=1.0, center=(0, 0)):
        self.__radius = radius
        self.__center = center

    # Prints the Circle object, containing the center and area
    def __str__(self):
        return f"Circle Center: {self.__center}\nCircle Area: {self.get_area():.2f}"

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

    # Returns the area of the circle
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # Draws the circle
    def draw_circle(self, t):
        t.penup()

        x, y = self.__center
        t.goto(x, y - self.__radius)

        t.setheading(0)
        t.pendown()

        distance = (2.0 * math.pi * self.__radius) / 120.0
        for i in range (120):
            t.forward(distance)
            t.left(3)

# Testing Code / Test Execution
def main():
    # Setup turtle screen
    screen = turtle.Screen()
    screen.title("Circle Test")
    t = turtle.Turtle()
    t.speed(0)  # Fast drawing speed

    print("--- Creating First Circle Object ---")
    c1 = Circle(radius=50, center=(0, 0))
    print(f"Initial c1 string representation: {c1}")
    print(f"c1 Radius via getter: {c1.get_radius()}")
    print(f"c1 Center via getter: {c1.get_center()}")
    print("Drawing c1...")
    c1.draw_circle(t)

    print("\n--- Modifying First Circle via Setters ---")
    c1.set_radius(100)
    c1.set_center((-150, 100))
    print(f"Updated c1 string representation: {c1}")
    print("Drawing updated c1...")
    c1.draw_circle(t)

    print("\n--- Creating Second Circle Object ---")
    c2 = Circle(radius=75, center=(150, -50))
    print(f"Initial c2 string representation: {c2}")
    print("Drawing c2...")
    c2.draw_circle(t)

    screen.mainloop()

# Run main method
if __name__ == "__main__":
    main()