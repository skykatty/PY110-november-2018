predloj = "I love you."

def GetWords(words):
    cur, prev = 0, 0
    while cur < len(words):
        if words[cur] == ' ' or words[cur] == '.':
           yield words[prev:cur:]
           prev = cur + 1
        cur += 1


for i in GetWords(predloj):
    print(i)

