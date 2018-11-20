def getword(s : str):
    s = s + " "  # висящий пробел для обработки последнего слова. Костыль )

    b = 0
    n = -1
    while True:
        n = s.find(' ', n + 1)
        if n < 0:
            return
        yield s[b:n]
        b = n + 1

def wordbyword(mystr):
    try:
        gen = getword(mystr)
        while True:
            print(next(gen))
    except StopIteration:
        pass

wordbyword('Lorem ipsum dolor')


