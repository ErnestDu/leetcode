# http://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
def combine(s, x):
	ss = []
	letter = letters[int(x)]
	for i in range (0, len(s)):
		for j in range (0, len(letter)):
			ss.append(s[i]+letter[j])
	return ss
class Solution:
	# @return a list of strings, [s1, s2]
	def letterCombinations(self, digits):
		if len(digits) > 0:
			s = []
			letter = letters[int(digits[0])]
			for i in range (0, len(letter)):
				s.append(letter[i])
		else:
			return [""]
		for i in range (1, len(digits)):
			s = combine(s, digits[i])
		return s

ss = Solution()
#digits = str(input())
print(ss.letterCombinations(""))
