# http://oj.leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param head, a ListNode
	# @param k, an integer
	# @return a ListNode
	def rotateRight(self, head, k):
		if head == None or k == 0:
			return head
		count = 0
		p = head
		while p:
			count += 1
			q = p
			p = p.next
		q.next = head
		p = head
		k = k % count
		x = count - k - 1
		while x > 0:
			p = p.next
			x -= 1
		head = p.next 
		p.next = None
		return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
l = s.rotateRight(n1, 5)
p = l
while p:
	print(p.val)
	p = p.next
