'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 11:38:43
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 11:41:55
FilePath: \Leetcode_Solver\1021.删除最外层的括号.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        all_depth = 0 
        
        depth_list = []
        for i in range(len(s)):
            if s[i] == "(":
                all_depth +=1 
                depth_list.append(all_depth)
            elif s[i] == ")":
                depth_list.append(all_depth)
                all_depth -=1
            
        
        res = ""
        for i in range(len(s)):
            if depth_list[i] != 1 :
                res += s[i]
                
        return res 
# @lc code=end

