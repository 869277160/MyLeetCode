#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        res = 0
        n_row, n_col = len(grid1), len(grid1[0])
        
        # 一共两种岛屿，一种是一定可以是子岛屿的，另一种则是一定不是的
        for i in range(n_row):
            for j in range(n_col):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs_traverse(grid2,i,j)
                    
        # print(grid2)
        
        for i in range(n_row):
            for j in range(n_col):
                if grid2[i][j] == 1:
                    res += 1 
                    self.dfs_traverse(grid2,i,j)
                    
        return res
        
    def dfs_traverse(self, grid: List[List[int]], now_row: int, now_col: int):
        
        n_row, n_col = len(grid), len(grid[0])
        
        # 边界判断
        if now_row < 0 or now_col < 0 or now_row >= n_row or now_col >= n_col:
            return 
        if grid[now_row][now_col] == 0:
            return 
        
        grid[now_row][now_col] = 0
        
        self.dfs_traverse(grid, now_row + 1, now_col)
        self.dfs_traverse(grid, now_row , now_col+ 1)
        self.dfs_traverse(grid, now_row - 1, now_col)
        self.dfs_traverse(grid, now_row , now_col- 1)
# @lc code=end

