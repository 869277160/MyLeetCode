'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 14:24:43
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 14:26:13
FilePath: \Leetcode_Solver\2864.最大二进制奇数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2864 lang=python3
#
# [2864] 最大二进制奇数
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        from collections import Counter
        c_count = Counter(s)
        
        return "1"*(c_count["1"]-1) + "0"*c_count["0"] + "1"
# @lc code=end

