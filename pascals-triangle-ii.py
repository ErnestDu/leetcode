# http://oj.leetcode.com/problems/pascals-triangle-ii/
class Solution:
	# @return a list of integers
	def getRow(self, rowIndex):
		rowIndex = rowIndex + 1
		if rowIndex <= 0:
			return []
		elif rowIndex == 1:
			return [1]
		elif rowIndex == 2:
			return [1, 1]
		else:
			x = [1, 1]
			for i in range (3, rowIndex + 1):
				a = []
				a.append(1)
				for j in range (0, len(x) - 1):
					a.append(x[j] + x[j + 1])
				a.append(1)
				x = a
			return x
s = Solution()
n = int(input())
print(s.getRow(n))
