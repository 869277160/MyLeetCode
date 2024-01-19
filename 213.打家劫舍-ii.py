'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:52:55
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-27 15:06:04
FilePath: \Leetcode_Solver\213.打家劫舍-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        memo_1 = [-1 for _ in nums]
        memo_2 = [-1 for _ in nums]
        
        def dp(nums,start,end,memo):
            if start > end:
                return 0
            if memo[start] != -1:
                return memo[start]
            res = max(dp(nums,start+1,end,memo),dp(nums,start+2,end,memo)+nums[start])
            memo[start] = res
            return res
        
        res = max(dp(nums,0,len(nums)-2,memo_1),dp(nums,1,len(nums)-1,memo_2))
        return res
        
        
# @lc code=end

