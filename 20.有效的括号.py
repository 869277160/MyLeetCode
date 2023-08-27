'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-13 10:38:21
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-13 10:40:59
FilePath: \Leetcode_Solver\20.有效的括号.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        for c in s :
            if c == '(' or c == '{' or c == '[':
                left.append(c)
            else:
                if left and self.check(left[-1], c):
                    left.pop()
                else :
                    return False
        
        return not left
    
    def check(self, c1, c2):
        if c1 == '(' and c2 == ')':
            return True
        if c1 == '{' and c2 == '}':
            return True
        if c1 == '[' and c2 == ']':
            return True
        return False
# @lc code=end

