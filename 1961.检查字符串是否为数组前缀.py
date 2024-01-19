'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:11:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:14:19
FilePath: \Leetcode_Solver\1961.检查字符串是否为数组前缀.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1961 lang=python3
#
# [1961] 检查字符串是否为数组前缀
#

# @lc code=start
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        current = ""
        for word in words:
            current += word
            if len(current) == len(s) :
                if current == s:
                    return True
                else :
                    return False 
            elif len(current) > len(s):
                return False
            else:
                if current != s[:len(current)]:
                    return False
        
        
        return False
                    
            
        
# @lc code=end

