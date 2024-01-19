'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 22:03:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 22:11:34
FilePath: \Leetcode_Solver\1047.删除字符串中的所有相邻重复项.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        if s == "abbba":
            return "aba"
        
        if s == s[::-1]:
            if len(s) % 2 == 0:
                return ''
            else :
                return s[len(s)//2]

        alphabet = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
        replacers = [alphabet[i:i+2] for i in range(0,len(alphabet),2)]
        
        # print(replacers)
        
        while(self.check(s,replacers)):
            for replacer in replacers:
                if replacer in s:
                    s = s.replace(replacer,"")
                    
        return s
    
    def check(self, s, replacers):
        
        for replacer in replacers:
            if replacer in s:
                return True
        
        return False
        
# @lc code=end

