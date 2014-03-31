class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
		if len(needle) > 0:
	 		for i in range (0, len(haystack)):
				#print("haystack", i, haystack[i])
				if haystack[i] == needle[0]:
					#print(haystack[i:i + len(needle)])
					if haystack[i: i + len(needle)] == needle:
						return haystack[i:]
		elif len(needle) == 0:
			return haystack
		return None

ss = Solution()
h = "hello, world"
n = "wor"
print(ss.strStr(h, n))
