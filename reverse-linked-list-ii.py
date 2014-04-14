# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @param m, an integer
	# @param n, an integer
	# @return a ListNode
	def reverseBetween(self, head, m, n):
		if head == None:
			return None
		count = 1
		p = head
		a = []
		while p:
			if count >= m and count <= n:
				a.append(p)
			p = p.next
			count += 1
		ln = len(a)
		for i in range (0, ln / 2):
			# a[i], a[ln -1 - i]
			temp = a[i].val
			a[i].val = a[ln-1-i].val
			a[ln-1-i].val = temp
		return head
