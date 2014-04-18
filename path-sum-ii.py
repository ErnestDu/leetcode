# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def traversal(self, root, sum, a, path):
		temp = path[::]
		if root:
			temp.append(root.val)
			if root.left == None and root.right == None:
				if root.val == sum:
					a.append(temp)
			if root.left:
				self.traversal(root.left, sum - root.val, a, temp)
			if root.right:
				self.traversal(root.right, sum - root.val, a, temp)
	def pathSum(self, root, sum):
		if root == None:
			return []
		a = []
		path = []
		self.traversal(root, sum, a, path)
		return a

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(1)
root.left = node1
root.right = node2
node1.right = node3
s = Solution()
print(s.pathSum(root, 4))
