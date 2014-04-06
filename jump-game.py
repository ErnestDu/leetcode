# http://oj.leetcode.com/problems/jump-game/
class Solution:
	# @param A, a list of integers
	# @return a boolean
	def canJump(self, A):
		if len(A) <= 1:
			return True
		mx = 0
		for i in range (0, len(A)):
			if mx < i:
				return False
			else:
				if mx < i + A[i]:
					mx = i + A[i]
				if mx >= len(A) - 1:
					return True
a = [1]
b = [3, 2, 1, 0, 4]
c = [100, 2,3,4]
s = Solution()
print(s.canJump(a))
print(s.canJump(b))
print(s.canJump(c))
