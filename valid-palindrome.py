# http://oj.leetcode.com/problems/valid-palindrome/
def isAlphanumeric(s):
	if (s >= '0' and s <= '9') or (s >= 'a' and s <= 'z') or (s >= 'A' and s <= 'Z'):
		return True
	else:
		return False

def isPalindrome1(s):
	length = len(s)
	for i in range (0, length / 2):
		if s[i] != s[length - 1 - i]:
			return False
	return True

class Solution:
    # @param s, a string
    # @return a boolean
	def isPalindrome(self, s):
		ss = ""
		for i in range (0, len(s)):
			if isAlphanumeric(s[i]):
				ss = ss + s[i].lower()
		
		if isPalindrome1(ss):
			return True
		else:
			return False

s = Solution()
#x = str(input())
x = "race a car"
print(s.isPalindrome(x))
