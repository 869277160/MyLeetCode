'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 09:41:08
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 09:41:44
FilePath: \Leetcode_Solver\2000.反转单词前缀.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2000 lang=python3
#
# [2000] 反转单词前缀
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        return word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:] if ch in word else word
        
        
# @lc code=end

