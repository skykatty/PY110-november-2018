import itertools
x = [x**2 for x in range(1,10) if x % 2 == 0]
print(x)

def f(x):
    return x ** 2

def s(x):
    return x if x % 2 == 0 else None

l = [x for x in range(10)]
print(list(map(f,list(filter(s, l)))))


print(list(map(lambda x: x**2, list(filter(s, l)))))
