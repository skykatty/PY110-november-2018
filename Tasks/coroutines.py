#бесконечная арифметическая прогрессия
def counter(start, step):
    n = start
    while True:
        new_start = yield n
        if new_start is not None:
            n = new_start
        else:
            n += step
STEP = 10
START = 0
cur = counter(START, STEP)
for i in cur:
    print(i)
    if i >= 1000:
        cur.send(START)
