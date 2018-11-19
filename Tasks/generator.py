string = "cow,cat dog kitty!"


sep = ",.?! "
string_new = ""
def gena():
    string_new = ""
    for i in string:
        if i not in sep:
            string_new+=i
        else:
            yield string_new
            string_new = ""
    yield string_new

for i in gena():
    print(i)