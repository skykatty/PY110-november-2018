def seqencer(start):
    n = start
    while True:
        data = yield n
        if data is None:
            n += 1
        else:
            n = data



g = seqencer(0)
g.send(None)
print(g.send(5))
print(g.send(None))
print(g.send(None))
print(g.send(8))
print(g.send(None))
print(g.send(None))
print(g.send(None))