from math import *

v = int(input('Vnesi hitrost: '))
kot = int(input('Vnesi kot: '))

s = ((v * v) * sin(radians(2 * kot))) / 9.81

print('Dolžina strela je:', s)