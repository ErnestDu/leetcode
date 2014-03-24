# http://oj.leetcode.com/problems/climbing-stairs/
# ref: http://blog.csdn.net/kenden23/article/details/17377869
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
		res = []
		res.append(1)
		res.append(1)
		for i in range (2, n+1):
			res.append(res[i - 1] + res[i - 2])
		return res[n]
ss = Solution()
n = int(input())
print(ss.climbStairs(n))
