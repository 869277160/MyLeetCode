'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 09:50:05
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 09:50:31
FilePath: \Leetcode_Solver\1678.设计-goal-解析器.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1678 lang=python3
#
# [1678] 设计 Goal 解析器
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()","o").replace("(al)","al")
    
    
# @lc code=end

