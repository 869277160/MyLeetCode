'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 18:11:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 18:13:27
FilePath: \Leetcode_Solver\409.最长回文串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections
        all_counts = collections.Counter(s)
        odd = [i for i in all_counts.values() if i % 2 == 1]
        even = [i for i in all_counts.values() if i % 2 == 0]
        
        return sum(even) + sum(odd) - len(odd) + 1 if odd else sum(even)

# @lc code=end

