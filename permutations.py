# http://oj.leetcode.com/problems/permutations/
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
	def insert1(self, a, num):
		x = []
		for i in range (0, len(a)):
			for j in range (0, len(a[i]) + 1):
				b = a[i][:]
				b.insert(j, num)
				if x.count(b) == 0:
					x.append(b)
		return x

	def permute(self, num):
		if len(num) == 0:
			return []
		elif len(num) == 1:
			return [[num[0]]]
		else:
			a = [[num[0]]]
			for i in range (1, len(num)):
				a = self.insert1(a, num[i])
			return a

s = Solution()
a = [1, 1, 0, 0]
print(s.permute(a))
