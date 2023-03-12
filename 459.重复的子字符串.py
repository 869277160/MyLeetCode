'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 18:21:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 18:21:48
FilePath: \Leetcode_Solver\459.重复的子字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range (1,len(s)//2+1):
            if len(s)%i == 0:
                if s[:i] * (len(s)//i) == s:
                    return True
        
        return False
        
# @lc code=end

