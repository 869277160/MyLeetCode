'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:28:10
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 15:28:53
FilePath: \Leetcode_Solver\2656.k-个元素的最大和.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2656 lang=python3
#
# [2656] K 个元素的最大和
#

# @lc code=start
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        return max(nums) * k + ((k - 1)*k//2)
        
        
# @lc code=end

