'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 10:40:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 10:42:41
FilePath: \Leetcode_Solver\2309.兼具大小写的最好英文字母.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2309 lang=python3
#
# [2309] 兼具大小写的最好英文字母
#

# @lc code=start
class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabet_1 = "abcdefghijklmnopqrstuvwxyz"
        alphabet_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for i in range(25,-1,-1):
            if alphabet_1[i] in s and alphabet_2[i] in s:
                return alphabet_2[i]
        
        return ""
        
        
        
        
# @lc code=end

