'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 19:18:24
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 19:22:39
FilePath: \Leetcode_Solver\2839.判断通过操作能否让字符串相等-i.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2839 lang=python3
#
# [2839] 判断通过操作能否让字符串相等 I
#

# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # from collections import Counter
        # if Counter(s1) != Counter(s2):
        #     return False
        # else:
        temp = [s1,
                s1[0]+s1[3]+s1[2]+s1[1],
                s1[2]+s1[1]+s1[0]+s1[3],
                s1[2]+s1[3]+s1[0]+s1[1],
                ]
        
        
        return True if s2 in temp else False
        
        
# @lc code=end

