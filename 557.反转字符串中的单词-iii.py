'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 20:49:36
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:50:08
FilePath: \Leetcode_Solver\557.反转字符串中的单词-iii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word[::-1] for word in s.split(' ')]
        return ' '.join(words)
    
    

# @lc code=end

