## http://oj.leetcode.com/problems/reverse-integer/
class Solution:
	# @return an integer
	def reverse(self, x):
		##ss = str(x)
		##return int(ss[::-1])
		if x >= 0:
			return int(str(x)[::-1])
		else:
			return 0 - int(str(abs(x))[::-1])
a = int(input())
s = Solution()
print(s.reverse(a))
