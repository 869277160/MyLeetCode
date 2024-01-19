'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 10:38:09
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 10:43:25
FilePath: \Leetcode_Solver\766.托普利茨矩阵.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        res = []
        for i in range(50):
            res.append([])
        
        for i in range(m):
            for j in range(n):
                if res[25 + (i - j)] == []:
                    res[25 + (i - j)].append(matrix[i][j])
                else :
                    if res[25 + (i - j)][0] != matrix[i][j]:
                        return False
                    else:
                        res[25 + (i - j)].append(matrix[i][j])
                        
        return True
# @lc code=end

