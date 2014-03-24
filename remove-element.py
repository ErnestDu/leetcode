## http://oj.leetcode.com/problems/remove-element/
#!/bin/env python2
class 
	def removeElement(self, A, elem):
		cc = A.count(elem) 
		## remove cc elems from A
		for i in range (0, cc):
			A.remove(elem)
		return len(A)