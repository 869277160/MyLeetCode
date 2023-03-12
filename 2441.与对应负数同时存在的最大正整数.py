'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 11:52:09
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 11:54:07
FilePath: \Leetcode_Solverd:\Leetcode_Solver\2441.与对应负数同时存在的最大正整数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2441 lang=python3
#
# [2441] 与对应负数同时存在的最大正整数
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return -1
        if -1*max(nums) in nums:
            return max(nums)
        else :
            current_max = -1
            for i in range(len(nums)):
                if nums[i] > 0 and nums[i] > current_max and -1*nums[i] in nums:
                    current_max = nums[i]
                
            return current_max
        
        
# @lc code=end

