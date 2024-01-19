'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 19:26:36
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 19:27:43
FilePath: \Leetcode_Solver\2475.数组中不等三元组的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2475 lang=python3
#
# [2475] 数组中不等三元组的数目
#

# @lc code=start
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        count = 0 
        total_len = len(nums)
        for i in range(total_len):
            for j in range(i+1,total_len):
                for k in range(j+1,total_len):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        count += 1
                        
        return count 
# @lc code=end

