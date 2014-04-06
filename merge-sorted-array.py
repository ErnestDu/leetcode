## WA
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
		p = 0
		for i in range (0, n):
			if B[i] >= A[-1]:
				for j in range (i, n):
					A.append(B[j])
				break

			j = p
			while A[j] <= B[i]:
				j += 1
			## A[j] > B[i]
			A.append(A[len(A) - 1])
			for k in range (len(A) - 1, j, -1):
				A[k] = A[k-1]
			A[j] = B[i]
			p = j
		print(A)
A = [2, 4, 5, 9, 11, 17]
B = [6, 8, 10, 14]
s = Solution()
print(s.merge(A, len(A), B, len(B)))
