class Solution:
	# @return a list of lists of integers
	def generate(self, numRows):
		a = []
		if numRows == 0:
			return []
		elif numRows == 1:
			return [[1]]
		elif numRows == 2:
			return [[1],[1,1]]
		a = [[1], [1,1]]
		for i in range (3, numRows + 1):
			x = a[-1]
			b = []
			b.append(1)
			for j in range (0, len(x) - 1):
				b.append(x[j] + x[j+1])
			b.append(1)
			a.append(b)
		return a

s = Solution()
#n = int(input())
n = 500
s.generate(n)
