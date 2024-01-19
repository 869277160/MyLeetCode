'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 13:22:46
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 13:25:32
FilePath: \Leetcode_Solver\1880.检查某单词是否等于两单词之和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1880 lang=python3
#
# [1880] 检查某单词是否等于两单词之和
#

# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        if self.tonum(firstWord) + self.tonum(secondWord) == self.tonum(targetWord):
            return True
        else:
            return False
    
    def tonum(self,input_str):
        total_len = len(input_str)
        total_sum = 0
        for i in range(total_len):
            total_sum += (ord(input_str[i]) - ord('a')) * (10**(total_len - i - 1))
            
        return total_sum
        
        
        
        
# @lc code=end

