# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @return a ListNode
	def removeNthFromEnd(self, head, n):
		if head == None:
			return head
		p = head
		a = []
		while p:
			a.append(p)
			p = p.next
		ln = len(a)
		if n == 1:
			return None
		if n == 1:
			a[ln-2].next = None
			return head
		if n == ln:
			head = head.next
			return head
		x = ln - n
		a[x-1].next = a[x+1]
		return head
