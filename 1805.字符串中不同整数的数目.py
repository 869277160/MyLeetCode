'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 10:16:26
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 10:18:54
FilePath: \Leetcode_Solver\1805.字符串中不同整数的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        replacer = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for i in replacer:
            word = word.replace(i," ")
        
        return len(set([int(i) for i in word.split() if i != ""]))
        
# @lc code=end

