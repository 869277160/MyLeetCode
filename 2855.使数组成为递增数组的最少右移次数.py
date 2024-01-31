'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 18:41:31
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 18:51:43
FilePath: \Leetcode_Solver\2855.使数组成为递增数组的最少右移次数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2855 lang=python3
#
# [2855] 使数组成为递增数组的最少右移次数
#

# @lc code=start
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        nums = nums+[nums[0]]
        chance = 1
        step = len(nums) - 1
        for i in range(1,len(nums)):
            if chance < 0:
                return -1
            if nums[i] < nums[i-1]:
                chance = chance - 1
                step = i

        return -1 if chance < 0 else len(nums) - 1 - step
        
# @lc code=end

