'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-14 16:54:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-14 17:06:11
FilePath: \Leetcode_Solver\1551.使数组中所有元素相等的最小操作数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1551 lang=python3
#
# [1551] 使数组中所有元素相等的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        
        if n % 2 == 0:
            return sum([i-1 for i in range(2, n+1, 2)])
        if n % 2 == 1:
            return sum([i-1 for i in range(1, n+1, 2)])
        
        
        
        
        
        
        
        
        
        
        
# @lc code=end

