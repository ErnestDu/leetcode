class Solution:
	def isValidBST(self, root):
		return self.isValidBSTImpl(root, -2**31, 2**31 - 1)
	
	def isValidBSTImpl(self, root, min, max):
		if root == None:
			return True
		return root.val > min and root.val < max \
				and self.isValidBSTImpl(root.left, min, root.val) \
				and self.isValidBSTImpl(root.right, root.val, max)
