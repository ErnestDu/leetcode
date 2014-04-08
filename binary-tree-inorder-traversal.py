# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traversal(self, root, a):
        if root:
            if root.left:
                self.traversal(root.left, a)
			a.append(root.val)
            if root.right:
                self.traversal(root.right, a)
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        a = []
        self.traversal(root, a)
        return a
