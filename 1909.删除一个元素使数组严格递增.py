'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 10:03:09
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 10:07:29
FilePath: \Leetcode_Solver\1909.删除一个元素使数组严格递增.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1909 lang=python3
#
# [1909] 删除一个元素使数组严格递增
#

# @lc code=start
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        if self.check(nums):
            return True
        else:
            for i in range(len(nums)):
                if self.check(nums[:i]+nums[i+1:]):
                    return True
            
            return False 

    
        
    def check(self,numbers):
        
        for i in range(len(numbers)-1):
            if numbers[i] >= numbers[i+1]:
                return False
        return True

        
        
        
        
# @lc code=end

