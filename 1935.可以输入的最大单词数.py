'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 15:40:19
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 15:42:31
FilePath: \Leetcode_Solver\1935.可以输入的最大单词数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1935 lang=python3
#
# [1935] 可以输入的最大单词数
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        
        count = 0
        for word in words:
            if self.cantype(word,brokenLetters):
                count += 1
        
        return count 
    
    def cantype(self,word,brokenLetters):
        for i in range(len(brokenLetters)):
            if brokenLetters[i] in word:
                return False
        
        return True
        
        
        

# @lc code=end

