# http://oj.leetcode.com/problems/unique-binary-search-trees/
class Solution:
	def f(self, n):
		if n == 0:
			return 1
		if n == 1:
			return 1
		s = 0
		for i in range (1, n+1):
			lc = i - 1
			rc = n - i
			s += self.f(lc) * self.f(rc)
		return s
	# @return an integer
	def numTrees(self, n):
		return self.f(n)
ss = Solution()
n = int(input())
print(ss.numTrees(n))
