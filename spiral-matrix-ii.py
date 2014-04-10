# http://oj.leetcode.com/problems/spiral-matrix-ii/
class Solution:
	# @return a list of lists of integer
	def generateMatrix(self, n):
		matrix = []
		for i in range (0, n):
			temp = []
			for j in range (0, n):
				temp.append(None)
			matrix.append(temp)
		count = 0
		i = j = 0
		while count < n * n:
			while i < n and j < n and matrix[i][j] == None:
				matrix[i][j] = count + 1
				j += 1
				count += 1
			j -= 1
			i += 1
			while i < n and j < n and matrix[i][j] == None:
				matrix[i][j] = count + 1
				i += 1
				count += 1
			i -= 1
			j -= 1
			while j >= 0 and matrix[i][j] == None:
				matrix[i][j] = count + 1
				j -= 1
				count += 1
			j += 1
			i -= 1
			while matrix[i][j] == None:
				matrix[i][j] = count + 1
				i -= 1
				count += 1
			j += 1
			i += 1
		return matrix
s = Solution()
n = input()
print(s.generateMatrix(n))
