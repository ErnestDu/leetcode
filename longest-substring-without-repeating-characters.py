# http://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		mx = 0
		if len(s) == 0:
			return 0
		start = 0
		ln = 0	
		for i in range (0, len(s)):
			if s[start: start + ln].count(s[i]) == 0:
				ln += 1
				if ln > mx:
					mx = ln
			else:
				x = s[start: start + ln].index(s[i])
				start += x + 1
				ln -= x

		return mx

s = Solution()
a = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
b = "abcabc"
c = "abcabcd"
print(s.lengthOfLongestSubstring(a))
print(s.lengthOfLongestSubstring(b))
print(s.lengthOfLongestSubstring(c))
