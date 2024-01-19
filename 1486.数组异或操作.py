'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 14:35:13
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 14:36:15
FilePath: \Leetcode_Solver\1486.数组异或操作.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        
        for i in range(1,n):
            res ^= start + 2 * i
        
        return res
        
        
        
        
# @lc code=end

