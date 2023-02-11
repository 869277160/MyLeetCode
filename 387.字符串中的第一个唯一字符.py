'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-06 10:25:47
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-06 10:28:31
FilePath: \Leetcode_Solver\387.字符串中的第一个唯一字符.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    # 集合思想
    def firstUniqChar(self, s: str) -> int:
        char_counter = [0]*26
        
        for i in s:
            char_counter[ord(i)-ord('a')] += 1
        
        for i in range(len(s)):
            if char_counter[ord(s[i])-ord('a')] == 1:
                return i
        return -1 
        
        
        
        
# @lc code=end

