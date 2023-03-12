'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-07 17:08:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-07 17:10:12
FilePath: \Leetcode_Solver\1979.找出数组的最大公约数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1979 lang=python3
#
# [1979] 找出数组的最大公约数
#

# @lc code=start
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        max_num = max(nums)
        min_num = min(nums)
        
        if max_num == min_num:
            return max_num
        else:
            if max_num % min_num == 0:
                return min_num
            else:
                for i in range(min_num,0,-1):
                    if max_num %i == 0 and min_num %i == 0:
                        return i
# @lc code=end

