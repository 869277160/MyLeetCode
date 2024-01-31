'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:35:40
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 15:36:52
FilePath: \Leetcode_Solver\2733.既不是最小值也不是最大值.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2733 lang=python3
#
# [2733] 既不是最小值也不是最大值
#

# @lc code=start
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2 :
            return -1 
        
        for i in nums:
            if i != max(nums) and i!= min(nums):
                return i 
        
        return -1 
# @lc code=end

