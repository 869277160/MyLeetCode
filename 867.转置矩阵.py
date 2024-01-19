'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:16:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-10-23 11:49:12
FilePath: \Leetcode_Solver\867.转置矩阵.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        # res = []
        # for i in range(len(matrix[0])):
        #     res.append([])
        #     for j in range(len(matrix)):
        #         res[i].append(matrix[j][i])
        # return res 
        
        return  list(zip(*matrix))
        
# @lc code=end

