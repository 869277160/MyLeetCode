'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-27 16:06:47
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-27 17:04:00
FilePath: \Leetcode_Solver\542.01-矩阵.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
    
        new_mat = [[-1 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0 and new_mat[i][j] == -1:
                    new_mat[i][j] = 0
                    new_mat = self.traverse(mat, new_mat, i+1,j, 1)
                    new_mat = self.traverse(mat, new_mat, i,  j-1, 1)
                    new_mat = self.traverse(mat, new_mat, i-1,j, 1)
                    new_mat = self.traverse(mat, new_mat, i,  j+1, 1)
        return new_mat
    
    
    def traverse(self, mat, input_mat, input_row, input_col, current_step):
        # print(input_mat, input_row, input_col, current_step)
        # 不合理路径
        if input_row < 0 or input_row >= len(mat) or input_col < 0 or input_col >= len(mat[0]):
            return input_mat
        # 更新过了则返回
        if input_mat[input_row][input_col] == -1:
            
            # 根据当前位置继续扫描
            if mat[input_row][input_col] == 0:
                input_mat[input_row][input_col] = 0
                input_mat = self.traverse(mat, input_mat, input_row+1, input_col, 1)
                input_mat = self.traverse(mat, input_mat, input_row, input_col-1, 1)
                input_mat = self.traverse(mat, input_mat, input_row-1, input_col, 1)
                input_mat = self.traverse(mat, input_mat, input_row, input_col+1, 1)
                return input_mat
            else:
                temp = []
                input_mat[input_row][input_col] = current_step
                input_mat = self.traverse(mat, input_mat, input_row+1, input_col, current_step+1)
                # temp.append(new_mat[input_row][input_col])
                input_mat = self.traverse(mat, input_mat, input_row, input_col+1, current_step+1)
                # temp.append(new_mat[input_row][input_col])
                input_mat = self.traverse(mat, input_mat, input_row-1, input_col, current_step+1)
                # temp.append(new_mat[input_row][input_col])
                input_mat = self.traverse(mat, input_mat, input_row, input_col-1, current_step+1)
                # temp.append(new_mat[input_row][input_col])
                # near_min = min(temp) + 1
                # input_mat[input_row][input_col] = min(input_mat[input_row][input_col], near_min)
                
                
                return input_mat
        else :
            if mat[input_row][input_col] == 1:
                # 是否有更好的解决方案？
                row, col = len(mat), len(mat[0])
                temp = []
                if input_row - 1 >= 0:
                    if input_mat[input_row - 1][input_col] != -1:
                        temp.append(input_mat[input_row - 1][input_col])
                if input_row + 1 < row:
                    if input_mat[input_row + 1][input_col] != -1:
                        temp.append(input_mat[input_row + 1][input_col])
                if input_col - 1 >= 0:
                    if input_mat[input_row ][input_col - 1] != -1:
                        temp.append(input_mat[input_row ][input_col- 1])
                if input_col + 1 < col:
                    if input_mat[input_row][input_col + 1] != -1:
                        temp.append(input_mat[input_row][input_col + 1])
                near_min = min(temp) + 1
                input_mat[input_row][input_col] = min(input_mat[input_row][input_col], near_min)
            
            return input_mat
         
# @lc code=end

