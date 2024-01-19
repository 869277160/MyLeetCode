'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-24 10:33:24
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-24 10:35:24
FilePath: \Leetcode_Solver\724.寻找数组的中心下标.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        current_sum = 0
        for i in range(len(nums)):
            right_sum = total - current_sum - nums[i]
            
            if current_sum == right_sum:
                return i
            
            current_sum += nums[i]
        
        return -1 
        
        
        
# @lc code=end

