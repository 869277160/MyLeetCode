'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 10:59:30
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 11:25:33
FilePath: \Leetcode_Solver\892.三维形体的表面积.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
                
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
        
        
        # (4) inner sum
        inner_sum = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # not in the edge of the cube 
                if i != 0 and j != 0 and i != len(grid)-1 and j != len(grid[i])-1:
                    if grid[i][j] <= grid[i-1][j] and grid[i][j] <= grid[i][j-1] and grid[i][j] <= grid[i+1][j] and grid[i][j] <= grid[i][j+1]:
                        
                        inner_sum += min(grid[i-1][j],grid[i+1][j]) - grid[i][j]
                        inner_sum += min(grid[i][j-1],grid[i][j+1]) - grid[i][j]
                # in the edge 
                elif ( i == 0 or i == len(grid) -1) and ( j != len(grid[i])-1 and j != 0) :
                    if  grid[i][j] <= grid[i][j-1] and grid[i][j] <= grid[i][j+1]:
                        
                        # inner_sum += max(grid[i-1][j],grid[i+1][j]) - grid[i][j]
                        inner_sum += min(grid[i][j-1],grid[i][j+1]) - grid[i][j]
                # in other edge 
                elif (j == 0 or j == len(grid[i])-1) and ( i != 0 and i != len(grid)-1) :
                    if grid[i][j] <= grid[i-1][j]  and grid[i][j] <= grid[i+1][j]:
                        
                        inner_sum += min(grid[i-1][j],grid[i+1][j]) - grid[i][j]
                        # inner_sum += max(grid[i][j-1],grid[i][j+1]) - grid[i][j]
                else :
                    pass
                
                
        return  (xy_sum + xz_sum + yz_sum + inner_sum) *2 
        
        
# @lc code=end

