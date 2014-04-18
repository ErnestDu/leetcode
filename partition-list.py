# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param x, an integer
	# @return a ListNode
	def partition(self, head, x):
		if head == None:
			return None

		p = head
		f1 = 0
		f2 = 0
		while p:
			node = ListNode(p.val)
			if p.val < x:
				if f1 == 1:
					p1.next = node
					p1 = p1.next
				if f1 == 0:
					h1 = node
					p1 = h1
					f1 = 1
			elif p.val >= x:
				if f2 == 1:
					p2.next = node
					p2 = p2.next
				if f2 == 0:
					h2 = node
					p2 = h2
					f2 = 1
			p = p.next
		
		if f1 == 1 and f2 == 1:
			p1.next = h2
			return h1
		elif f1 == 0:
			return h2
		elif f2 == 0:
			return h1

n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

s = Solution()
print(n1)
l = s.partition(n1, 3)
p = l
while p:
	print(p.val)
	p = p.next
