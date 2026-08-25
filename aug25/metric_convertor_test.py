import metric_converter
import math
import random
import time

def main():
    print(metric_converter.__doc__)
    help(metric_converter.fahrenheitToCelsius)

    """
    All of this does the same thing.
    """
    apr = 0.03
    print("apr: ", apr * 100, "%", sep='')
    print(f"apr: {apr * 100}%")
    print(f"apr: {apr:.1%}")

    numbers = [1, 3, 5, 7, 9]
    print("Numbers are: ")
    """
    Specifies special ending when doing it
    """
    for n in numbers:
        print(n, end = " ")

if __name__ == "__main__":
    main()