class Solution:
	def longestConsecutive(self, num):
		num.sort() ## cheating here
		mx = 1
		count = 1
		i = 0
		if len(num) <= 1:
			return len(num)
		while i < len(num) and i + 1 < len(num):
			if num[i+1] == num[i] + 1:
				count += 1
			elif num[i+1] == num[i]:
				pass
			else:
				count = 1
			if mx < count:
				mx = count
			i += 1
		return mx

a = [1, 2, 0, 1]
s = Solution()
print(s.longestConsecutive(a))
