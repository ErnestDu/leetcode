# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	def f(self, root, tail):
		if root == None:
			return tail
		root.right = self.f(root.left, self.f(root.right, tail))
		root.left = None
		return root
	# @param root, a tree node
	# @return nothing, do it in place
	def flatten(self, root):
		self.f(root, None)
