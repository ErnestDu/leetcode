## wrong answer
# http://oj.leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param a list of ListNode
	# @return a ListNode
	def mergeKLists(self, lists):
		ln = len(lists)
		if ln == 0:
			return None
		end = 0
		flag = 0
		while end == 0:
			for i in range (0, ln):
				val = []
				p = []
				if lists[i]:
					val.append(lists[i].val)
					p.append(i)
				if len(val) == 0:
					end = 1
					break
				if min(val) == None:
					end = 1
					break
				n = ListNode(min(val))
				if flag == 0:
					head = ListNode(min(val))
					q = head
					flag = 1
				else:
					q.next = n
					q = q.next
				x = p[val.index(min(val))]
				lists[x] = lists[x].next
				end = 1
				for i in range (0, ln):
					if lists[i] != None:
						end = 0
						break
		if flag == 1:
			return head
		else:
			return None

lists = []
n1 = ListNode(1)
lists.append(n1)

s = Solution()
print(s.mergeKLists(lists))
