def cor():
    value = yield
    q = 2
    i = 0
    yield value
    while True:
        i += 1
        if i == 1:
            yield value
        else:
            value *= q
            yield value

g = cor()
next(g)
g.send(2)
for i in g:
    print(i)