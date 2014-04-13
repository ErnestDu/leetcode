# http://oj.leetcode.com/problems/swap-nodes-in-pairs/
# Definition for  singly-linked list
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param a ListNode
	# @return a ListNode
	def swapPairs(self, head):
		if head == None or head.next == None:
			return head
		p = head
		while p and p.next:
			temp = p.val
			p.val = p.next.val
			p.next.val = temp
			p = p.next.next
		return head

