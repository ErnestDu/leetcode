# http://oj.leetcode.com/problems/combinations/
class Solution:
	def f(self, a, n):
		b = []
		for i in range (0, len(a)):
			for j in range(0, n+1):
				if j > a[i][len(a[i]) -1]:
					b.append(a[i] + [j])
		return b
	# @return a list of lists of integers
	def combine(self, n, k):
		a = []
		for i in range (1, n+1):
			a.append([i])
		for i in range (2, k+1):
			a = self.f(a, n)
		return a

n = 10
k = 4
s = Solution()
print(s.combine(n, k))
