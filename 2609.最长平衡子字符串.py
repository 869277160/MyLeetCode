'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 21:05:34
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 21:12:13
FilePath: \Leetcode_Solver\2609.最长平衡子字符串.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2609 lang=python3
#
# [2609] 最长平衡子字符串
#

# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        max_res = 0
        for i in range(1,26):
            if 2*i <= len(s):
                if "0"*i+"1"*i in s:
                    max_res = i

        return max_res *2
# @lc code=end

