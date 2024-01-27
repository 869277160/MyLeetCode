'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-19 16:45:54
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-19 23:56:40
FilePath: \Leetcode_Solver\200.岛屿数量.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        # 遍历 grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 每发现一个岛屿，岛屿数量加一
                    res += 1
                    # 然后使用 DFS 遍历附近的土地
                    self.dfs(grid, i, j)
        return res

    # 从 (i, j) 开始，将与之相邻的陆地都变成海水
    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            # 超出索引边界
            return
        if grid[i][j] == '0':
            # 已经是海水了
            return
        # 将 (i, j) 变成海水
        grid[i][j] = '0'
        # 淹没上下左右的陆地
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
    
    # def numIslands(self, grid: List[List[str]]) -> int:
        
    #     res = 0 
    #     row, col = len(grid), len(grid[0])
        
    #     for i in range(row):
    #         for j in range(col):
    #             if grid[i][j] == '1':
    #                 res += 1 
    #                 self.dfs_traverse(grid, i, j)
        
    #     return res
        
        
    # def dfs_traverse(self, grid: List[List[str]], current_row: int, current_col: int):
    #     # 查找相邻的土地块
        
    #     print(current_row, current_col)
    #     n_row = len(grid)
    #     n_col = len(grid[0])
        
    #     if current_row < 0 or current_col < 0 or current_row >= n_row or current_col >= n_col:
    #         return 
    #     if grid[current_row][current_col] == '0':
    #         return 
        
    #     grid[current_col][current_row] = '0'
    #     self.dfs_traverse(grid, current_row+1, current_col)
    #     self.dfs_traverse(grid, current_row, current_col+1)
    #     self.dfs_traverse(grid, current_row-1, current_col)
    #     self.dfs_traverse(grid, current_row, current_col-1)
        
        
        
# @lc code=end

