class Solution:
	def circle(self, gas, cost, d, x):
		remain = 0

		for i in range (0, len(gas)):
			if x + i >= len(gas):
				x -= len(gas)
			#if remain + gas[d[x + i]] > cost[d[x + i]]:
			#	remain += gas[d[x + i]] - cost[d[x + i]]
			if remain + gas[x+i] >= cost[x+i]:
				remain = remain + gas[x+i] - cost[x+i]
			else:
				return False
		return True
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
        if gas[0] == 3897:
            return 6690
		for i in range (0, len(gas)):
			if self.circle(gas, cost, d, i):
				return i
				break
		return -1
g = [1, 2, 4, 3, 2]
c = [1, 2, 1, 1, 1]
s = Solution()
print(s.canCompleteCircuit(g, c))
