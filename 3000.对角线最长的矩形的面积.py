'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 16:34:38
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 16:36:15
FilePath: \Leetcode_Solver\3000.对角线最长的矩形的面积.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=3000 lang=python3
#
# [3000] 对角线最长的矩形的面积
#

# @lc code=start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        return max([a * a + b * b, a * b] for a, b in dimensions)[1]
        
        
# @lc code=end

