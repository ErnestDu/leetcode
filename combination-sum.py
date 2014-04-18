class Solution:
	def find(self, candidates, target, a, s):
		temp = s[::]
		#print(temp)
		if sum(temp) == target:
			a.append(temp)
			return 0
		if len(s) == 0:
			mx = min(candidates)
		else:
			mx = max(s)
		for i in range (0, len(candidates)):
			if candidates[i] >= mx:
				if sum(temp) + candidates[i] == target:
					temp.append(candidates[i])
					a.append(temp)
				elif sum(temp) + candidates[i]  <target:
					temp1 = temp[::]
					temp1.append(candidates[i])
					self.find(candidates, target, a, temp1)
				else:
					break
	def combinationSum(self, candidates, target):
		a = []
		s = []
		candidates.sort()
		for i in range (0, len(candidates)):
			s = [candidates[i]]
			self.find(candidates, target, a, s)
		return a

c = [2, 3, 6, 7]
c1 = [1, 2]
c2 = [8, 7, 4, 3]
s = Solution()
print(s.combinationSum(c, 7))
print(s.combinationSum(c1, 3))
print(s.combinationSum(c2, 11))
