# http://oj.leetcode.com/problems/3sum-closest/
class Solution:
	# @return an integer
	def threeSumClosest(self, num, target):
		if len(num) < 3:
			return 0
		mn = abs(target - (num[0] + num[1] + num[2]))
		result = num[0] + num[1] + num[2]
		for i in range (0, len(num) - 2):
			for j in range (i+1, len(num) - 1):
				for k in range (j+1, len(num)):
					if abs(target - (num[i] + num[j] + num[k])) < mn:
						mn = abs(target - (num[i] + num[j] + num[k]))
						result = num[i] + num[j] + num[k]
						if mn == 0:
							return result
		return result
s = Solution()
a = [-1, 2, 1, -4]
print(s.threeSumClosest(a, 1))
