"""
модуль, который генерирует случайные адреса для тестирования ПО службы доставки
"""

import re
import json
import random


class InputError(Exception):
	pass


class CheckTypeError(InputError):
	pass


def data_type_checking(check_data):
	"""
	Проверка, что тип данных str

	:param check_data:  проверяеммые данные
	:return: None
	"""
	if type(check_data) != str:
		raise ValueError('It\'s not str')


def correct_input(check_data):
	"""
	Проверка, что нет опечаток

	:param check_data: проверяеммые данные
	:return: None
	"""
	if re.search(r'(?:[,.?!\n])', check_data):
		raise CheckTypeError("check_data")


def load_json(json_data):
	"""
	прием json в  виде строки

	:param json_data:
	:return: dict
	"""
	my_dict = json.loads(json_data)
	return my_dict


def read_file(file_data):
	"""
	Считываем из файла
	:return: содержание файлов
	"""
	data = []
	with open(file_data, 'r') as f:
		for line in f:
			data.append(line)
	return data


def address_gen(country, city, street):
	while True:
		n = random.randint(1, 100)
		housing = [None, 1]
		address = {'country': random.choice(country), 'city': random.choice(city), 'street': random.choice(street),
					'housing': random.choice(housing), 'home': n}
		yield address


def decarator_my():
	"""
	Декоратор
	:return:
	"""

	def my_decorator(func):
		def wrapped(*ar, **kwargs):
			parameter = "test"
			if ar:
				if parameter in ar:
					print("Вызов функции decorated_function с параметрами {}".format(ar))
				elif kwargs:
					for _ in kwargs.values():
						if parameter in kwargs:
							print("Вызов функции decorated_function с параметрами {}".format(kwargs))
					return func(*ar, **kwargs)

		return wrapped

	return my_decorator


if __name__ == '__main__':
	json_dict = json.dumps({'Список_стран': 'Россия',
							'Список_городов': 'Москва',
							'Список_улиц': ('Арбат',
											'Большая Молчановка',
											'Воздвиженка',
											'Знаменка',
											'Композиторская',
											'Моховая')}, ensure_ascii=False)
	print(load_json(json_dict))

	city = ["Москва"]
	street = ['Арбат', 'Большая Молчановка', 'Воздвиженка', 'Знаменка', 'Композиторская', 'Моховая']
	country = ["Россия"]
	print(next(address_gen(country, city, street)))
	print(next(address_gen(country, city, street)))

	@decarator_my()
	def decorated_function():
		print()

	decorated_function("test", 'дом')
