# http://oj.leetcode.com/problems/single-number/
class Solution:
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		res = 0
		for num in A:
			res ^= num
		return res
