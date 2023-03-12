'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:17:26
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:24:37
FilePath: \Leetcode_Solver\2124.检查是否所有-a-都在-b-之前.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2124 lang=python3
#
# [2124] 检查是否所有 A 都在 B 之前
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s: 
            return True
        if 'b' not in s: 
            return True
        if s == "ab":
            return True
        if s == "ba":
            return False 
        if s == "a" or s == "b":
            return True
        
        first_b = s.rfind('b')   
        if 'a' not in s[first_b:]:
            return True
        else :
            return False
        # return True
# @lc code=end

