# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
	# @return an integer
	def minDepth(self, root):
		if root == None:
			return 0
		else:
			ldepth = rdepth = 0
			if root.left and root.right:
				ldepth = self.minDepth(root.left)
				rdepth = self.minDepth(root.right)
				return min(ldepth, rdepth) + 1
			elif root.left:
				ldepth = self.minDepth(root.left)
				return ldepth + 1
			elif root.right:
				rdepth = self.minDepth(root.right)
				return rdepth + 1
			else:
				return 1
