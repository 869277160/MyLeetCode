'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-28 09:29:26
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 13:45:52
FilePath: \Leetcode_Solver\1413.逐步求和得到正数的最小值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        res = [nums[0]]
        for i in range(1,len(nums)):
            res.append(nums[i]+res[-1])
        
        return 1 if min(res) >= 1 else 1-min(res)
        
        
# @lc code=end

