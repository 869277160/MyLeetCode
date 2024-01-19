'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 11:20:21
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 11:25:08
FilePath: \Leetcode_Solver\2562.找出数组的串联值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2562 lang=python3
#
# [2562] 找出数组的串联值
#

# @lc code=start
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        total = 0 
        
        for i in range(len(nums)//2):
                total += nums[len(nums)-1-i]
                total += nums[i]*(10**len(str(nums[len(nums)-1-i])))
        
        if len(nums) % 2 != 0 :
            total += nums[len(nums)//2]
        
        return total
        
        
        
# @lc code=end

