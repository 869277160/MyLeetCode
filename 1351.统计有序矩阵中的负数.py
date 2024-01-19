'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:45:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:46:24
FilePath: \Leetcode_Solver\1351.统计有序矩阵中的负数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] >= 0:
            return 0

        count = 0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    count += 1
        
        return count 
        
        
# @lc code=end

