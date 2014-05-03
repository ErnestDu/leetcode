# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def f(self, root, sibling):
		if root == None:
			return 0
		else:
			root.next = sibling
			self.f(root.left, root.right)
			if sibling:
				self.f(root.right, sibling.left)
			else:
				self.f(root.right, None)
	# @param root, a tree node
	# @return a list of lists of integers
	def connect(self, root):
		self.f(root, None)

		
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
print(s.connect(n1))
