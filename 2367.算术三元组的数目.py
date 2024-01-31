'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:19:17
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 15:20:36
FilePath: \Leetcode_Solver\2367.算术三元组的数目.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2367 lang=python3
#
# [2367] 算术三元组的数目
#

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] - nums[i] == diff:
                    for k in range(j, len(nums)):
                        if nums[k] - nums[j] == diff:
                            res+=1
        return res 
        
        
# @lc code=end

