# http://oj.leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def validate(self, root):
		if root == None:
			return 0
		lh = self.validate(root.left)
		rh = self.validate(root.right)
		if lh < 0 or rh < 0 or abs(lh - rh) > 1:
			return -1
		return max(lh, rh) + 1

	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		return self.validate(root) >= 0

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n4.right = n5
s = Solution()
print(s.isBalanced(n1))

