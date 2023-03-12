'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-04 23:22:38
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-04 23:23:56
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1051.高度检查器.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        heights_sorted = sorted(heights)
        
        res = 0
        for i in range(len(heights_sorted)):
            if heights[i] != heights_sorted[i]:
                res +=1 

        return res 
        
        
# @lc code=end

