from linear_algebra import *

m, n = map(int, input('Matrix size (y on x): ').split())
print('Matrix:')
array = array_input(m, n)
array = array_in_rational(array)
A = matrix(array)

print("1 — Jordnan-Gauss alorhitm. For i'th columns and i-th lines")
print('2 — Resolution of element (a, a)')
print('3 — Determinant')
print('4 — Adjugate and inverible matrices (if exists)')
print('5 — Multiplication on other matrix')
print('6 — Exponentiation on matrix ')
print('7 — Divide by a number')
print('0 — stopping')

while 1:
	print('Type a codificator number')
	n = int(input())
	if n == 1:
		A.array = array_in_rational(A.array)
		A.jordan_gauss_method()
		array_output_correction(A.array)
	if n == 2:
		A.array = array_in_rational(A.array)
		while 1:	
			y, x = map(int, input('Coordinates: ').split())
			matrix.rectangle_method(A, y - 1, x - 1)
			array_output_correction(A.array)

	if n == 3:
		print('Determinant:', rational.correction(determinant(A.array)))
	if n == 4:
		print('Adjugate matrix: ')
		array_output_correction(adjugate_matrix(A.array).array)
		print('Inverible matrix: ')
		array_output_correction(invertible_matrix(A.array).array)
	if n == 5:
		m, n = map(int, input('Matrix size (y on x): ').split())
		print('Matrix:')
		array = array_input(m, n)
		B = matrix(array)
		A = A * B
		print('Answer:')
		array_output_correction((A).array)
	if n == 6:
		a = int(input('Type power: '))
		A = A**a
		array_output_correction(A.array)
	if n == 7:
		a = int(input('Divider: '))
		A = A/a
		array_output_correction(A.array)
	if n == 0:
		break