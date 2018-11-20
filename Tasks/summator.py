class SummatorError(Exception):
    pass

class UnCorrectTypeError(SummatorError):
    pass
class DivideError(SummatorError):
    pass

def sum(input):
    if type(input) != list:
        raise UnCorrectTypeError("входным параметром ф-ции summ должен быть список list")
    summ_ = 0
    for item in input:
        if type(item) != int and type(item) != float:
            raise UnCorrectTypeError("элементами списка должны быть переменные типа int или float")
        summ_ += item
    return summ_

def avg(input):
    if type(input) != list:
	    raise UnCorrectTypeError("входным параметром ф-ции summ должен быть список list")
    if len(input) == 0:
        raise DivideError("нельзя передавать в функцию avg пустой массив")
    return sum(input)/len(input)


#a = []
#avg(a)

