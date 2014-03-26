class Solution:
	# @param A, a list of integers
	# @return nothing, sort in place
	def sortColors(self, A):
		c0 = A.count(0)
		c1 = A.count(1)
		for i in range (0, c0):
			A[i] = 0
		for i in range (c0, c0 + c1):
			A[i] = 1
		for i in range (c0 + c1, len(A)):
			A[i] = 2
