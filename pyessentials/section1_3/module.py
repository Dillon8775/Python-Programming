"""
Test Python module file.
"""

'''
print("I like to be a module.")
'''

import math

__counter = 0

if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for e in the_list:
        the_sum += e
    return the_sum

def prodl(the_list):
    global __counter
    __counter += 1
    prod:int = 1
    for e in the_list:
        prod *= e
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    '''
    Create variable i to reference for the for loop
    '''
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 20)

    result = math.e != math.pow(2, 4)
    print(bool(result))
    print(int(result))