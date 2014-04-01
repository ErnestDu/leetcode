# http://oj.leetcode.com/problems/restore-ip-addresses/
class Solution:
	# @param s, a string
	# @return a list of strings
	def valid(self, x):
		if len(x) > 1:
			if x[0] == "0":
				return False
		if int(x) <= 255 and int(x) >= 0:
			return True
			
		return False
	def restoreIpAddresses(self, s):
		validIp = []
		for a in range (1, 4):
			for b in range (1, 4):
				for c in range (1, 4):
					for d in range (1, 4):
						ip1 = s[0: a]
						ip2 = s[a: a + b]
						ip3 = s[a + b: a + b + c]
						ip4 = s[a + b + c: a + b + c + d]
						if len(ip1) * len(ip2) * len(ip3) * len(ip4) != 0 and len(ip1+ip2+ip3+ip4) == len(s):
							if self.valid(ip1) and self.valid(ip2) and self.valid(ip3) and self.valid(ip4):
								x = ip1 + "." + ip2 + "." + ip3 + "." + ip4
								if validIp.count(x) == 0:
								 	validIp.append(x)
		return validIp

s = Solution()
x = "25525511135"
print(s.restoreIpAddresses(x))


		
