# http://oj.leetcode.com/problems/set-matrix-zeroes/

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
	def setZeroes(self, matrix):
		m = len(matrix)
		if m != 0:
			n = len(matrix[0])
		for i in range (0, m):
			for j in range (0, n):
				if matrix[i][j] == 0:
					#markRow(matrix, i, j)
					#markCol(matrix, i, j)
					for k in range (0, n):
						if matrix[i][k] != 0:
							matrix[i][k] = -111 ## dirty code
					for k in range (0, m):
						if matrix[k][j] != 0:
							matrix[k][j] = -111

		for i in range (0, m):
			for j in range (0, n):
				if matrix[i][j] == -111:
					matrix[i][j] = 0
