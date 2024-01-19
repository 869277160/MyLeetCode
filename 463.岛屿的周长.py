'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 18:48:36
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 11:08:41
FilePath: \Leetcode_Solver\463.岛屿的周长.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        if grid == [[1]]:
            return 4
        
        # 用加法思路 
        total = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] :
                    # （1） 计算最外侧上下边 
                    if i == 0 :
                        total +=1 
                    
                    if i == len(grid)- 1 :
                        total +=1 
                    
                    # (2)  计算内部上下边是否有效
                    if i+1 < len(grid) and grid[i+1][j] == 0:
                            total +=1
                    if i-1 > -1 and grid[i-1][j] == 0:
                            total +=1
                   

                    # （3） 计算最外侧左右边
                    if j == 0 :
                        total+=1 
                    if j == len(grid[0]) -1 :
                        total +=1
                    # (4)  计算内部左右边是否有效
                    if j + 1 <len(grid[0]) and grid[i][j+1] == 0:
                            total +=1
                    if j-1 > -1 and grid[i][j-1] == 0:
                            total +=1
                    # else:
                    #     if grid[i][j-1] == 0:
                    #         total +=1 
                    #     if grid[i][j+1] == 0:
                    #         total +=1
                print(total,"\n")
               
        return total
                
        
# @lc code=end

