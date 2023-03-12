'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-03-07 10:12:53
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-03-07 10:21:48
FilePath: \Leetcode_Solver\1365.有多少小于当前数字的数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)

        res = []
        current_max = max(nums)
        current_min = min(nums)
        
        for i in range(len(nums)):
            # if nums[i] == current_min:
            #     res.append(0)
            # elif nums[i] == current_max:
            #     res.append(len(nums)-1)
            # else :
            res.append(sorted_nums.index(nums[i]))
        return res 
        
# @lc code=end

