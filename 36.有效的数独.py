#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check row
        for row in board:
            if not self.Checker(row):
                return False

        # check column
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if not self.Checker(column):
                return False

        # check sub-box
        for i in range(3):
            for j in range(3):
                sub_box = [board[m][n] for m in range(i*3, (i+1)*3) for n in range(j*3, (j+1)*3)]
                if not self.Checker(sub_box):
                    return False

        return True
        
        
    def Checker(self,row:list):
        for i in range(9):
            if row[i] == '.':
                continue
            if row[i] in row[i+1:]:
                return False
        
        return True

# @lc code=end

