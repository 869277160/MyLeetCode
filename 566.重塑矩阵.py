'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 20:42:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:48:07
FilePath: \Leetcode_Solver\566.重塑矩阵.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m,n = len(mat), len(mat[0])
        total_len = m*n
        if total_len != r*c:
            return mat
        else :
            mat_list = [mat[i][j] for i in range(m) for j in range(n)]
            if m == r:
                return mat
            if r ==1 :
                return [mat_list] 
            if c == 1:
                return [[i] for i in mat_list]
            
            res= [mat_list[i*c:(i+1)*c] for i in range(r)]
            return res
        
# @lc code=end

