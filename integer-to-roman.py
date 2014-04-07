class Solution:
	# @return an string
	def intToRoman(self, num):
		td = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
		tc = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
		tb = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
		ta = ["", "M", "MM", "MMM"]
		a = num / 1000
		b = (num - a * 1000) / 100
		c = (num - a * 1000 - b * 100) / 10
		d = num % 10
		s = ""
		s = ta[a] + tb[b] + tc[c] + td[d]
		return s
s = Solution()
x = input()
print(s.intToRoman(x))
