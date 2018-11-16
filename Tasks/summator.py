class SummatorError(Exception):
    pass


class InputDataTypeError(SummatorError):
    pass


class EmptyListError(SummatorError):
    pass


def sum(arr: list):
    sum_ = 0
    if len(arr) == 0: raise EmptyListError
    for x in arr:
        if type(x) == int or type(x) == float :
            sum_ += x
        else:
            raise InputDataTypeError

    return sum_


def avg(arr: list):
        sum_ = 0
        if len(arr) ==0: raise EmptyListError

        for x in arr:
            if type(x) == int or type(x) == float:
                sum_ += x
            else:
                raise InputDataTypeError

        return sum_ / len(arr)

# print(sum([1, 2, 3]))
# print(avg([1, 2, 3]))