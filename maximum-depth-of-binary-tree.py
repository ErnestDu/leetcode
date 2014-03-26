# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
	# @return an integer
	def maxDepth(self, root):
		if root == None:
			return 0
		else:
			ldepth = self.maxDepth(root.left)
			rdepth = self.maxDepth(root.right)
			return max(ldepth, rdepth) + 1
