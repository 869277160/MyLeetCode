'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 19:32:10
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 19:32:57
FilePath: \Leetcode_Solver\1991.找到数组的中间位置.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1991 lang=python3
#
# [1991] 找到数组的中间位置
#

# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1        
# @lc code=end

