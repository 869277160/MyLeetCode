'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 10:18:56
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 10:21:12
FilePath: \Leetcode_Solver\268.丢失的数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0 ^ len(nums)
        n = len(nums)
        
        for i in range(n):
            res = res^(i^nums[i])
            
        return res 
        
        
# @lc code=end

