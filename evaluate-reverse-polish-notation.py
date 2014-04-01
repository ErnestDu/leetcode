# http://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
	# @param tokens, a list of string
	# @return an integer
	def evalRPN(self , tokens):
		if len(tokens) == 0:
			return None
		elif len(tokens) == 1:
			return int(tokens[0])
		elif len(tokens) == 2:
			return None
		while len(tokens) != 1:
			#print(tokens)
			for i in range (0, len(tokens)):
				x = tokens[i]
				if x == "+":#  or x == "-" or x == "*" or x == "/":
					tokens[i] = int(tokens[i - 2]) + int(tokens[i - 1])
					del(tokens[i-1])
					del(tokens[i-2])
					break
				elif x == "-":
					tokens[i] = int(tokens[i - 2]) - int(tokens[i - 1])
					del(tokens[i-1])
					del(tokens[i-2])
					break
				elif x == "*":
					tokens[i] = int(tokens[i - 2]) * int(tokens[i - 1])
					del(tokens[i-1])
					del(tokens[i-2])
					break
				elif x == "/":
					tokens[i] = int(float(tokens[i-2]) / float(tokens[i-1]))
					del(tokens[i-1])
					del(tokens[i-2])
					break 
		return tokens[0]
s = Solution()
a = ["2", "1", "+", "3", "*"]
b = ["4", "13", "5", "/", "+"]
print(s.evalRPN(a))
print(s.evalRPN(b))
