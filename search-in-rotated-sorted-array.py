class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if A.count(target) > 0:
            return A.index(target)
        else:
            return -1
