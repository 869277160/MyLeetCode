'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-27 14:29:37
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-27 14:34:07
FilePath: \Leetcode_Solver\198.打家劫舍.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for _ in nums]

        def dp(nums,start):
            if start >= len(nums):
                return 0
            if memo[start] != -1:
                return memo[start]
            res = max(dp(nums,start+1),dp(nums,start+2)+nums[start])
            memo[start] = res
            return res
        
        return dp(nums,0)
        
        
        
        
        
        
# @lc code=end

