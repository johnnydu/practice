def matrix_multiplication(A, B):
	assert len(A) > 0 and len(A[0]) == len(B), 'incompatible sizes'

	new_matrix = []
	for i in range(len(A)):
		row = []
		for j in range(len(B[0])):
			row.append(row_A_dot_col_B(A, B, i, j))
		new_matrix.append(row)
	return new_matrix

def row_A_dot_col_B(A, B, i, j):
	total = 0
	for k in range(len(A[0])):
		total += A[i][k]*B[k][j]
	return total

print matrix_multiplication([[1, 2]], [[2], [1]])
print matrix_multiplication([[1,2,3],[4,5,6]], [[1,2], [1, 2], [1,2]])