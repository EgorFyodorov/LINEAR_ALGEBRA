from rational import *
from complex import *
import copy

def array_input(y, x): #функция ввода двумерного массива
	array = [[0 for i in range(x)] for q in range(y)]
	for i in range(y):
		m = list(map(int, input().split()))
		for q in range(x):
			array[i][q] = m[q]
	return array

def array_output(array): #функция вывода двумерного массива
	for i in range(len(array)):
		for q in range(len(array[0])):
			print(array[i][q], end = ' ')
		print()

	
def cofactor(array, i, q): #АЛГЕБРАИЧЕСКОЕ ДОПОЛНЕНИЕ по i,j-му элементу ((−1)^(i+j) * Mi,j)
	array = copy.deepcopy(array)
	for k in range(len(array)):
		array[k].pop(q)
	array.pop(i)
	return (-1)**(i + q) * determinant(array)

def determinant(array): #ОПРЕДЕЛИТЕЛЬ МАТРИЦЫ (квадратного массива)
	array = copy.deepcopy(array)
	rank = len(array)
	if rank == 1:
		return array[0][0]
	if rank == 2:
		return array[0][0] * array[1][1] - array[0][1] * array[1][0]
	result = 0
	for i in range(rank):
		result += array[i][0] * cofactor(array, i, 0) 
	return result 

def adjugate_matrix(array): #ПРИСОЕДИНЁННАЯ МАТРИЦА
	adj_matrix = copy.deepcopy(array) 
	for i in range(len(array)):
		for q in range(len(array[0])):
			adj_matrix[i][q] = cofactor(array, i, q)
	return matrix(adj_matrix)

def invertible_matrix(array): #ОБРАТНАЯ МАТРИЦЫ
	array = copy.deepcopy(array)
	A = adjugate_matrix(array)
	A.transposition()
	A = A * (1 / determinant(array))
	return A

class matrix(): #КЛАСС МАТРИЦА
	def __init__(self, array):
		self.array = array
		self.size_x = len(array[0])
		self.size_y = len(array)

	def __add__(self, other): #CЛОЖЕНИЕ(одноразмерных)
		if (type(other) != matrix) or (self.size_y != other.size_y) or (self.size_x != other.size_x):
			raise TypeError('Некорректная операция')

		result_array = [[0 for i in range(self.size_x)] for q in range(self.size_y)]
		for i in range(self.size_y):
			for q in range(self.size_x):
				result_array[i][q] = self.array[i][q] + other.array[i][q]
		return matrix(result_array)

	def __sub__(self, other): #ВЫЧИТАНИЕ(одноразмерных)
		if (type(other) != matrix) or (self.size_y != other.size_y) or (self.size_x != other.size_x):
			raise TypeError('Некорректная операция')
		return other * (-1) + self 

	def __mul__(self, other): #УМНОЖЕНИЕ(на число и матрицу)     
		if (type(other) == matrix) and (self.size_x == other.size_y): #НА МАТРИЦУ
			n = self.size_x 
			result_array = [[0 for i in range(other.size_x)] for q in range(self.size_y)]
			for i in range(self.size_y):
				for q in range(other.size_x):
					for k in range(n):
						result_array[i][q] += self.array[i][k] * other.array[k][q]
			return matrix(result_array)

		elif type(other) == int or type(other) == rational: #НА ЧИСЛО
			result_array = [[0 for i in range(self.size_x)] for q in range(self.size_y)]
			for i in range(self.size_y):
				for q in range(self.size_x):
					result_array[i][q] = self.array[i][q] * other
			return matrix(result_array)

		else:
			raise TypeError('Некорректная операция')
	def __rmul__(self, other):
		return self * other 

	def __truediv__(self, other): #ДЕЛЕНИЕ (на число, соотв A * (1/b))
		return self * rational(1, other)

	def __pow__(self, other): #ВОЗВЕДЕНИЕ МАТРИЦЫ В СТЕПЕНЬ
		B = copy.deepcopy(self)
		for i in range(other - 1):
			self = self * B
		return self

	def transposition(self): #ТРАНСПОНИРОВАНИЕ
		result_array = [[0 for i in range(self.size_y)] for q in range(self.size_x)]
		for i in range(self.size_x):
			for q in range(self.size_y):
				result_array[i][q] = self.array[q][i]
		self.array = result_array
		
	def rectangle_method(self, y, x): #МЕТОД ПРЯМОУГОЛЬНИКА к Ayx элементу матрицы А
		number_of_columns = self.size_x
		number_of_lines = self.size_y
		side_array = [[0 for q in range(self.size_x)] for j in range(self.size_y)] #побочный(промежуточный) массив, откуда берём данные для прямоугольника
		for j in range(self.size_y):
			for q in range(self.size_x):
				side_array[j][q] = self.array[j][q]

		if self.array[y][x].a != self.array[y][x].b:
			for q in range(number_of_columns):
				self.array[y][q] /= side_array[y][x]

		#непосредственно правило прямоугольника
		for j in range(y):
			for q in range(number_of_columns):
				self.array[j][q] -= side_array[y][q] * side_array[j][x] / side_array[y][x]
			self.array[j][x] = rational(0, 1)

		for j in range(y + 1, number_of_lines):
			for q in range(number_of_columns):
				self.array[j][q] -= side_array[y][q] * side_array[j][x] / side_array[y][x]
			self.array[j][x] = rational(0, 1)

	def jordan_gauss_method(self): #МЕТОД ЖОРДАНА_ГАУССА (идёт по диагонали, может сломаться)

		for i in range(self.size_y):
			for q in range (self.size_x):
				if rational.correction(self.array[i][q]) != 0:
					self.rectangle_method(i, q)
					break	


m, n = map(int, input('Размерность матрицы: ').split())
print('Матрица:')
array = array_input(m, n)
array = array_in_rational(array)
A = matrix(array)

print('1 — К матрице применится алгоритм Жордана-Гаусса. Разрешающими будут i-тые элементы в i-ых строках')
print('2 — Элемент с указаными координатами y и x (начиная с 1) будет сделан разрешающим')
print('3 — Посчитать определитель')
print('4 — Сопряжённая и обратная матрицы')
print('5 — Домножение на ещё одну матрицу')
print('6 — Возведение матрицы в степень')
print('7 — Делить матрицу на число')

while 1:
	print('Введите число кодификатор')
	n = int(input())
	if n == 1:
		A.array = array_in_rational(A.array)
		A.jordan_gauss_method()
		array_output_correction(A.array)
	if n == 2:
		A.array = array_in_rational(A.array)
		while 1:	
			y, x = map(int, input('Координаты: ').split())
			matrix.rectangle_method(A, y - 1, x - 1)
			array_output_correction(A.array)

	if n == 3:
		print('Определитель равен:', rational.correction(determinant(A.array)))
	if n == 4:
		print('Сопряжённая матрица')
		array_output_correction(adjugate_matrix(A.array).array)
		print('Обратная матрица')
		array_output_correction(invertible_matrix(A.array).array)
	if n == 5:
		m, n = map(int, input('Размерность матрицы: ').split())
		print('Матрица:')
		array = array_input(m, n)
		B = matrix(array)
		A = A * B
		print('Ответ:')
		array_output_correction((A).array)
	if n == 6:
		a = int(input('Введите степень: '))
		A = A**a
		array_output_correction(A.array)
	if n == 7:
		a = int(input('Делитель: '))
		A = A/a
		array_output_correction(A.array)


