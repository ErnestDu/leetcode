# http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
	# @param A a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		p = 0
		length = len(A)
		if length < 3:
			return length
		while p <= length - 3:
			if A[p] == A[p+1] and A[p] == A[p+2]:
				i = p + 2
				del(A[p+2])
				length -= 1
			else:
				p += 1
		#print(A)
		return length
s = Solution()
A = [1,1,1,2,2,3]
print(s.removeDuplicates(A))
