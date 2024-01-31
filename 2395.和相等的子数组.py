'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 21:48:56
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 21:54:25
FilePath: \Leetcode_Solver\2395.和相等的子数组.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2395 lang=python3
#
# [2395] 和相等的子数组
#

# @lc code=start
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        totals = set()
        for i in range(len(nums)-1):
            total = nums[i] + nums[i + 1]
            if total in totals:
                return True
            totals.add(total)
        return False
# @lc code=end

