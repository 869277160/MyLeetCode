'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 16:10:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 16:11:11
FilePath: \Leetcode_Solver\1502.判断能否形成等差数列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        
        return True
# @lc code=end

