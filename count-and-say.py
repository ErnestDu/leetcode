# http://oj.leetcode.com/problems/count-and-say/
class Solution:
	# @return a string
	def generate(self, n):
		s = str(n)
		i = 0
		if len(s) < 0:
			return 0
		p = s[0]
		result = ""
		while i < len(s):
			temp = ""
			while i < len(s) and s[i] == p:
				temp += s[i]
				i += 1
			if i < len(s):
				p = s[i]
			result += (str(len(temp)) + temp[0])
		return int(result)

	def countAndSay(self, n):
		if n == 0:
			return None
		elif n == 1:
			return "1"
		p = 1
		for i in range (2, n + 1):
			p = self.generate(p)
		return str(p)
s = Solution()
n = input()
print(s.countAndSay(n))
