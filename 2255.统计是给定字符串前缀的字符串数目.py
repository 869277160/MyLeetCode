'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-23 09:24:16
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-23 09:25:55
FilePath: \Leetcode_Solver\2255.统计是给定字符串前缀的字符串数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2255 lang=python3
#
# [2255] 统计是给定字符串前缀的字符串数目
#

# @lc code=start
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        import collections
        
        freq = collections.Counter(words)
        
        res = 0
        for key in freq.keys():
            if s.startswith(key):
                res += freq[key]
    
        return res

# @lc code=end

