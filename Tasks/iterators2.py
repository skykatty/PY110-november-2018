l = "hello world"
a = [1, 2, 6]

result = ""
for i,v in enumerate(l):
    if i in a:
        result += l[i]
print(result)

print("".join([v for i, v in enumerate(l) if i in a]))

