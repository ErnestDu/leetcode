# http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if len(prices) <= 0:
			return 0
		mn = prices[0]
		mp = 0
		for i in range (0, len(prices)):
			if prices[i] - mn > mp:
				mp = prices[i] - mn
			if prices[i] < mn:
				mn = prices[i]
		return mp
s = Solution()
a = [9,8,7,6]
print(s.maxProfit(a))
