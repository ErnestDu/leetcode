# http://oj.leetcode.com/problems/valid-sudoku/
class Solution:
	# @param board, a 9x9 2D array
	# @return a boolean
	def validate(self, a):
		for i in range (0, 10):
			if a.count(str(i)) > 1:
				#print(a, False)
				return False
		#print(a, True)
		return True
	def isValidSudoku(self, board):
		# validate each row
		for i in range (0, 9):
			if self.validate(board[i]) == False:
				return False
		for i in range (0, 9):
			a = []
			for j in range (0, 9):
				a.append(board[j][i])
			if self.validate(a) == False:
				return False
		for i in range (0, 9, 3):
			for j in range (0, 9, 3):
				b = []
				for x in range (0, 3):
					for y in range (0, 3):
						b.append(board[i+x][j+y])
				if self.validate(b) == False:
					return False
		return True

a = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
s = Solution()
print(s.isValidSudoku(a))
