# http://oj.leetcode.com/problems/text-justification/
class Solution:
	# @param words, a list of strings
	# @param L, an integer
	# @return a list of strings
	def fullJustify(self, words, L):
		count = 0
		if len(words) == 0:
			return []
		ss = []
		while count < len(words):
			tl = 0
			tc = 1
			a = []
			tw = 0
			while count < len(words) and tl <= L:
				tw  += len(words[count])
				if tc > 1:
					tl = tw + (tc - 1)
				else:
					tl = tw
				if tl <= L:
					a.append(words[count])
					tc += 1
					count += 1
			#print(a)
			la = 0
			s = ""
			for i in range (0, len(a)):
				la += len(a[i])
			lb = L - la
			#print(la, lb)
			if len(a) == 1:
				s = a[i] + " " * L
				s = s[:L]
			else:
				sp = lb / (len(a) - 1)
				spx = lb % (len(a) - 1)
				s = a[0]
				for i in range (1, len(a)):
					if spx > 0: 
						s += " " * (sp+1) + a[i]
						spx -= 1
					else:
						s += " " * sp + a[i]
			ss.append(s)
#		print(ss)
		x = ss[-1]
		x = x.split()
		y = ""
		if len(x) == 0:
			return [" " * L]
		if len(x) == 1:
			y += x[0] + " " * L
			y = y[:L]
		else:
			y += x[0]
			for i in range (1, len(x)):
				y += " " + x[i]
			y += " " * L
			y = y[: L]
		del(ss[-1])
		ss.append(y)
		return ss

s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
words1 = ["What","must","be","shall","be."]
words2 = [""]
L = 14
print(s.fullJustify(words, L))
print(s.fullJustify(words1, 12))
print(s.fullJustify(words2, 0 ))
