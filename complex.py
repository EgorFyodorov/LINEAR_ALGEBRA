'''
	Класс комплексного числа вида: a + bi
	Поддерживаются все необходимые арифметические операции
	А также работа на основе рациональных чисел
'''

from rational import *

class complex(object): #взаимодействует либо с комплексным, либо с обычным числом. третьего не дано!!!!!

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __add__(self, other): #СЛОЖЕНИЕ
		if type(other) == complex: 
			return complex(self.a + other.a, self.b + other.b)
		return complex(self.a + other, self.b)
	def __radd__(self, other):
		return self + other
	
	def __sub__(self, other): #ВЫЧИТАНИЕ
		if type(other) == complex: 
			return complex(self.a - other.a, self.b - other.b)
		return complex(self.a - other, self.b)
	def __rsub__(self, other):
		return complex(other, 0) - self

	def __mul__(self, other): #УМНОЖЕНИЕ
		if type(other) == complex: 
			return complex(self.a * other.a - self.b * other.b, other.a * self.b + self.a * other.b)
		return complex(self.a * other, self.b * other)
	def __rmul__(self, other):
		return self * other

	def __truediv__(self, other): #ДЕЛЕНИЕ 
	#(работает через умножение)
		if type(other) == complex: 
			return(self * complex(other.a, other.b * (-1)) / (other.a * other.a + other.b * other.b))
		return complex(self.a / other, self.b / other)
	def __rtruediv__(self, other):
		return complex(self.a, self.b * (-1)) * other / (self.a * self.a + self.b * self.b)

	def __eq__(self, other): # x == y
		if type(other) == complex: #с комплексным
			return (self.a == other.a) and (self.b == other.b)
		return (self.b == 0) and (self.a == other)

	def __repr__(self): # PRINT() & STR()
		if self.b > 0:
			return '(' + str(self.a) + ' + ' + str(self.b) + 'j' + ')'
		else:
			return '(' + str(self.a) + ' - ' + str(self.b * (-1)) + 'j' + ')'

	def correction(self):
		return complex(rational.correction(self.a), rational.correction(self.b))

print('COMPLEX')
print('Только с комплексными числами:')
a = complex(1, 2)
b = complex(1, 3)
c = a + b
print(a, '+', b, '=', c)
c = a - b
print(a, '-', b, '=', c)
c = a * b
print(a, '*', b, '=', c)
c = a / b
print(a, '/', b, '=', c)

#print()
print('Взаимодействие с вещественными числами:')

a = complex(1, 2)
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
print()

print('COMPLEX')
print('Только с комплексными числами:')
a = complex(rational(1,2), rational(3,2))
b = complex(rational(3,2), rational(4,2))
c = complex.correction(a + b)
print(a, '+', b, '=', c)
c = complex.correction(a - b)
print(a, '-', b, '=', c)
c = complex.correction(a * b)
print(a, '*', b, '=', c)
c = complex.correction(a / b)
print(a, '/', b, '=', c)

#print()
print('Взаимодействие с вещественными числами:')

c = complex.correction(a + 2)
print(a, '+', 2, '=', c)
c = complex.correction(2 + a)
print(2, '+', a, '=', c)
c = complex.correction(a - 2)
print(a, '-', 2, '=', c)
c = complex.correction(2 - a)
print(2, '-', a, '=', c)
c = complex.correction(a / 2)
print(a, '/', 2, '=', c)
c = complex.correction(2 / a)
print(2, '/', a, '=', c)
c = complex.correction(2 * a)
print(2, '*', a, '=', c)
c = complex.correction(a * 3)
print(a, '*', 3, '=', c)
print()