# http://oj.leetcode.com/problems/search-insert-position/
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
		try:
			pos = A.index(target)
			return pos
		except ValueError:
			for i in range (0, len(A)):
				 if target < A[i]:
					return i
			return len(A)

ss = Solution()
a = [1,3,5,6]
x = int(input())

print(ss.searchInsert(a, x))
