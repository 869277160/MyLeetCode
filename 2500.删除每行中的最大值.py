'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:56:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 00:09:37
FilePath: \Leetcode_Solver\2500.删除每行中的最大值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2500 lang=python3
#
# [2500] 删除每行中的最大值
#

# @lc code=start
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        
        total = 0
        while(len(grid[0])>0):
            current_remove_num = []
            max_value = max(grid[0])
            for i in range(len(grid)):
                max_value = max(grid[i])
                current_remove_num.append(max_value)
                grid[i].remove(max_value)
            total += max(current_remove_num)
        
        return total
        
# @lc code=end

