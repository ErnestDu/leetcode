class Solution:
	# @param strs, a list of strings
	# @return a list of strings
	def anagrams(self, strs):
		#print(strs)
		ss = []
		i = 0
		for s in strs:
			temp = []
			for c in s:
				temp.append(c)
			temp.sort()
			s = ""
			for c in temp:
				s += c
			ss.append((s,i))
			i += 1
		#print(ss)
		ss.sort()
		#print(ss)
		index = []
		p = 0
		for i in range (1, len(ss)):
			if ss[i][0] == ss[i-1][0]:
				if i - 1 == p:
					index.append(ss[i-1][1])
				index.append(ss[i][1])
			else:
				p = i
		
		#print(index)
		res = []
		for i in index:
			res.append(strs[i])
		return res

s = Solution()
a = ["tea","and","ate","eat","dan"]
print(s.anagrams(a))
