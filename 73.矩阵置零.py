'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-11 17:53:05
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-08-27 23:00:51
FilePath: \Leetcode_Solver\73.矩阵置零.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

# @lc app=leetcode.cn id=73 lang=python3

# [73] 矩阵置零


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
#         new_matrix = [[1]*len(matrix[0])] *len(matrix)
        
#         for i in range(len(matrix)):
#             if 0 in matrix[i]:
#                 new_matrix[i] =[1]*len(matrix[0])
        
        row,col = len(matrix), len(matrix[0])
        
        col_checker = [0] * col 
        
        for i in range(row):
            current_row = 0
            for j in range(col):
                if matrix[i][j] == 0:
                    current_row = 1 
                    col_checker[j] = 1
            if current_row:
                matrix[i] = [0]*col
                    # break
        
        for j in range(col):
            if col_checker[j]:
                for i in range(row):
                    matrix[i][j] = 0
                    
        return 
        


# @lc code=end

