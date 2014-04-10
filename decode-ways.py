# http://oj.leetcode.com/problems/decode-ways/
class Solution:
	# @param s, a string
	# @return an integer
	def numDecodings(self, s):
		s = str(s)
		d = [0] * len(s)
		if len(s) == 0:
			return 0
		if s[0] == "0":
			return 0
		if len(s) == 1:
			return 1
		for i in range (0, len(s)-1):
			if s[i] == "0" and s[i+1] == "0":
				return 0
			elif s[i] > "2" and s[i+1] == "0":
				return 0
		d[0] = 1
		if int(s[0] + s[1]) <= 26:
			if s[1] == "0":
				d[1] = 1
			else:
				d[1] = 2
		else:
			d[1] = 1
		for i in range (2, len(s)):
			if i < len(s) - 1 and s[i] == "0" and s[i+1] == "0":
				return 0
			if int(s[i-1] + s[i]) > 26 or s[i-1] == "0":
				d[i] += d[i-1]
			elif s[i] == "0":
				d[i] += d[i-2]
			else:
				d[i] += d[i-2]
				d[i] += d[i-1]
		return d[len(s) - 1]

s = Solution()
n = "227"
print(s.numDecodings(n))
