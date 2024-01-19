'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 16:03:43
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 16:07:52
FilePath: \Leetcode_Solver\1848.到目标元素的最小距离.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1848 lang=python3
#
# [1848] 到目标元素的最小距离
#

# @lc code=start
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        for i in range(0,len(nums)):
            if start + i < len(nums) and nums[start+i ] == target:
                return i
            if start - i >= 0 and nums[start-i] == target:
                return i
            
# @lc code=end

