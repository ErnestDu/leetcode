class Solution:
	# @return a list of lists of integers
	def triangle(self, numRows):
		if numRows == 0:
			return []
		elif numRows == 1:
			return [1]
		elif numRows == 2:
			return  [1,1]
		else:
			a = self.triangle(numRows - 1)
			b = []
			b.append(1)
			for i in range (0, len(a) - 1):
				b.append(a[i] + a[i+1])
			b.append(1)
			return b

	def generate(self, numRows):
		a = []
		if numRows == 0:
			return []
		for i in range(1, numRows + 1):
		#print(i , self.triangle(i))
			a.append(self.triangle(i))

		return a

s = Solution()
#n = int(input())
n = 500
#print(s.generate(n))
s.generate(n)
