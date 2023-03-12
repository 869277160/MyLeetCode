'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 12:34:45
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 12:39:40
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1446.连续字符.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        max_res = -1 
        
        i = 0 
        while i < len(s)-1:
            if s[i] != s[i+1]:
                i+=1
            else:
                j = i 
                while j < len(s) and s[j] == s[i]:
                    j+=1
                max_res = max(max_res, j-i)
                i = j
        
        return max_res if max_res != -1 else 1
                
# @lc code=end

