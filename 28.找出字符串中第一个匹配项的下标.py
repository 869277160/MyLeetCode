'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 10:46:46
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 10:47:15
FilePath: \Leetcode_Solver\28.找出字符串中第一个匹配项的下标.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        return haystack.find(needle)
        
# @lc code=end

