# http://oj.leetcode.com/problems/add-binary/
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
		la = len(a)
		lb = len(b)
		if la > lb:
			lm = la
		else:
			lm = lb

		result = ""
		aux = 0
		for i in range (0, lm):
			if i < la:
				x = int(a[la - 1 - i])
			else:
				x = 0
			if i < lb:
				y = int(b[lb - 1 -i])
			else:
				y = 0
			
			bit = int((aux + x + y) % 2)
			aux = int((aux + x + y) / 2)
			result = str(bit) + result

		if aux == 1:
			result = "1" + result

		return result

ss = Solution()
a = str(input())
b = str(input())
print(ss.addBinary(a, b))
