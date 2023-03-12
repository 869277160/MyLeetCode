'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 21:56:58
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 21:58:19
FilePath: \Leetcode_Solver\1480.一维数组的动态和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        return [sum(nums[:i+1]) for i in range(len(nums))]
        
        
# @lc code=end

