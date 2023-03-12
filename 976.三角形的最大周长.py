'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:29:26
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 11:30:50
FilePath: \Leetcode_Solver\976.三角形的最大周长.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        if len(nums) < 3:
            return 0
        
        return nums[-1] + nums[-2] + nums[-3] if nums[-1] < nums[-2] + nums[-3] else self.largestPerimeter(nums[:-1])
        
        
# @lc code=end

