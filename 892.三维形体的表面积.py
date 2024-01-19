'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 10:59:30
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 16:05:19
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
        
        # # 整体思路为 加法思路
        # # 在计算内部暴露在外的面积时，需要减去内部的重叠面积
        # # (1) xy sum  
        # xy_sum = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] != 0:
        #             xy_sum += 1
        
        # # (2) xz sum 
        # xz_sum = 0 
        # for i in range(len(grid)):
        #     xz_sum += max(grid[i])
        
        
        # # (3) yz sum 
        # yz_sum = 0 
        # for j in range(len(grid[0])):
        #     yz_sum += max([grid[i][j] for i in range(len(grid))])
        
        
        # # (4) inner sum
        # inner_sum = 0 
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         # not in the edge of the cube 
        #         if i != 0 and j != 0 and i != len(grid)-1 and j != len(grid[i])-1:
        #             if grid[i][j] <= grid[i-1][j] and grid[i][j] <= grid[i][j-1] and grid[i][j] <= grid[i+1][j] and grid[i][j] <= grid[i][j+1]:
                        
        #                 inner_sum += min(grid[i-1][j],grid[i+1][j]) - grid[i][j]
        #                 inner_sum += min(grid[i][j-1],grid[i][j+1]) - grid[i][j]
        #         # in the edge 
        #         elif ( i == 0 or i == len(grid) -1) and ( j != len(grid[i])-1 and j != 0) :
        #             if  grid[i][j] <= grid[i][j-1] and grid[i][j] <= grid[i][j+1]:
                        
        #                 # inner_sum += max(grid[i-1][j],grid[i+1][j]) - grid[i][j]
        #                 inner_sum += min(grid[i][j-1],grid[i][j+1]) - grid[i][j]
        #         # in other edge 
        #         elif (j == 0 or j == len(grid[i])-1) and ( i != 0 and i != len(grid)-1) :
        #             if grid[i][j] <= grid[i-1][j]  and grid[i][j] <= grid[i+1][j]:
                        
        #                 inner_sum += min(grid[i-1][j],grid[i+1][j]) - grid[i][j]
        #                 # inner_sum += max(grid[i][j-1],grid[i][j+1]) - grid[i][j]
        #         else :
        #             pass
                
                
        # return  (xy_sum + xz_sum + yz_sum + inner_sum) *2 
        
        import math as Math
        # 整体思路为减法思路
        N = len(grid)
        cubes = 0 # 记录立方体的数量
        faces = 0 # 记录立方体接触面的数量
        
        for i in range(N):
            for j in range(N):
                cubes += grid[i][j];
                if (grid[i][j] > 0):
                    # 叠起来的 v 个立方体有 v-1 个接触面
                    faces += grid[i][j] - 1;
                
                if (i > 0) :
                    # // 当前柱子与上边柱子的接触面数量
                    faces += min(grid[i-1][j], grid[i][j]);
            
                if (j > 0) :
                    # // 当前柱子与左边柱子的接触面数量
                    faces += min(grid[i][j-1], grid[i][j]);
        
        return 6 * cubes - 2 * faces;
# @lc code=end

