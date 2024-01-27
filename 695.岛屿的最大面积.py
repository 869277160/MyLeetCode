'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-21 14:46:56
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-21 15:13:03
FilePath: \Leetcode_Solver\695.岛屿的最大面积.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n_row = len(grid)
        n_col = len(grid[0])
        
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 1:
                    res = max(res, self.dfs_traverse(grid,i,j))
                
        return res
        
        
        
    
    def dfs_traverse(self, grid: List[List[int]], now_row: int, now_col: int) -> int:
        
        n_row = len(grid)
        n_col = len(grid[0])
        
        # 边界条件
        if now_row < 0 or now_col < 0 or now_row >= n_row or now_col >= n_col:
            # 超出索引边界
            return 0
        if grid[now_row][now_col] == 0:
            # 岛屿边界
            return 0 
        
        grid[now_row][now_col] = 0
    
        return self.dfs_traverse(grid, now_row + 1, now_col) + \
                self.dfs_traverse(grid, now_row, now_col + 1) + \
                self.dfs_traverse(grid, now_row - 1, now_col) + \
                self.dfs_traverse(grid, now_row, now_col - 1) + 1
    
    
# @lc code=end

