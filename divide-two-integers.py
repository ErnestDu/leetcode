class Solution:
	# @return an integer
	def divide(self, dividend, divisor):
		a = abs(dividend)
		b = abs(divisor)
		if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
			sign = 1
		else:
			sign = -1
		if a < b:
			result = 0
		elif a == b:
			result = 1
		elif b == 1:
			result = a
		elif b == 2:
			result = a / b
		else:
			result = 0
			c = b
			while c <= a:
				c += b 
				result += 1
		if sign == 1:
			return result
		else:
			return 0 - result
s = Solution()
a = input()
b = input()
print(s.divide(a, b))

