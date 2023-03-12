'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:34:49
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:38:01
FilePath: \Leetcode_Solver\2319.判断矩阵是否是一个-x-矩阵.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2319 lang=python3
#
# [2319] 判断矩阵是否是一个 X 矩阵
#

# @lc code=start
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        duijiao = []
        rest = []
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i == j or i + j == len(grid) - 1:
                    if grid[i][j] == 0:
                        return False
                    # duijiao.append(grid[i][j])
                else :
                    if grid[i][j] != 0:
                            return False
                    rest.append(grid[i][j])
        
        
        return True
        
# @lc code=end

