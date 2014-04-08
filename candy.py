# http://oj.leetcode.com/problems/candy/
class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		a = [1] * len(ratings)
		for i in range (1, len(a)):
			if ratings[i] > ratings[i-1] and a[i] <= a[i-1]:
				a[i] = a[i-1] + 1
		for i in range (len(a) - 1, 0, -1):
			if ratings[i-1] > ratings[i] and a[i-1] <= a[i]:
				a[i-1] = a[i] + 1
		#print(a)
		return sum(a)
r = [7, 6, 2, 1, 3]
x = [4, 2, 3, 4, 1]
s = Solution()
print(s.candy(r))
print(s.candy(x))
