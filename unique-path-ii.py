class Solution:
	# @param obstacleGrid, a list of lists of integers
	# @return an integer
	def uniquePathsWithObstacles(self, obstacleGrid):
		m = len(obstacleGrid)
		if m < 0:
			return None
		n = len(obstacleGrid[0])
		if 	obstacleGrid[0][0] != 1:
			obstacleGrid[0][0] = 1
		else:
			return 0
		
		for i in range (1, m):
			if obstacleGrid[i][0] == 1:
				obstacleGrid[i][0] = 0
			else:
				if obstacleGrid[i-1][0] == 1:
					obstacleGrid[i][0] = 1
				else:
					obstacleGrid[i][0] = 0
		
		for i in range (1, n):
			if obstacleGrid[0][i] == 1:
				obstacleGrid[0][i] = 0
			else:
				if obstacleGrid[0][i-1] == 1:
					obstacleGrid[0][i] = 1
				else:
					obstacleGrid[0][i] = 0
		#print(obstacleGrid)
		for i in range (1, m):
			for j in range (1, n):
				if obstacleGrid[i][j] == 1:
					obstacleGrid[i][j] = 0
				else:
					obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
		#print(obstacleGrid)
		return obstacleGrid[m-1][n-1]
s = Solution()
a = [[0,0,0], [0,1,0],[0,0,0]]
print(s.uniquePathsWithObstacles(a))
