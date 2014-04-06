class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, m, n):
		grid = [[0] * n] * m
		for i in range (0, n):
			grid[0][i] = 1
		for i in range (0, m):
			grid[i][0] = 1
		for i in range (1, m):
			for j in range (1, n):
				grid[i][j] = grid[i-1][j] + grid[i][j-1]
		return grid[m-1][n-1]
		
m = 1
n = 1
s = Solution()
print(s.minPathSum(m, n))
