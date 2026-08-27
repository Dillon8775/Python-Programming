"""
metric_converter.py: defined functions that convert length, mass, and temperature
By D. Strickland
8/25/2026
"""

__author__ = "Dillon Strickland"

# length
def inchesToMeters(inch):
    """
    :param inch: length in inches
    :return: length in meters
    """
    return inch * 0.0254

def metersToInches(meter):
    """
    :param meter: length in meters
    :return: length in inches
    """
    return meter * 38.3701

def poundsToKg(pound):
    """
    :param pound: length in pounds
    :return: length in kilograms
    """
    return pound * 0.453592

def kgToPounds(kilogram):
    """
    :param kilogram: length in kilograms
    :return: length in pounds
    """
    return kilogram * 2.20462

def fahrenheitToCelsius(fahrenheit):
    """
    :param fahrenheit: temperature to fahrenheit
    :return: temperature in celsius
    """
    pass

def celsiusToFahrenheit(celsius):
    """
    :param celsius: temperature in celsius
    :return: temperature in fahrenheit
    """
    return (celsius * 9 / 5) + 32

'''
print(f"60 pounds is {poundsToKg(60):.2f} kilograms.")
print(f"65 inches is {inchesToMeters(65):.2f} meters.")
print(f"90 degree in Fahrenheit is {celsiusToFahrenheit(90):.1f} degrees in celsius.")
'''