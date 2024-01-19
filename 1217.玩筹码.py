'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 23:18:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 23:21:50
FilePath: \Leetcode_Solver\1217.玩筹码.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        odd = [1 for i in position if i % 2 == 1]
        even = [1 for i in position if i % 2 ==0]
        
        return min(sum(odd),sum(even))
        
# @lc code=end

