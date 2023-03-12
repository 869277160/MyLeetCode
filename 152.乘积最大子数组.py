'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-25 14:15:19
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 14:45:47
FilePath: \Leetcode_Solver\152.乘积最大子数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else :
            dp1 = [0 for i in nums]
            dp2 = [0 for i in nums]
            
            
            dp1[0], dp2[0] = nums[0], nums[0]
            
            for i in range(len(nums)):
                dp1[i] = min(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i]);
                dp2[i] = max(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i]);
            
            return max(dp2)
        
        
        
# @lc code=end

