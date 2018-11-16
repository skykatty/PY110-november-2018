class SummatorError(Exception):
    pass


class InputDataTypeError(SummatorError):
    pass


class EmptyListError(SummatorError):
    pass


class NotListError(SummatorError):
    pass


def checkNotList(data):
    return type(data) != list

def checkIsEmptyList(arr):
    return len(arr) == 0

def checkDataTypes(elm):
    return type(elm) == int or type(elm) == float



def sum(arr: list):
    sum_ = 0
    if checkNotList(arr): raise NotListError
    if checkIsEmptyList(arr): raise EmptyListError

    for x in arr:
        if checkDataTypes(x):
            sum_ += x
        else:
            raise InputDataTypeError

    return sum_


def avg(arr: list):
        return sum(arr) / len(arr)

# print(sum([1, 2, 3]))
# print(avg([1, 2, 3]))