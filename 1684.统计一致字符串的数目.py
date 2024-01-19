'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-03-07 10:07:13
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-03-07 10:08:19
FilePath: \Leetcode_Solver\1684.统计一致字符串的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        def check(word, allowed):
            for s in word:
                if s not in allowed:
                    return False
            return True
        
        
        res = 0
        for word in words:
            if check(word, allowed):
                res += 1
        return res 
# @lc code=end

