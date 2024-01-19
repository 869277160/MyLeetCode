'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-08-31 10:21:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-10-23 15:46:49
FilePath: \Leetcode_Solver\48.旋转图像.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        s,e = 0,len(matrix)-1
        
        while (s < e):
            matrix[s], matrix[e] = matrix[e], matrix[s]
            s += 1
            e -= 1
        
        
        N = len(matrix[0])
        for i in range(N):
            for j in range(i+1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# @lc code=end

