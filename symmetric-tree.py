# Definaition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
	def isSym(self, left, right):
		if left == None and right == None:
			return True
		if (left == None and right != None) or (left != None and right == None):
			return False
		if left.val != right.val:
			return False
		return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)
    def isSymmetric(self, root):
		if root == None:
			return True
		return self.isSym(root.left, root.right)
