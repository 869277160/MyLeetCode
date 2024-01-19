'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:38:26
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:39:27
FilePath: \Leetcode_Solver\2351.第一个出现两次的字母.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2351 lang=python3
#
# [2351] 第一个出现两次的字母
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        for i in range(len(s)) :
            if s[i] in s[:i]:
                return s[i]
# @lc code=end

