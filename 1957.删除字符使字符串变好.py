'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:15:37
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:31:44
FilePath: \Leetcode_Solver\1957.删除字符使字符串变好.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1957 lang=python3
#
# [1957] 删除字符使字符串变好
#

# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        
        if len(s) < 3:
            return s
        if len(s) == 3 :
            if s[0] == s[1] == s[2]:
                return s[:2]
            else :
                return s
        
        current_pos = 0
        current = ""
        while(current_pos < len(s)-2):
            if s[current_pos] == s[current_pos+1] == s[current_pos+2]:
                current += s[current_pos]
                current += s[current_pos]
                
                new_pos = current_pos+2
                for i in range(current_pos+2,len(s)):
                    if s[i] != s[current_pos] or i == len(s)-1:
                        new_pos = i
                        break
                current_pos = new_pos 
            elif s[current_pos] == s[current_pos+1] and s[current_pos+2] != s[current_pos]:
                current += s[current_pos:current_pos+2]
                current_pos += 2
            elif s[current_pos+1] != s[current_pos]:
                current += s[current_pos]
                current_pos += 1 
        
        # print(curres[current_pos]nt_pos,current)
        if (s[-1] == s[-2] and s[-1] != s[-3]) or (s[-1] != s[-2]):
            return current+s[current_pos:]
        else:
            return current
# @lc code=end

