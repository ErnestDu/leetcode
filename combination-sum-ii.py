# http://oj.leetcode.com/problems/combination-sum-ii/
class Solution:
	def find(self, candidates, target, a, s, i):
		temp = s[::]
		if sum(temp) == target:
			if a.count(temp) == 0:
				a.append(temp)
			return a
		for j in range (i + 1, len(candidates)):
			if sum(temp) + candidates[j] == target:
				temp.append(candidates[j])
				if a.count(temp) == 0:
					a.append(temp)
			elif sum(temp) + candidates[j] < target:
				temp1 = temp[::]
				temp1.append(candidates[j])
				self.find(candidates, target, a, temp1, j)
			else:
				break

	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum2(self, candidates, target):
		a = []
		candidates.sort()
		for i in range (0, len(candidates)):
			s = [candidates[i]]
			self.find(candidates, target, a, s, i)
		return a

a = [10, 1, 2, 7, 6, 1, 5]
t = 8
b = [1, 1]
s = Solution()
print(s.combinationSum2(a, t))
print(s.combinationSum2(b, 1))
