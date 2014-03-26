class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
		length = len(matrix)
		for i in range(0, length):
			if matrix[i].count(target):
				return True
		return False
