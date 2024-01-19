'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 13:27:03
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 13:50:36
FilePath: \Leetcode_Solver\1544.整理字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        
        alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
        alphabet2 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        
        replacers = []
        for i in range(0,len(alphabet),2):
            replacers.append(alphabet[i:i+2])
            replacers.append(alphabet2[i:i+2])
            
        res = s 
        # current_stage = True
        while(self.check(replacers,res)):
            if res == "":
                return res
            for replacer in replacers:
                res = res.replace(replacer,"") 
            print(res)
        return res

    def check(self, replacers, s):
        if len(s) ==1 :
            return False 
        
        for replacer in replacers:
            if replacer in s :
                return True
        
        return False
            
        
# @lc code=end

