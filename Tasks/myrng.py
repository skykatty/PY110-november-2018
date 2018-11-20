def myverybadrng(seed):
    a, b, c = 55, 17, 78
    while True:
        seed = (a * seed + b) % c
        yield seed

gen = myverybadrng(2)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

