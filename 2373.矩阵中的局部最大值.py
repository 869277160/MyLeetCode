'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 08:51:33
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 09:23:51
FilePath: \Leetcode_Solver\2373.矩阵中的局部最大值.py
Description:

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2373 lang=python3
#
# [2373] 矩阵中的局部最大值
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        
        for i in range(1,len(grid)-1):
            temp_res = []
            for j in range(1,len(grid[0])-1):
                temp_res.append(self.Getsmallgrid(grid,i,j))
            
            res.append(temp_res)

        return res 
        
    def Getsmallgrid(self,grid,i,j):
        
        res = [
        grid[i-1][j-1],
        grid[i-1][j],
        grid[i-1][j+1],
        grid[i][j-1],
        grid[i][j],
        grid[i][j+1],
        grid[i+1][j-1],
        grid[i+1][j],
        grid[i+1][j+1],]
        
        return max(res)
# @lc code=end

