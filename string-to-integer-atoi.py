# http://oj.leetcode.com/problems/string-to-integer-atoi/
class Solution:
	# @return an integer
	def atoi(self, str):
		s = str.strip()
		sign = 1
		if len(s) == 0:
			return 0
		if s[0] == "-":
			sign = -1
			s = s[1:]
		elif s[0] == "+":
			s = s[1:]
		if len(s) == 0:
			return 0
#		s = s.strip()
		a = ""
		flag = 1
		start = 0
#		print(s)
		for i in range (0, len(s)):
			if s[i] >= "0" and s[i] <= "9" and flag == 1:
				if start == 0 and s[i] != "0":
					a = a + s[i]
					start = 1
				elif start == 1:
					a = a + s[i]
			else:
				flag = 0
		if a == "":
			return 0
#		print(a)
		x = 0
		for i in range (0, len(a)):
			x = x + int(a[i]) * pow(10, len(a) - 1 - i)
		if x >= pow(2, 31) and sign == 1: 
			return pow(2,31) - 1
		elif x >= pow(2,31)+1 and sign == -1:
			return 0 - pow(2,31)
		return x * sign

s = Solution()
x = "    - 321"
print(s.atoi(x))
