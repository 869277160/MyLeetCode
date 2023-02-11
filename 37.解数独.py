'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:05:09
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-05 15:09:07
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
    def solveSudoku(self, board: List[List[str]]) -> None:
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
        
# @lc code=end

