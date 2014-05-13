class Solution:
	# @return an integer
	def minDistance(self, word1, word2):
		f = []
		for i in range (0, len(word1) + 1):
			temp = [0] * (len(word2) + 1)
			f.append(temp)
		for i in range (0, len(word1) + 1):
			f[i][0] = i
		for j in range (0, len(word2) + 1):
			f[0][j] = j
		
		for i in range (1, len(word1) + 1):
			for j in range (1, len(word2) + 1):
				if word1[i-1] == word2[j-1]:
					f[i][j] = f[i-1][j-1]
				else:
					mn = min(f[i-1][j], f[i][j-1])
					f[i][j] = 1 + min(f[i-1][j-1], mn)
		return f[len(word1)][len(word2)]

s = Solution()
a = raw_input()
b = raw_input()
print(s.minDistance(a, b))
