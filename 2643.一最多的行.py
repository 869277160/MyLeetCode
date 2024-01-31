'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 20:51:12
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 20:52:14
FilePath: \Leetcode_Solver\2643.一最多的行.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2643 lang=python3
#
# [2643] 一最多的行
#

# @lc code=start
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        res = [row.count(1) for row in mat]
        
        return [res.index(max(res)), max(res)]
        
        
        
# @lc code=end

