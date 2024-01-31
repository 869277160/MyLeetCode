'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 16:05:08
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 16:13:10
FilePath: \Leetcode_Solver\3014.输入单词需要的最少按键次数-i.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=3014 lang=python3
#
# [3014] 输入单词需要的最少按键次数 I
#

# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        
        if len(word) <= 8:
            return len(word)
        if len(word) <= 16:
            return 8 + 2*(len(word)-8)
        if len(word) <= 24:
            return 8 + 16 + 3*(len(word)-16)
        else:
            return 8 + 16 + 24 + 4*(len(word)-24)
        
        
# @lc code=end

