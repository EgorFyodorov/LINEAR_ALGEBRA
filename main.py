from linear_algebra import *

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