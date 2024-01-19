'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 14:09:27
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 14:16:15
FilePath: \Leetcode_Solver\1071.字符串的最大公因子.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        min_len = min(len(str1),len(str2))
        res = ""
        for i in range(min_len, 0, -1):
            if len(str1) % (i) == 0 and len(str2) % (i) == 0:
                if str1[:i] * (len(str1)//i) == str1 and str1[:i] * (len(str2)//i) == str2:
                    return str1[:i]
        
        return res 
        
        
        
        
# @lc code=end

