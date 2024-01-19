'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 11:22:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 11:24:17
FilePath: \Leetcode_Solver\796.旋转字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if s == goal:
            return True
        
        for i in range(1,len(s)):
            if s[i:] + s[:i] == goal:
                return True
        
        return False 
        
# @lc code=end

