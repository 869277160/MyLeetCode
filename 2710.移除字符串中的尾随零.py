'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 21:21:30
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 21:22:23
FilePath: \Leetcode_Solver\2710.移除字符串中的尾随零.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2710 lang=python3
#
# [2710] 移除字符串中的尾随零
#

# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        for i in range(len(num)-1, -1, -1):
            if num[i] != "0":
                return num[:i+1]
        
        
        
# @lc code=end

