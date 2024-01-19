'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 23:06:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 23:07:11
FilePath: \Leetcode_Solver\977.有序数组的平方.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        return sorted([i**2 for i in nums])
# @lc code=end

