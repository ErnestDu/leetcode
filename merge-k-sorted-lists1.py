# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
	# @param a list of ListNode
	# @return a ListNode
	def mergeKLists(self, lists):
		a = []
		for i in range (0, len(lists)):
			p = lists[i]
			while p:
				a.append(p.val)
				p = p.next
		a.sort()
		if len(a) == 0:
			return None
		head = ListNode(a[0])
		p = head
		for i in range (1, len(a)):
			node = ListNode(a[i])
			p.next = node
			p = p.next
		return head

