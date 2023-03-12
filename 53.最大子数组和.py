'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 13:38:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 14:10:58
FilePath: \Leetcode_Solver\53.最大子数组和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 0 :
            return 0 
        if len(nums) == 1:
            return nums[0]

        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range (len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        
        
        return max(dp)
                                                                                                                                                                                                                                          
        
# @lc code=end

