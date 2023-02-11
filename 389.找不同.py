'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-08 10:26:02
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-08 10:30:56
FilePath: \Leetcode_Solver\389.找不同.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        
        count_s = [0]*30
        count_t = [0]*30

        for i in s:
            count_s[ord(i)-ord("a")+1] += 1 
        
        for j in t:
            count_t[ord(j)-ord("a")+1] += 1 
            if count_t[ord(j)-ord("a")+1] > count_s[ord(j)-ord("a")+1]:
                return j
        
# @lc code=end

