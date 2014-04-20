# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param head, a ListNode
	# @return nothing
	def reorderList(self, head):
		if head == None:
			return None
		p = head
		count = 0
		a = []
		while p:
			count += 1
			a.append(p)
			p = p.next
		if count <= 2:
			return head

		n = int(count / 2)
		p = head
		i = 0
		while n:
			a[count-1-i].next = p.next
			p.next = a[count-1-i]
			p = a[count-1-i].next
			q = a[count-1-i]
			i += 1
			n -= 1
		#print(q.val)
		if count % 2 == 0:
			q.next = None
		else:
			p.next = None
		return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

s = Solution()
l = s.reorderList(n1)
p = l
while p:
	print(p.val)
	p = p.next
