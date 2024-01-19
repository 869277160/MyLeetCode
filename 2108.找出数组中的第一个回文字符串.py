'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 15:43:31
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 15:43:59
FilePath: \Leetcode_Solver\2108.找出数组中的第一个回文字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2108 lang=python3
#
# [2108] 找出数组中的第一个回文字符串
#

# @lc code=start
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            if word == word[::-1]:
                return word
        
        return ""
# @lc code=end

