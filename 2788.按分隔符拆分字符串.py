'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:49:44
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 15:51:00
FilePath: \Leetcode_Solver\2788.按分隔符拆分字符串.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2788 lang=python3
#
# [2788] 按分隔符拆分字符串
#

# @lc code=start
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        
        res = []
        for word in words:
            res += [c for c in word.split(separator) if c != ""]
        return res 
# @lc code=end

