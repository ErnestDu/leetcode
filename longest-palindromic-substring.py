class Solution:
	def maxPalindrome1(self, p, s):
		x = p - 1
		y = p + 1
		end = 0
		count = 0
		if x >= 0 and y < len(s):
			if s[x] != s[y]:
				#print(s[p])
				return s[p]
		while x >= 0 and y < len(s) and end == 0:
			if s[x] == s[y]:
				x -= 1
				y += 1
				count += 1
			else:
				end = 1
		return s[p-count:p+count+1]
		
	def maxPalindrome2(self, p, s):
		if p + 1 < len(s):
			if s[p] != s[p+1]:
				return ""
		else:
			return ""
		x = p - 1
		y = p + 2
		end = 0
		count = 0
		if x >= 0 and y < len(s):
			if s[x] != s[y]:
				return s[p: p+1]
		while x >= 0 and y < len(s) and end == 0:
			if s[x] == s[y]:
				x -= 1
				y += 1
				count += 1
			else:
				end = 1
		return s[p-count:p+count+2]
			
	# @return a string
	def longestPalindrome(self, s):
		mx = 0
		for i in range (0, len(s)):
			s1 = self.maxPalindrome1(i, s)
			s2 = self.maxPalindrome2(i, s)
			if len(s1) > len(s2):
				ln = len(s1)
				ss = s1
			else:
				ln = len(s2)
				ss = s2
			if mx < ln:
				mx = ln
				result = ss
		return result
