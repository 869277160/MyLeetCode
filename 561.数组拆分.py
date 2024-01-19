'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 20:39:32
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:40:23
FilePath: \Leetcode_Solver\561.数组拆分.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        return sum(nums[::2])
        
        
        
# @lc code=end

