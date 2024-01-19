'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-19 15:43:18
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-19 15:47:32
FilePath: \Leetcode_Solver\1876.长度为三且各字符不同的子字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1876 lang=python3
#
# [1876] 长度为三且各字符不同的子字符串
#

# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        if len(s) < 3:
            return 0
        
        res_dict = {}
        for i in range(0, len(s)-2):
            if self.check(s[i:i+3]):
                if s[i:i+3] not in res_dict:
                    res_dict[s[i:i+3]] = 0
                res_dict[s[i:i+3]] += 1
        
        return sum(res_dict.values())
    
    def check(self, s):
        return len(set(s)) == 3
        
# @lc code=end

