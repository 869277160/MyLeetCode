'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 13:36:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 13:39:39
FilePath: \Leetcode_Solver\1408.数组中的字符串匹配.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words = sorted(words, key=lambda x:len(x))
        
        res = []
        for i in range(len(words)):
            word = words[i] 
            for j in range(len(words)-1,i,-1):
                if word in words[j]:
                    res.append(word)
                    break
        
        return res 
        
        
        
        
# @lc code=end

