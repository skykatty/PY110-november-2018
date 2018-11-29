def gpsn():
    seed = int(input())
    number = (seed/2 + 7653) / 18652
    yield number

a = gpsn()
print(next(a))