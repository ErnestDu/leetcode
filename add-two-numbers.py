# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @return a integer
	def getNumber(self, head):
		digits = []
		p = head
		while p != None:
			digits.append(p.val)
			p = p.next
		digits.reverse()
		s = ""
		for i in range (0, len(digits)):
			s += str(digits[i])
		return int(s)
	
	def numToList(self, num):
		s = str(num)
		i = 0
		p = None
		while i < len(s):
			temp = ListNode(s[i])
			temp.next = p
			p = temp
			i += 1
		return p

    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
		a = self.getNumber(l1)
		b = self.getNumber(l2)
		return self.numToList(a + b)
