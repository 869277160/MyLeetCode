'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-30 14:18:35
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-30 14:21:02
FilePath: \Leetcode_Solver\853.车队.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=853 lang=python3
#
# [853] 车队
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# @lc code=end

