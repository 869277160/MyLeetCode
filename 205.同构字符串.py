'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-15 09:37:57
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-15 09:48:43
FilePath: \Leetcode_Solver\205.同构字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        maper = [-1]*256
        
        for i in range(len(s)):
            if maper[ord(s[i])] == -1 and ord(t[i]) not in maper:
                maper[ord(s[i])] = ord(t[i])
                # print(ord(s[i]),ord(t[i]))
            else :
                if maper[ord(s[i])] != ord(t[i]):
                    return False
         
        return True
        
        
        
        
# @lc code=end

