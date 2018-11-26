string = "cow cat dog kitty"


def gena(string):
    start = 0
    while True:
        try:
            ind = string.index(" ", start, len(string))
            yield string[start:ind]
            start = ind + 1
        except ValueError:
            yield string[start:]
            break


for i in gena(string):
    print(i)