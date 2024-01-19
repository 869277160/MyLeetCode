'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:01:36
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:08:48
FilePath: \Leetcode_Solver\1380.矩阵中的幸运数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        min_er = [min(r) for r in matrix]
        m = len(matrix)
        n = len(matrix[0])
        
        res = []
        for i in range(n):
            row = [matrix[j][i] for j in range(m)]
            current_max = max(row)
            if current_max in min_er:
                res.append(current_max)
        
        return res 
        
        # row = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         row
        # row = [matrix[i][j] for i in range(len(matrix))]
        # miner = [min([])]
        # min_er = [min(c) for c in zip(*matrix)]
        
        # return list(set(max_er) & set(min_er))
        
        
        
# @lc code=end

