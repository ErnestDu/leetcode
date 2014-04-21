## http://oj.leetcode.com/problems/single-number/
class Solution:
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		a.sort()
		#print(a)
		if len(a) == 1:
			return a[0]
		for i in range (0, len(a), 2):
			##print("i", i, a[i], "i+1", i+1, a[i+1])
			if i + 1 < len(a):
				if a[i] != a[i+1]:
					return a[i]
		return a[len(a)-1]
a = [1,5,1,2,4,8,8,9,9,2,3,3,4]
ss = Solution()
print(ss.singleNumber(a))

