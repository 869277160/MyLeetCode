'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2023-08-21 17:30:26
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-25 18:40:24
FilePath: \Leetcode_Solver\47.全排列-ii.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
from collections import Counter 
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
       
        if len(nums) == 0: return []
        elif len(nums) == 1: return [nums]
        elif len(nums) == 2: 
            if nums[0] == nums[1]:
                return [nums]
            else :
                return [nums,nums[::-1]]
        else :
            self.res = []
            counted_nums = Counter(nums)
            for num in counted_nums:
                counted_nums = Counter(nums)
                counted_nums[num] -= 1 
                self.backtrack(counted_nums,[num],len(nums))
            return self.res
        
   
    def backtrack(self, counted_nums, track,total_len):
        # print(counted_nums, track)
        if len(track) == total_len:
            self.res.append(list(track))
            return 
        
        for i in counted_nums:
            if counted_nums[i] > 0:
                counted_nums[i] -= 1
                self.backtrack(counted_nums, track+[i], total_len)
                counted_nums[i] += 1
# @lc code=end

