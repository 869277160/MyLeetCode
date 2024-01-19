'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 15:52:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 15:57:09
FilePath: \Leetcode_Solver\2239.找到最接近-0-的数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2239 lang=python3
#
# [2239] 找到最接近 0 的数字
#

# @lc code=start
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        # min, max, sorted 都可以用lambda表达式
        return min(nums, key=lambda x: (abs(x), -x))
        
        # for i in range(0,abs(max(nums))+1):
        #     if i in nums: 
        #         return i
        #     if  -i in nums:
        #         return -i
        
        
        
# @lc code=end

