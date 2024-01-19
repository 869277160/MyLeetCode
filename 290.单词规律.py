'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-24 09:38:27
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-24 09:48:46
FilePath: \Leetcode_Solver\290.单词规律.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern2word = {}
        word2pattern = {}
        words = s.split(" ")
        if len(pattern) != len(words):
            return False 
        
        for i in range(len(pattern)):
            if pattern[i] not in pattern2word.keys() and words[i] not in word2pattern.keys():
                pattern2word[pattern[i]] = words[i]
                word2pattern[words[i]] = pattern[i]
            else :
                if  pattern[i] not in pattern2word.keys() or words[i] not in word2pattern.keys(): 
                    return False
                else :
                    if pattern2word[pattern[i]] != words[i] or word2pattern[words[i]] != pattern[i] :
                        return False 
            
        # print(word2pattern)
        # print(pattern2word)
        
        return True 
        
# @lc code=end

