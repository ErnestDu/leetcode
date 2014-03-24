# http://oj.leetcode.com/problems/length-of-last-word/
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        ss = s.split()
        if len(ss) == 0:
            return 0
        return len(ss[-1])
