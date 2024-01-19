'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 10:01:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 10:11:12
FilePath: \Leetcode_Solver\2451.差值数组不同的字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2451 lang=python3
#
# [2451] 差值数组不同的字符串
#

# @lc code=start
class Solution:
    def oddString(self, words: List[str]) -> str:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        diff = []
        
        for i in range(len(words)):
            temp = []
            for j in range(len(words[i])-1):
                temp += [alphabet.index(words[i][j+1])-alphabet.index(words[i][j])]
            
            if temp not in diff and i > 1:
                return words[i]
            diff.append(temp)
            # print(diff)
        
        return words[0] if diff[0] != diff[1] and diff[1] == diff[2] else words[1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# @lc code=end

