class Solution:
	# @return an integer
	def maxArea(self, height):
		mx = 0
		start = 0
		end = len(height) - 1
		while start < end:
			area = min(height[end], height[start]) * (end - start)
			mx = max(mx, area)
			if height[start] <= height[end]:
				start += 1
			else:
				end -= 1
		return mx

s = Solution()
a = [1, 8, 4, 9]
print(s.maxArea(a))
