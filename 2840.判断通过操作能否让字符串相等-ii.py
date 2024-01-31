'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 19:23:05
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 19:28:28
FilePath: \Leetcode_Solver\2840.判断通过操作能否让字符串相等-ii.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2840 lang=python3
#
# [2840] 判断通过操作能否让字符串相等 II
#

# @lc code=start
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s1_odds_count = {c:0 for c in alphabet}
        s1_even_count = {c:0 for c in alphabet}
        s2_odds_count = {c:0 for c in alphabet}
        s2_even_count = {c:0 for c in alphabet}
        
        for i in range(len(s1)):
            if i % 2 ==0:
                s1_odds_count[s1[i]] += 1
            else :
                s1_even_count[s1[i]] += 1
        
        for i in range(len(s2)):
            if i % 2 ==0:
                s2_odds_count[s2[i]] += 1
            else :
                s2_even_count[s2[i]] += 1
                
        return True if s1_odds_count == s2_odds_count and s1_even_count == s2_even_count else False 
        
# @lc code=end

