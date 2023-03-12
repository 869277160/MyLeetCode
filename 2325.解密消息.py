'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 14:34:29
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 14:44:23
FilePath: \Leetcode_Solver\2325.解密消息.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2325 lang=python3
#
# [2325] 解密消息
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        org = "abcdefghijklmnopqrstuvwxyz"
        
        ordered = ""
        for i in key:
            if i not in ordered and i in org and i != " ":
                ordered += i
        
        res = ""
        for i in message:
            if i == " ":
                res += " "
            else:
                res += org[ordered.index(i)]

            
        return res 

# @lc code=end

