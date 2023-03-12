'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 12:07:21
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 12:08:32
FilePath: \Leetcode_Solver\1464.数组中两元素的最大乘积.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (max(nums)-1)*(max(nums[:nums.index(max(nums))]+nums[nums.index(max(nums))+1:])-1)
        
# @lc code=end

