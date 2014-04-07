# http://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
	# @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        new = ListNode(head.val)
        prev = head.val
        i = head.next
        j = new
        while i != None:
            if i.val == prev:
                pass
            
            else:
                temp = ListNode(i.val)
                j.next = temp
                j = j.next
                prev = i.val
            i = i.next
        return new
