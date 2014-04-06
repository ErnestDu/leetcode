# http://oj.leetcode.com/problems/maximum-subarray/
class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxSubArray(self, A):
		if len(A) == 0:
			return 0
		d = [0] * len(A)
		for i in range (0, len(A)):
			if (d[i-1]) > 0:
				d[i] = d[i - 1] + A[i]
			else:
				d[i] = A[i]
		return max(d)

a = [-2,1,-3,4,-1,2,1,-5,4]
b = []
s = Solution()
print(s.maxSubArray(b))
