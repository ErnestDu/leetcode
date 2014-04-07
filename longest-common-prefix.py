# http://oj.leetcode.com/problems/longest-common-prefix/
class Solution:
	# @return a string
	def commonPrefix(self, str1, str2):
		if len(str1) * len(str2) <= 0:
			return ""
		if str1[0] != str2[0]:
			return ""
		for i in range (0, min(len(str1), len(str2))):
			if str1[i] != str2[i]:
				return str1[0:i]
		return str1[0:min(len(str1), len(str2))]
				
	def longestCommonPrefix(self, strs):
		if len(strs) == 0:
			return ""
		elif len(strs) == 1:
			return strs[0]
		prefix = strs[0]
		for i in range (1, len(strs)):
			prefix = self.commonPrefix(prefix, strs[i])
			if prefix == "":
				return prefix
		return prefix

a = ["", "hellojim", "hellojack"]
s = Solution()
print(s.longestCommonPrefix(a))
