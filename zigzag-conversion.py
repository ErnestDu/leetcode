# http://oj.leetcode.com/problems/zigzag-conversion/
class Solution:
	# @return a string
	def convert(self, s, nRows):
		a = []
		if nRows == 1:
			return s
		if nRows == 2:
			ss = ""
			for i in range (0, len(s), 2):
				ss += s[i]
			for i in range (1, len(s), 2):
				ss += s[i]
			return ss
		for i in range (0, nRows):
			b = []
			a.append(b)
		d = 1
		count = 0
		for i in range (0, len(s)):
			if d == 1:
				a[count].append(s[i])
				count += 1
			else:
				a[nRows-2-count].append(s[i])
				count += 1
			if d == 1 and count == nRows:
				count = 0
				d *= -1
			elif d == -1 and count == nRows - 2:
				count = 0
				d *= -1
		ss = ""
		for i in range (0, nRows):
			for j in range (0, len(a[i])):
				ss += a[i][j]
		return ss

s = Solution()
x = "PAYPALISHIRING"
n = 3
print(s.convert(x, 3))
