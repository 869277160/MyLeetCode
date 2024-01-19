'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:55:40
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:56:11
FilePath: \Leetcode_Solver\2215.找出两数组的不同.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2215 lang=python3
#
# [2215] 找出两数组的不同
#

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        return [list(set(nums1) - set(nums2)),list(set(nums2) - set(nums1))]
        
# @lc code=end

