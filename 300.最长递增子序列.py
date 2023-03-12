'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-24 11:28:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-24 11:29:34
FilePath: \Leetcode_Solver\300.最长递增子序列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp_list = [1]* (len(nums))
        
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_list[i] = max(dp_list[i], dp_list[j]+1)
                    
        return max(dp_list)
        
        
        
        
# @lc code=end

