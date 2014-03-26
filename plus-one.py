class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
		length = len(digits)
		if length == 0:
			return [1]
		elif digits[length - 1] < 9:
			digits[length - 1] = digits[length - 1] + 1
			return digits
		else:
			digits[length - 1] = 0
			aux = 1
			
			for i in range (length - 2, -1, -1):
				#print(digits[i], aux)
				if digits[i] + aux >= 10:
					digits[i] = 0
					aux = 1
				elif aux == 1:
					digits[i] = digits[i] + 1
					aux = 0
			
			if aux == 1:
				digits = [1] + digits
			return digits

ss = Solution()
d = [2,4,9,3,9]
d1 = [1]
d2 = [9, 999999999]
print(ss.plusOne(d))
print(ss.plusOne(d1))
print(ss.plusOne(d2))
