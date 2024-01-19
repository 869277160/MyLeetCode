'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 11:47:07
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 12:05:56
FilePath: \Leetcode_Solver\1260.二维网格迁移.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        if k%(m*n) == 0 :
            return grid
        
        # create the list 
        total = []
        for i in range(len(grid)):
            total += grid[i]
        total += total 
        
        start = m*n - (k%(m*n))
        print(start)
        listed_grid = total[start:start- m*n]
        print(listed_grid)
        
        grid = self.shift(listed_grid, m, n )
            
        return grid
    
    def shift(self,listed_grid: List[int], m:int, n:int) -> List[List[int]]:
        
        # create the new grid based on the list 
        grids = []
        for i in range(m):
            grids.append(listed_grid[i*n:(i+1)*n])

        return grids
        
# @lc code=end

