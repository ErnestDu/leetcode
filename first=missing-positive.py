class Solution:
	# @param A, a list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		if len(A) == 0:
			return 1
		mx = max(A)
		if mx <= 0:
			return 1
		for i in range (1, mx):
			if A.count(i) == 0:
				return i
		return mx + 1

s = Solution()
A = [1, 1000]
B = [3, 4, -1, 1]
print(s.firstMissingPositive(A))
print(s.firstMissingPositive(B))
