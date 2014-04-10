# http://oj.leetcode.com/problems/spiral-matrix/
class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of integers
	def spiralOrder(self, matrix):
		n = len(matrix)
		if n > 0:
			m = len(matrix[0])
		else:
			return []
		count = 0
		i = j = 0
		a = []
		while count < n * m:
			while i < n and j < m and matrix[i][j] != None:
				a.append(matrix[i][j])
				matrix[i][j] = None
				j += 1
				count += 1
			j -= 1
			i += 1
			while i < n and j < m and matrix[i][j] != None:
				a.append(matrix[i][j])
				matrix[i][j] = None
				i += 1
				count += 1
			i -= 1
			j -= 1
			while j >= 0 and matrix[i][j] != None:
				a.append(matrix[i][j])
				matrix[i][j] = None
				j -= 1
				count += 1
			j += 1
			i -= 1
			while matrix[i][j] != None:
				a.append(matrix[i][j])
				matrix[i][j] = None
				i -= 1
				count += 1
			j += 1
			i += 1
		return a
s = Solution()
matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
matrix2 = [[2,5],[8,4],[0,-1]]
print(s.spiralOrder(matrix))
print(s.spiralOrder(matrix2))
