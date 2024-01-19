'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 09:55:33
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 09:57:35
FilePath: \Leetcode_Solver\1768.交替合并字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        if len(word1) > len(word2):
            for i in range(len(word2)):
                res += word1[i] + word2[i]
            res += word1[len(word2):]
        
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                    res += word1[i] + word2[i]
            res += word2[len(word1):]
        else :
            for i in range(len(word1)):
                res += word1[i] + word2[i]
        
        return res
        
        
        
# @lc code=end

