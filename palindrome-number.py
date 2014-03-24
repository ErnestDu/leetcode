#!/bin/env python2
# http://oj.leetcode.com/problems/palindrome-number/
def getInteger(x, pos, length):
	return int((x % int(pow(10, length-pos+1))) / int(pow(10, length-pos)))
class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		length = len(str(x))
		if x < 0:
			return False
		if length == 1:
			return True
		for i in range (1, length / 2 + 1):
			if getInteger(x, i, length) != getInteger(x, length - i + 1, length):
				return False
			return True

s = Solution()
x = int(input())
print(s.isPalindrome(x))
