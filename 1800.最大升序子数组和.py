'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:03:34
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:09:18
FilePath: \Leetcode_Solver\1800.最大升序子数组和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1800 lang=python3
#
# [1800] 最大升序子数组和
#

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        res = []
        current_sum = 0 
        for i in range(len(nums)):
            if i == 0:
                res.append(nums[0])
            else:
                if nums[i] > nums[i-1]:
                    res.append(res[-1]+nums[i])
                else:
                    res.append(nums[i])
        
        return max(res)
        
# @lc code=end

