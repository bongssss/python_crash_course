from sys import path

path.append('..\\ubong')


import ubong
from ubong import mod, suml, prodl

mod()

print(ubong.counter)

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
