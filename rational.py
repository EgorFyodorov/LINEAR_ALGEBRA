'''
	В данном модуле содержится класс дробь (вида a/b)
со всеми, необходимыми для нормальной работы, функциями
* При каждой арифметическое операции, дробь сокращается;
* Существует коррекция, которая приводит дробь к наиболее
простому виду; 
'''

def abs(a):
	if a < 0:
		return -a
	return a

def greatest_common_divisor(a, b):
	'''Наибольший общий делитель (для сокращения дроби)'''
	a = abs(a)
	b = abs(b)
	if a == 0 or b == 0:
		return a + b
	if a >= b:
		return greatest_common_divisor(a % b, b)
	else:
		return greatest_common_divisor(a, b % a)

def array_output_correction(array):
	'''Вывод массива с корректировкой находящихся в нём дробей'''
	for i in range(len(array)):
		for q in range(len(array[0])):
			print(rational.correction(array[i][q]), end = ' ')
		print()

def array_in_rational(array):
	'''Перевод массива целых чисел в дроби'''
	for i in range(len(array)):
		for q in range(len(array[0])):
			if type(array[i][q]) != rational:
				array[i][q] = rational(array[i][q], 1)
	return array

class rational(object):

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __add__(self, other): #СЛОЖЕНИЕ
		if type(other) == rational:
			result_a = self.a * other.b + other.a * self.b
			result_b = self.b * other.b
			gcd = greatest_common_divisor(result_a, result_b)
			return rational(result_a // gcd, result_b // gcd)
		if type(other) == int:
			return self + rational(other, 1)
	def __radd__(self, other):
		return rational(other, 1) + self

	def __sub__(self, other): #ВЫЧИТАНИЕ 
	#(работает через сложение)
		if type(other) == rational:
			return self + rational(-other.a, other.b)
		if type(other) == int:
			return self + rational(-other, 1)
	def __rsub__(self, other):
		return rational(other, 1) - self

	def __mul__(self, other): #УМНОЖЕНИЕ
		if type(other) == rational:
			result_a = self.a * other.a
			result_b = self.b * other.b
			gcd = greatest_common_divisor(result_a, result_b)
			return rational(result_a // gcd, result_b // gcd)
		if type(other) == int:
			return self * rational(other, 1)
	def __rmul__(self, other):
		return rational(other, 1) * self

	def __truediv__(self, other): #ДЕЛЕНИЕ
	#(работает через уможение)
		if type(other) == rational:
			return self * rational(other.b, other.a)
		if type(other) == int:
			return self * rational(1, other)
	def __rtruediv__(self, other):
		return rational(other, 1) / self

	def __lt__(self, other): # x < y
		if type(other) == rational:
			return self.a / self.b < other.a / other.b
		else:
			return self.a / self.b < other

	def __gt__(self, other): # x > y
		if type(other) == rational:
			return self.a / self.b > other.a / other.b
		else:
			return self.a / self.b > other

	def __eq__(self, other): # x == y
		if type(other) == rational:
			return self.a / self.b == other.a / other.b
		else:
			return self.a / self.b == other

	def __le__(self, other): # x <= y
	#(работает через x > y)
		return not (self > other)

	def __ge__(self, other): # x >= y
	#(работает через x < y)
		return not (self < other)

	def __repr__(self): # PRINT() & STR()
		return str(self.a) + '/' + str(self.b)

	def correction(self):
		'''Коррекция, приводит дробь к наиболее простому виду'''
		if type(self) == int:
			return self
		if self.a == 0:
			return 0 
		elif self.b == 1:
			return self.a
		elif self.b == -1:
			return -self.a
		elif self.b < 0:
			return rational(-self.a, -self.b)
		return self

print('RATIONAL')
print('Только с дробями:')
a = rational(1, 2)
b = rational(1, 3)
c = a + b
print(a, '+', b, '=', c)
c = a - b
print(a, '-', b, '=', c)
c = a * b
print(a, '*', b, '=', c)
c = a / b
print(a, '/', b, '=', c)

print('Взаимодействие с целыми числами:')

c = a + 2
print(a, '+', 2, '=', c)
c = 2 + a
print(2, '+', a, '=', c)
c = a - 2
print(a, '-', 2, '=', c)
c = 2 - a
print(2, '-', a, '=', c)
c = a / 2
print(a, '/', 2, '=', c)
c = 2 / a
print(2, '/', a, '=', c)
c = 2 * a
print(2, '*', a, '=', c)
c = a * 3
print(a, '*', 3, '=', c)

print('Коррекция: ')
print(rational(0, 1), '=',rational.correction(rational(0, 1)))
print(rational(2, 1), '=',rational.correction(rational(2, 1)))
print(rational(-2, 1), '=',rational.correction(rational(-2, 1)))
print(rational(1, -2), '=',rational.correction(rational(1, -2)))
print(rational(2, 5), '=',rational.correction(rational(2, 5)))
print()