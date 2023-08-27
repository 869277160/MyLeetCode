'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:05:09
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-08-27 23:07:29
FilePath: \Leetcode_Solver\37.解数独.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j] == '.':
    #                 for num in range(1, 10):
    #                     if self.CheckLine(board, i, j, str(num)) and self.CheckColumn(board, i, j, str(num)) and self.CheckBlock(board, i - i % 3, j - j % 3, str(num)):
    #                         board[i][j] = str(num)
    #                         self.solveSudoku(board)
    #                         board[i][j] = '.'

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)
        
    def backtrack(self, board: List[List[str]], i:int, j:int) -> bool:
        row, col = 9, 9
        
        if j == col: return self.backtrack(board, i + 1, 0) # 穷举到最后一列的话就换到下一行重新开始。
        if i == row: return True      # 找到一个可行解，触发 base case
        
        if board[i][j] != '.':
            # 如果有预设数字，不用我们穷举
            return self.backtrack(board, i, j + 1)

        for ch in range(1, 10):
            ch = str(ch)
            # 如果该数字合法，则填入该数字并进一步向后搜索。
            if self.isValid(board, i, j, ch):
                board[i][j] = ch
                # 如果找到一个可行解，立即结束
                if self.backtrack(board, i, j + 1):
                    return True
                # 否则退回填入的数字，并重新进行输出
                board[i][j] = '.'
        # 穷举完 1~9，依然没有找到可行解，此路不通
        return False

    # 判断 board[i][j] 是否可以填入 n
    def isValid(self, board: List[List[str]], r: int, c: int, n: str) -> bool:
        for i in range(9):
            # 判断行是否存在重复
            if board[r][i] == n:
                return False
            # 判断列是否存在重复
            if board[i][c] == n:
                return False
            # 判断 3 x 3 方框是否存在重复
            if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                return False
        return True


    # def CheckLine(self, board, row, col, num):
    #     for i in range(9):
    #         if board[row][i] == num:
    #             return False
    #     return True
    # def CheckColumn(self, board, row, col, num):
    #     for i in range(9):
    #         if board[i][col] == num:
    #             return False
    #     return True
    # def CheckBlock(self, board, row, col, num):
    #     for i in range(3):
    #         for j in range(3):
    #             if board[row + i][col + j] == num:
    #                 return False
    #     return True
        
    # def solveSudoku(self, board: List[List[str]]) -> None:

    #     self.backtrackForSudoku(board,0)
            
    # def backtrackForSudoku(self, board, row):
    #     total_row = len(board)
    #     if row == total_row:
    #         print(board)
    #         print()
    #         self.res += 1
    #         return 
        
    #     for col in range(total_row):
    #         # print(board)
    #         if self.isValid(board,row,col):
    #             board[row][col] = "Q"
    #             self.backtrackForSudoku(board, row+1)
    #             board[row][col] = "."
                
    
    # def isValid(self,board,row,col):
    #     n = len(board)
        
    #     for i in range(row):
    #         if board[i][col] == "Q":
    #             return False 
        
    #     # 检测右上是否有
    #     count = min(row,n-1-col)
    #     # print(count)
    #     # count = count + 1 if count ==1 else count  # type: ignore
    #     if count != 0:
    #         i = 1 
    #         while i <= count:
    #             if board[row-i][col+i] == "Q":
    #                 return False 
    #             i += 1
            
    #     # 检测左上是否有
    #     count = min(row,col)
    #     # count = count + 1 if count ==1  else count # type: ignore
    #     if count !=0:
    #         i = 1 
    #         while i<= count:
    #             if board[row-i][col-i] == "Q":
    #                 return False 
    #             i += 1
    #     return True
# @lc code=end

