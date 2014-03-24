## http://oj.leetcode.com/problems/reverse-words-in-a-string/
class Solution:
	def reverseWords(self, s):
		print(self)
		ns = s.split()
		ns.reverse()
		return " ".join(ns)

##print(Solution.reverseWords("solution","aa bb cc"))

ss = Solution()
print(ss.reverseWords("aa cc dd"))
