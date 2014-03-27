# http://oj.leetcode.com/problems/subsets/
class Solution:
	# @param S, a list of integer
	# @return a list of lists of integer
	def uniq(input):
		output = []
		for x in input:
			if x not in output:
				output.append(x)
		return output
	def subSet(self, S, x):
		bstr = bin(x)[2:]
		#print(bstr)
		s = ["0"] * len(S)
		j = 0
		for i in range (len(bstr) - 1, -1 , -1):
			#print(bstr[i])
			s[len(s) - 1 - j] = bstr[i]
			j = j + 1
		#print(s)
		ss = []
		for i in range (0, len(s)):
			if s[i] == "1":
				ss.append(S[i])
		#print(ss)
		return ss

	def subsets(self, S):
		S.sort()
		ss = []
		if len(S) == 0:
			return [[]]
		#prev  = [-1]
		for i in range (0, pow(2, len(S))):
			#print("i: ", i)
			x = self.subSet(S, i)
			#if x != prev:
			ss.append(x)
			#	prev = x
		output = []
		for i in range(0, len(ss)):
			if output.count(ss[i]) <= 0:
				output.append(ss[i])
		return output

ss = Solution()
a = [1,2,3,4]
print(ss.subsets(a))
b =  [1, 2, 2]
print(ss.subsets(b))
