# http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
	def removeDuplicates(self, A):
		B = []
		if len(A) == 0:
			return 0
		p = A[0] - 1 
		for i in range (0, len(A)):
			if A[i] != p:
				B.append(A[i])
				p = A[i]
		for i in range (0, len(B)):
			A[i] = B[i]
		
		return len(B)
A = [1,1,2]


s = Solution()

print(s.removeDuplicates(A))

print(A)
