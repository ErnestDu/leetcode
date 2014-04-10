# http://oj.leetcode.com/problems/rotate-image/
class Solution:
	def rotateCircle(self, matrix, x):
		ln = len(matrix) - 2 * x
		temp = matrix[x][x:x+ln]
		for i in range (0, ln):
			matrix[x][x+i] = matrix[x+ln-1-i][x]
		for i in range (0, ln):
			matrix[x+i][x] = matrix[x+ln-1][x+i]
		for i in range (0, ln):
			matrix[x+ln-1][x+i] = matrix[x+ln-1-i][x+ln-1]
		for i in range (0, ln):
			matrix[x+ln-1-i][x+ln-1] = temp[ln - 1 - i]

	# @param matrix, a list of lists of integers
	# @return a list of lists of integers
	def rotate(self, matrix):
		n = len(matrix)
		if n <= 1:
			return matrix
		for i in range (0, n / 2):
			self.rotateCircle(matrix, i)
		return matrix

s = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1]]
matrix3 = [[1, 2], [3, 4]]
matrix4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix5 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20], [21,22,23,24,25]]
print(s.rotate(matrix))
print(s.rotate(matrix2))
print(s.rotate(matrix3))
print(s.rotate(matrix4))
print(s.rotate(matrix5))
