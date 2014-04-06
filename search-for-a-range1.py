class Solution:
	def searchRange(self, A, target):
		if A.count(target) > 0:
			x = []
			x.append(A.index(target))
			x.append(A.index(target) + A.count(target) - 1)
		else:
			x = [-1, -1]
		return x
