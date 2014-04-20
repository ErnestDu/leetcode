class Solution:
	# @param path, a string
	# @return a string
	def simplifyPath(self, path):
		if len(path) == 0:
			return "/"
		a = path.split('/' or '.')
		b = []
		for i in range (0, len(a)):
			if a[i] != "":
				b.append(a[i])
		for i in range (0, len(b)):
			if b[i] == '.':
				b[i] = None
		#print(b)
		for i in range (0, len(b)):
			if b[i] == "..":
				b[i] = None
				for j in range (i - 1, -1, -1):
					if b[j] != None:
						b[j] = None
						break
		#print(b)
		s = ""
		for i in range (0, len(b)):
			if b[i] != None:
				s += "/" + b[i]

		#print(s, len(s))
		if len(s) == 0:
			return "/"
		else:
			return s
s = Solution()
p = "/a/.//b/../../c/"
p1 = "/home"
p2 = "/../"
print(s.simplifyPath(p))
print(s.simplifyPath(p1))
print(s.simplifyPath(p2))
