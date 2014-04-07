class Solution:
	# @return an integer
	def romanToInt(self, s):
		td = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
		tc = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
		tb = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
		ta = ["", "M", "MM", "MMM"]
		ln = len(s)
		if ln == 0:
			return 0
		i = 0
		sa = sb = sc = sd = ""
		if s[0] == "M":
			while i < ln and s[i] == "M":
				sa += s[i]
				i += 1
		#print(i, sa)
		
		if i < ln and (s[i] == "C" or s[i] == "D"):
			while i < ln and (s[i] == "C" or s[i] == "D" or s[i] == "M"):
				sb += s[i]
				i += 1
		#print(i, sb)
		
		if i < ln and (s[i] == "X" or s[i] == "L"):
			while i < ln and (s[i] == "X" or s[i] == "L" or s[i] == "C"):
				sc += s[i]
				i += 1
		#print(i, sc)

		if i < ln:
			sd = s[i:]
		#print(i, sa)
		
		a = b = c = d = 0
		for i in range (0, len(ta)):
			if ta[i] == sa:
				a = i

		for i in range (0, len(tb)):
			if tb[i] == sb:
				b = i

		for i in range (0, len(tc)):
			if tc[i] == sc:
				c = i
		
		for i in range (0, len(td)):
			if td[i] == sd:
				d = i
		#print(a, b, c, d)
		return a * 1000 + b * 100 + c * 10 + d

s = Solution()
ss = "MMMCC"
print(s.romanToInt(ss))
