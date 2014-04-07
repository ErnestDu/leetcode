## http://oj.leetcode.com/problems/linked-list-cycle/
## http://leetcode.com/2010/09/detecting-loop-in-singly-linked-list.html
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
		if head == None:
			return False
		fast = head
		slow = head
		while fast and slow and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		return False
