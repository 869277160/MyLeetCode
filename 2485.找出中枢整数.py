'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 14:24:33
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 14:27:22
FilePath: \Leetcode_Solver\2485.找出中枢整数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2485 lang=python3
#
# [2485] 找出中枢整数
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [i for i in range(n+1)]
        
        for i in range(n//2,n+1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            

        return -1

# @lc code=end

