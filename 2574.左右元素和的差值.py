'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 11:14:50
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 11:18:27
FilePath: \Leetcode_Solver\2574.左右元素和的差值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2574 lang=python3
#
# [2574] 左右元素和的差值
#

# @lc code=start
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        leftsum = [0 for i in range(len(nums))]
        rightsum = [0 for i in range(len(nums))] 
        res = [0 for i in range(len(nums))] 
        
        
        for i in range(len(nums)):
            if i == 0:
                leftsum[i] = 0
                rightsum[i] = total - nums[i]
            else:
                leftsum[i] = leftsum[i-1] + nums[i-1]
                rightsum[i] = total - leftsum[i] - nums[i]

            res[i] = abs(leftsum[i] - rightsum[i])
            
        return res
        
        
# @lc code=end

