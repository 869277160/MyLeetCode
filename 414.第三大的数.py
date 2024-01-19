'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 18:09:25
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 18:10:22
FilePath: \Leetcode_Solver\414.第三大的数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]
        
        
        
# @lc code=end

