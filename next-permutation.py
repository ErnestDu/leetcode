class Solution:
	def hasPermutation(self, num):
		for i in range (len(num) - 1, 0, -1):
			if num[i] > num[i-1]:
				return True
		return False
	def permute(self, num):
		x = num[0] 
		num.sort()
		i= num.index(x) + 1
		while num[i] <= x:
			i += 1
		temp = num[i]
		del(num[i])
		return [temp]+num
	# @param num, a list of integer
	# @return a list of integer
	def nextPermutation(self, num):
		if len(num) <= 1:
			return num
		if len(num) == 2:
			return num[::-1]
		flag = 0
		for i in range (len(num) - 2, -1, -1):
			if self.hasPermutation(num[i::]):
				s = num[:i] + self.permute(num[i::])
				flag = 1
				break
		if flag == 0:
			return num[::-1]
		else:
			return s 
s = Solution()
a = [1, 3, 2]
a2 = [3, 2, 1]
a3 = [1, 5, 1]
print(s.nextPermutation(a))
print(s.nextPermutation(a2))
print(s.nextPermutation(a3))
