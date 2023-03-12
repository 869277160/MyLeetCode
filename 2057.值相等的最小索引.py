'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-06 09:47:50
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-06 09:48:58
FilePath: \Leetcode_Solverd:\Leetcode_Solver\2057.值相等的最小索引.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2057 lang=python3
#
# [2057] 值相等的最小索引
#

# @lc code=start
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        
        return -1
        
# @lc code=end

