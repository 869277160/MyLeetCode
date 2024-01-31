'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 20:20:48
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 20:37:16
FilePath: \Leetcode_Solver\2716.最小化字符串长度.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2716 lang=python3
#
# [2716] 最小化字符串长度
#

# @lc code=start
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        from collections import Counter 
        return len(Counter(s).keys())
        
# @lc code=end

