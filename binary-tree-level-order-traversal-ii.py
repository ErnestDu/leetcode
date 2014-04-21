# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def traversal(self, root, h, a):
		if root:
			if len(a) < h + 1:
				a.append([])
			a[h].append(root.val)
			if root.left:
				self.traversal(root.left, h + 1, a)
			if root.right:
				self.traversal(root.right, h + 1, a)
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrderBottom(self, root):
		if root == None:
			return []
		a = []
		b = []
		a.append(b)
		self.traversal(root, 0, a)
		a.reverse()
		return a

n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

s = Solution()
print(s.levelOrderBottom(n1))
print(s.levelOrderBottom(n5))
