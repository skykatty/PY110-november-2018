# arr = [2,12,1,10,5,7]
# arr = [2,12,1,10,5,7,'cat']
class SummatorError(Exception):
	pass


class WrongType(SummatorError):
	pass


class NotList(SummatorError):
	pass


class EmptyInput(SummatorError):
	pass


def sum(input):
	s = 0

	if type(input) != list:
		raise NotList("U give me not list!")
	for i in input:
		if type(i) != int:
			raise WrongType("This is not int!")
	for i in input:
		s += i

	return s


def avg(input):
	s = 0
	length = len(input)

	if length == 0:
		raise EmptyInput
	if type(input) != list:
		raise NotList("U give me not list!")
	for i in input:
		if type(i) != int:
			raise WrongType("This is not int!")

	for i in input:
		s += i
	sr = s / length
	return sr