'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 09:53:43
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 09:55:40
FilePath: \Leetcode_Solver\1844.将所有数字用字符替换.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1844 lang=python3
#
# [1844] 将所有数字用字符替换
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        
        for i in range(1,len(s),2):
            s = s[:i] + alphabet[alphabet.index(s[i-1])+int(s[i])] + s[i+1:]
        
        return s

        
      
# @lc code=end

