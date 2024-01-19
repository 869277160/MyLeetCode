'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 22:01:06
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-19 21:49:03
FilePath: \Leetcode_Solver\1576.替换所有的问号.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

@lc code=start
class Solution:
    def modifyString(self, s: str) -> str:
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        # alphabet_modified = "bcdefghijklmnopqrstuvwxyza"
        
        # # for i in range(len(s)):
        # #     if s[i] == "?":
        # if "?" not in s:
        #     return s
        # else:
        #     if s[0] == "?":
        #         return alphabet_modified[alphabet.index(s[1])] + s[1:]
        #     elif s[-1] == "?"
        #     else:
        #         return s[0]
        res = list(s)
        n = len(res)
        for i in range(n):
            if res[i] == '?':
                for b in "abc":
                    if not (i > 0 and res[i - 1] == b or i < n - 1 and res[i + 1] == b):
                        res[i] = b
                        break
        return ''.join(res)

        
# @lc code=end

