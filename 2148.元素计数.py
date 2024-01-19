'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:47:51
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:49:57
FilePath: \Leetcode_Solver\2148.元素计数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2148 lang=python3
#
# [2148] 元素计数
#

# @lc code=start
class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num, max_nums = min(nums), max(nums)
        
        res = 0
        for nums in nums:
            if nums < max_nums and nums > min_num:
                res += 1
        return res 
        
# @lc code=end

