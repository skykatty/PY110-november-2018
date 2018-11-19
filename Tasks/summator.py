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


def error(input):
	length = len(input)
	if type(input) != list:
		raise NotList("U give me not list!")
	for i in input:
		if type(i) != int:
			raise WrongType("This is not int!")
	if length == 0:
		raise EmptyInput
	if type(input) != list:
		raise NotList("U give me not list!")
	for i in input:
		if type(i) != int:
			raise WrongType("This is not int!")


def sum(input):
	s = 0

	try:
		for i in input:
			s += i
	except:
		error(input)

	return s


def avg(input):
	s = 0
	length = len(input)

	try:
		for i in input:
			s += i
		sr = s / length
	except:
		error(input)

	return sr