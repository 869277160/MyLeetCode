'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-19 21:38:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-19 21:41:43
FilePath: \Leetcode_Solver\1403.非递增顺序的最小子序列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        nums.sort(reverse=True)
    
        res = []
        
        for i in range(len(nums)):
            res.append(nums[i])
            if sum(res) > sum(nums[i+1:]):
                return res
        
        return res 
        
        
# @lc code=end

