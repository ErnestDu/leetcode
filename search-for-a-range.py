# http://oj.leetcode.com/problems/search-for-a-range/
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
		if len(A) == 0:
			return [-1, -1]
		start = 0
		end = len(A) - 1
		while end > start:
			mid = (start + end) / 2
			print(start, end, mid)
			if A[mid] >= target:
				end = mid
			else:
				start = mid
		if A[start] == target:
			return start
		elif A[start + 1] == target:
			return start + 1
a = [5, 7, 7, 8, 8, 10]
target = 8
s = Solution()
print(s.searchRange(a, target))
