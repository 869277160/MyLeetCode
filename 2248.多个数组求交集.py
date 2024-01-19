'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:58:26
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:59:03
FilePath: \Leetcode_Solver\2248.多个数组求交集.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2248 lang=python3
#
# [2248] 多个数组求交集
#

# @lc code=start
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res = nums[0]
            else:
                res = list(set(res) & set(nums[i]))
        
        return sorted(res)
        
        
# @lc code=end

