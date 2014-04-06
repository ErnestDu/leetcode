class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		if len(triangle) < 1:
			return 0
		elif len(triangle) == 1:
			return triangle[0][0]
		for i in range (1, len(triangle)):
			triangle[i][0] += triangle[i - 1][0]
			triangle[i][i] += triangle[i-1][i-1] 
			for j in range (1, i):
				triangle[i][j] = triangle[i][j] + min(triangle[i-1][j-1], triangle[i-1][j])
		return min(triangle[-1])
t = [[2], [3,4], [6,5,7],[4,1,8,3]]
s = Solution()
print(s.minimumTotal(t))

