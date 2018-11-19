class SummatorError(Exception):
    pass

def is_inp_correct(l):
    for i in l:
        if type(i) != int and type(i) != float:
            return False
    return True

def sum(input):
    if not is_inp_correct(input):
        raise SummatorError("На вход был подан массив с некорректными данными")
    my_sum = 0
    for i in input:
        my_sum += i
    return my_sum

def avg(input):
    if len(input) == 0:
        raise SummatorError("На вход был подан пустой массив")
    if not is_inp_correct(input):
        raise SummatorError("На вход был подан массив с некорректными данными")

    my_avg = sum(input) / len(input)

    return my_avg

