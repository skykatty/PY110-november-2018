sentence = "This pop has a dog"

def generator_1(n:str):
    for i in n.split():
        yield i


a = generator_1(sentence)
for j in a:
    print(j)


def generator_2(n:str):
    st = 0
    en = len(n)
    while True:
        y = n.find(" ", st, en)
        if y == -1:
            yield n[st:en]
        yield n[st:y]
        st = y + 1


a = generator_2(sentence)
for j in a:
    print(j)


def generator_psevdo(seed):
    se = seed
    while True:
        ps = (se * 145.814763) % 18.386
        se = (ps % 100) / 100
        yield se


a = generator_psevdo(10)
b = generator_psevdo(10)

for i in a:
    print(i)

for i in b:
    print(i)


