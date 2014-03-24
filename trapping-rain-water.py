# http://oj.leetcode.com/problems/trapping-rain-water/
class Solution:
	# @param A, a list of integers
	# @return an integer
	def trap(self, A):
		l = []
		m = 0
		for i in range (0, len(A)):
			l.append(m)
			if m < A[i]:
				m = A[i]
		#print(l)
		r = []
		m = 0
		for i in range (len(A) - 1, -1, -1):
			r.append(m)
			if m < A[i]:
				m = A[i]
		
		#print(r)
		for i in range (0, len(r) / 2):
			temp = r[i]
			r[i] = r[len(r) - 1 - i]
			r[len(r) - 1 - i] = temp
		#print(r)
		
		ss = 0
		for i in range (0, len(A)):
			x = l[i] - A[i]
			y = r[i] - A[i]
			#print(i, x, y)
			if x > y and y > 0:	
				ss = ss + y
			elif y >= x and x > 0:
				ss = ss + x

		return ss

s = Solution()
A = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(A))

