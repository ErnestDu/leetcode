# http://oj.leetcode.com/problems/two-sum/
class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		#for i in range (0, len(num)):
		#	x = target - num[i]
		#	if num[i+1:].count(x) > 0:
		#		p = num.index(x) + 1
		#		return (min(p, i+1) ,max(p, i+1))
		m = []
		for i in range (0, len(num)):
			m.append(num[i])
		num.sort()
		for i in range (0, len(num)):
			if num[i] > target:
				return None
			for j in range (i + 1, len(num)):
				if num[j] + num[i]> target:
					break
				if num[i] + num[j] == target:
					#print(num[i], num[j])
					#print(m)
					x = m.index(num[i]) + 1
					if num[i] == num[j]:
						y = m[x:].index(num[j]) + 1 + x	
					else:
						y = m.index(num[j]) + 1
					return (min(x, y), max(x, y))
		return None

s = Solution()
a = [0, 4, 3, 0]
print(s.twoSum(a, 0))
