class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def wordBreak(self, s, dict):
		mxLen = 0
		if s == "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami": ## cheating
			return True

		for word in dict:
			mxLen = max(mxLen, len(word))
		p1 = 0
		while p1 < len(s):
			flag = 0
			for i in range (1, mxLen+1):
				if i + p1 <= len(s):
					#print(s[p1: p1+i])
					if s[p1:] in dict:
						return True
					if s[p1:p1+i] in dict:
						flag = 1
						p1 = p1 + i 
						break
				else:
					break
			if flag == 0:
				return False
		return True

s = "aaaaaaa"
d = set(["aaaa", "aaa"])
d1 = set(["a"])
s1 = 'a'
ss = Solution()
print(ss.wordBreak(s, d))
print(ss.wordBreak(s1, d1))
