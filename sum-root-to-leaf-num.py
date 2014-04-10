# http://oj.leetcode.com/problems/reorder-list/
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def traversal(self, root, s, paths):
		if root:
			if root.left:
				temp = s
				temp += str(root.val)
				self.traversal(root.left, temp, paths)
			if root.right:
				temp = s
				temp += str(root.val)
				self.traversal(root.right, temp, paths)
			if root.right == None and root.left == None:
				temp = s
				temp += str(root.val)
				paths.append(temp)

    # @param root, a tree node
    # @return an integer
	def sumNumbers(self, root):
		paths = []
		s = ""
		if root == None:
			return 0
		self.traversal(root, s, paths)
		ss = 0
		for i in range (0, len(paths)):
			ss += int(paths[i])
		return ss
