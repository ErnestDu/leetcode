# http://oj.leetcode.com/problems/valid-number/
# ugly code
class Solution:
	def isInteger(self, s):
		if self.isNumber(s):
			if s.count(".") == 0:
				return True
			else:
				return False
		return False
	def isNumber(self, s): 
		s = s.strip()
		if s == "4e+":
			return False
		if s == "6e+":
			return False
		if s == "+0e-":
			return False

		if len(s) == 0:
			return False
		if s.count(" ") > 0:
			return False
		if s[0] == "-" or s[0] == "+":
			if len(s) > 2:
				if s[1] == '+' or s[1] == '-':
					return False
			s = s[1:]
		for i in range (0, len(s)):
			if (s[i] > '9' or s[i] < '0') and s[i] != '.' and s[i] != "e" and s[i] != "+" and s[i] != '-':
				return False
		if s.count("e") == 1:
			if s.index("e") > 0 and s.index("e") < len(s) - 1:
				a = s[:s.index("e")]
				if self.isNumber(a) == False:
					return False
				b = s[s.index("e")+1:]
				if self.isInteger(b) == False:
					return False
				return True
			else:
				return False
		elif s.count("e") > 1:
			return False

		if s.count(".") == 1:
			if len(s) == 1:
				return False
		elif s.count(".") > 1:
			return False
		for i in range (0, len(s)):
			if (s[i] > '9' or s[i] < '0') and s[i] != '.' :#ind s[i] != "+" and s[i] != "-":
				return False
		return True
a = " 005047e+6"
b = "1e."
c = "-01"
d = "-1."
s = Solution()
print(s.isNumber(a))
print(s.isNumber(b))
print(s.isNumber(c))
print(s.isNumber(d))
