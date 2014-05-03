# http://oj.leetcode.com/problems/linked-list-cycle-ii/
# http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return a list node
	def detectCycle(self, head):
		if head == None:
			return None
		fast = head
		slow = head
		hasCycle = 0
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				hasCycle = 1
				break
		if hasCycle == 0:
			return None
		slow = head
		while slow != fast:
			slow = slow.next
			fast = fast.next
		return fast
