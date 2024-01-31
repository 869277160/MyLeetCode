'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 21:02:24
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 21:04:47
FilePath: \Leetcode_Solver\2605.从两个数字数组里生成最小数字.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2605 lang=python3
#
# [2605] 从两个数字数组里生成最小数字
#

# @lc code=start
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(10):
            if i in nums2 and i in (nums1):
                return i
        
        return min(min(nums1),min(nums2))*10 + max(min(nums1),min(nums2))
        
        
        
# @lc code=end

