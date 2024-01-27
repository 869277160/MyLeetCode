'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-08-25 16:14:07
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-08-25 17:58:51
FilePath: \Leetcode_Solver\52.n-皇后-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1 :
            return 1
        elif n ==2 or n ==3 :
            return 0
        else:
            self.res = 0
            board = [["."]* n for _ in range(n)]
            self.backtrackForTotalNQueen(board,0)
            return self.res
            
    def backtrackForTotalNQueen(self, board, row):
        total_row = len(board)
        if row == total_row:
            # print(board)
            # print()
            self.res += 1
            return 
        
        for col in range(total_row):
            # print(board)
            if self.isValid(board,row,col):
                board[row][col] = "Q"
                self.backtrackForTotalNQueen(board, row+1)
                board[row][col] = "."
                
    
    def isValid(self,board,row,col):
        n = len(board)
        
        for i in range(row):
            if board[i][col] == "Q":
                return False 
        
        # 检测右上是否有
        count = min(row,n-1-col)
        # print(count)
        # count = count + 1 if count ==1 else count  # type: ignore
        if count != 0:
            i = 1 
            while i <= count:
                if board[row-i][col+i] == "Q":
                    return False 
                i += 1
            
        # 检测左上是否有
        count = min(row,col)
        # count = count + 1 if count ==1  else count # type: ignore
        if count !=0:
            i = 1 
            while i<= count:
                if board[row-i][col-i] == "Q":
                    return False 
                i += 1
        return True
        
# @lc code=end


if __name__ == "__main__":
    
    # s = Solution()
    # print(s.totalNQueens(4))
    
