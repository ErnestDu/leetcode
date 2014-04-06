# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
		if l1 == None:
			return l2
		elif l2 == None:
			return l1
		node = None
		while l1 != None and l2 != None:
			if l1.val <= l2.val:
				if node == None:
					node = l1
					head = node
				else:
					node.next = l1
					node = node.next
				l1 = l1.next
			else:
				if node == None:
					node = l2
					head = node
				else:
					node.next = l2
					node = node.next
				l2 = l2.next

		if l1 != None:
			node.next = l1
		elif l2 != None:
			node.next = l2

		return head
