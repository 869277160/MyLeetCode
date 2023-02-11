'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-06 09:28:02
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 10:11:33
FilePath: \Leetcode_Solver\58.最后一个单词的长度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "":
            return 0 
        count = 0
        for i in s:
            if i == " ":
                count += 1 
        if count == 0 :
            return len(s)
        else :
            return len(s.split()[-1])
            
            
            # bos = len(s) - 1
            # eos = len(s)
            # for i in range(1,len(s)):
            #     if s[len(s)-i] == " ":
            #         bos -= 1
            #         eos -= 1
            #     if s[len(s)-i] != " ":
            #         if len(s)-i-1 < 0:
            #             return eos
            #         else :
            #             if s[len(s)-i-1] == " ":
            #                 bos = len(s) - i - 1
            #                 return eos - bos - 1 
            #             else :
            #                 bos -= 1
# @lc code=end

