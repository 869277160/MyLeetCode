'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 10:00:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 14:16:32
FilePath: \Leetcode_Solver\994.腐烂的橘子.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) :
        
        # # 检测是否可以完全腐烂
        # if self.checkunrot(grid) == True:
        #     return -1
        # else:
        count = 0 
        last = grid 
    
        # 没有完全腐坏时遍历
        while(self.checkallrot(last) == False):
            # 腐坏
            currrent = self.rot(last)
            
            # 存在无法腐坏的橘子, 即特定时刻状态不变且存在无法腐坏的橘子
            if currrent == last and self.checkallrot(last) == False:
                return -1 

            
            # 状态和计数器转化
            last = currrent 
            count += 1

            # return last 
        
        # 返回
        return count 
                
    # 0 表示没有腐烂完成的橘子
    # 1 表示腐烂完成
    def checkallrot(self,grid):
        for i in grid:
            for j in i:
                if j == 1:
                    return False
        return True

    # 遍历并进行腐坏
    def rot(self,grid):
        
        new_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    new_grid[i][j] = 1
                    if i > 0 and grid[i-1][j] == 2:
                        new_grid[i][j] = 2
                    elif i < len(grid)-1 and grid[i+1][j] == 2:
                        new_grid[i][j] = 2
                    elif j > 0 and grid[i][j-1] == 2:
                        new_grid[i][j] = 2
                    elif j < len(grid[i])-1 and grid[i][j+1] == 2:
                        new_grid[i][j] = 2
                elif grid[i][j] == 2 :
                    new_grid[i][j] = 2
                elif grid[i][j] == 0 :
                    new_grid[i][j] = 0
                else:
                    pass 
            
        return new_grid
    
    # # 如果有橘子被0包围，返回True
    # def checkunrot(self,grid):
    #     return False
    #     for i in range(len(grid)):
    #         if 
            
            
    #         for j in range(len(grid[i])):
    #             if grid[i][j] == 1:
    #                 if
    #                 if i > 0 and grid[i-1][j] == 0:
    #                     new_grid[i][j] = 2
    #                 elif i < len(grid)-1 and grid[i+1][j] == 2:
    #                     new_grid[i][j] = 2
    #                 elif j > 0 and grid[i][j-1] == 2:
    #                     new_grid[i][j] = 2
    #                 elif j < len(grid[i])-1 and grid[i][j+1] == 2:
    #                     new_grid[i][j] = 2

# @lc code=end

