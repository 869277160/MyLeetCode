'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 19:08:21
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 19:17:39
FilePath: \Leetcode_Solver\2873.有序三元组中的最大值-i.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2873 lang=python3
#
# [2873] 有序三元组中的最大值 I
#

# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        # left, right = 0, len(nums)
        # while left < right:
        #     for i in range(left + 1, right):
        #         res = max(res, (nums[left] - nums[i])*nums(right))
        left_max = nums[0]
            
        for i in range(1, len(nums)-1):
            res = max(res, (left_max - nums[i])*max(nums[i+1:]))
            left_max = max(left_max, nums[i])
        
        return res 
            
# @lc code=end

