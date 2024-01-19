'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-23 13:01:46
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-23 13:02:42
FilePath: \Leetcode_Solver\1455.检查单词是否为句中其他单词的前缀.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1455 lang=python3
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        words = sentence.split(' ')
        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i+1
        
        return -1
        
        
        
# @lc code=end

