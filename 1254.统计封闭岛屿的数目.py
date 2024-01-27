#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        res = 0 
        n_row, n_col = len(grid), len(grid[0])
        
        # 移除最外侧的岛屿
        for col in range(n_col):
            self.dfs_traverse(grid, 0, col)
            self.dfs_traverse(grid, n_row - 1, col)
        for row in range(n_row):
            self.dfs_traverse(grid, row, 0)
            self.dfs_traverse(grid, row, n_col - 1)

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 0:
                    res +=1 
                self.dfs_traverse(grid, i, j)
        return res 

    def dfs_traverse(self, grid: List[List[int]], now_row: int, now_col: int):
        
        n_row, n_col = len(grid), len(grid[0])
        
        # 边界判断
        if now_row < 0 or now_col < 0 or now_row >= n_row or now_col >= n_col:
            return 
        if grid[now_row][now_col] == 1:
            return 
        
        grid[now_row][now_col] = 1
        
        self.dfs_traverse(grid, now_row + 1, now_col)
        self.dfs_traverse(grid, now_row , now_col+ 1)
        self.dfs_traverse(grid, now_row - 1, now_col)
        self.dfs_traverse(grid, now_row , now_col- 1)
# @lc code=end



# @lc code=end

