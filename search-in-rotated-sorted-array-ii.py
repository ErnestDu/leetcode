class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if A.count(target) > 0:
            return True
        else:
            return False
