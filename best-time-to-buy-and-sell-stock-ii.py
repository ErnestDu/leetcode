# http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit1(self, prices):
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
	def maxProfit(self, prices):
		if len(prices) <= 0:
			return 0
		mp = 0
		for i in range (0, len(prices) - 1):
			mp += self.maxProfit1(prices[i:i+2])
		return mp
s = Solution()
a = [1,5,4,6, 7]
print(s.maxProfit(a))
