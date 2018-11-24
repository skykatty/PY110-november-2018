import math
def get_random(seed, limit):
    cur = seed
    for i in range(limit):
        x = float(str(math.sin(cur))[1:5])
        yield x
        cur += 1


for i in get_random(1, 10):
    print(i)

