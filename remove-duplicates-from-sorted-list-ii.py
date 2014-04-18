# http://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
	# @return a ListNode
    def deleteDuplicates(self, head):
		if head == None:
			return None
		a = []
		x = None
		p = head
		while p:
			if p.val != x:
				if p.next and p.next.val != p.val:
					a.append(p.val)
				elif p.next == None:
					a.append(p.val)
				x = p.val
			p = p.next
		if len(a) == 0:
			return None
		new = ListNode(a[0])
		p = new
		for i in range (1, len(a)):
			node = ListNode(a[i])
			p.next = node
			p = p.next
		return new

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(1)
n4 = ListNode(2)
n5 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

h2 = ListNode(1)
n6 = ListNode(2)
n7 = ListNode(2)
h2.next = n6
n6.next = n7
s = Solution()
a = s.deleteDuplicates(n1)
p = a
while p:
	print(p.val)
	p = p.next
