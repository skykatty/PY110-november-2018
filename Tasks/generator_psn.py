import random as rnd
number = 1
def gpsn():
    number = (rnd.randint(10,50)/2 + 7653) % 76
    yield number

for i in gpsn():
    print(i)