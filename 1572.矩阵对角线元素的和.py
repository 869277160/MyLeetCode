'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 15:16:02
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 15:19:35
FilePath: \Leetcode_Solver\1572.矩阵对角线元素的和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        if len(mat) == 1:
            return mat[0][0]
        
        if len(mat) %2 == 0:
            p_diag = [mat[i][i] for i in range(len(mat))]
            s_diag = [mat[i][len(mat)-1-i] for i in range(len(mat))]
            return sum( p_diag) + sum(s_diag)

        if len(mat) %2 == 1:
            p_diag = [mat[i][i] for i in range(len(mat))]
            s_diag = [mat[i][len(mat)-1-i] for i in range(len(mat))]
            return sum(p_diag) + sum(s_diag) - mat[len(mat)//2][len(mat)//2]
        
        
        
        
# @lc code=end

