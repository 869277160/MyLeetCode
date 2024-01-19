'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 11:26:28
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 11:31:24
FilePath: \Leetcode_Solver\2529.正整数和负整数的最大计数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2529 lang=python3
#
# [2529] 正整数和负整数的最大计数
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        if nums == [] :
            return 0
        
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums) 

        less = great = 0
        for x in nums:
            if x < 0: less += 1
            elif x > 0: great += 1
        return max(less, great)
        
        # return max(bisect_left(nums, 0), len(nums) - bisect_right(nums, 0)
        
# @lc code=end

