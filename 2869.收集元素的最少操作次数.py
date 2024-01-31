'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 14:28:04
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 14:42:08
FilePath: \Leetcode_Solver\2869.收集元素的最少操作次数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2869 lang=python3
#
# [2869] 收集元素的最少操作次数
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = [0 for i in range(k+1)]
        step = 1
        while(nums != []):
            if nums[-1] < k+1 and nums[-1]>= 1:
                res[nums[-1]] = nums[-1]

            # print(nums, res, step)
            if sum(res) == ((k)*(k+1))//2:
                return step
           
            step += 1
            nums = nums[:-1]
            
        return step - 1 
            
# @lc code=end

