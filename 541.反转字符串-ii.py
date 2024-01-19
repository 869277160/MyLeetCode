'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-08 09:17:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:57:25
FilePath: \Leetcode_Solver\541.反转字符串-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        # for i in range(0,len(s)-2*k,2*k):
        
        if k == 1 :
            return s 
        if k == len(s):
            return s[::-1]
        
        total_len = len(s)
        
        if total_len % 2*k == 0:
            for i in range(0,total_len,2*k):
                res += s[i:i+k][::-1]
                res += s[i+k:i+2*k]
        else:
            
            rest = total_len % (2*k)
            
            for i in range(0,total_len-rest,2*k):
                res += s[i:i+k][::-1]
                res += s[i+k:i+2*k]
            
            if rest < k:
                res += s[-rest:][::-1]
            else :
                same = rest - k 
                res += s[-rest:-same][::-1]
                res += s[-same:]
                
        
        return res 
        
# @lc code=end

