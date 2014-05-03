# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
	def createBST(self, num):
		if len(num) == 0:
			return None
		if len(num) == 1:
			newNode = TreeNode(num[0])
		mid = len(num) / 2
		root = TreeNode(num[mid])
		root.left = self.createBST(num[:mid])
		root.right = self.createBST(num[mid+1:])
		return root
	def sortedArrayToBST(self, num):
		return self.createBST(num)
