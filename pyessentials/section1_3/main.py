from sys import path

path.append('..\\modules')

from module import suml, prodl

zeros = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeros))
print(prodl(ones))