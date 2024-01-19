'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 10:53:32
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 10:58:18
FilePath: \Leetcode_Solver\883.三维形体投影面积.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        # (1) xy sum  
        xy_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    xy_sum += 1
        
        # (2) xz sum 
        xz_sum = 0 
        for i in range(len(grid)):
            xz_sum += max(grid[i])
        
        
        # (3) xz sum 
        yz_sum = 0 
        for j in range(len(grid[0])):
            yz_sum += max([grid[i][j] for i in range(len(grid))])
        
        
        return  xy_sum + xz_sum + yz_sum
        
        
# @lc code=end

