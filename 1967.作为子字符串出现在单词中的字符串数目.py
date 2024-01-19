'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:32:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:33:53
FilePath: \Leetcode_Solver\1967.作为子字符串出现在单词中的字符串数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1967 lang=python3
#
# [1967] 作为子字符串出现在单词中的字符串数目
#

# @lc code=start
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 for pattern in patterns if pattern in word])
# @lc code=end

