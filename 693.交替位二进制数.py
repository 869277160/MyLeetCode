'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 11:05:45
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 11:18:01
FilePath: \Leetcode_Solver\693.交替位二进制数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return a & (a + 1) == 0
        
        
        
# @lc code=end

