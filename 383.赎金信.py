'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-06 10:21:53
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-06 10:25:14
FilePath: \Leetcode_Solver\383.赎金信.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    # 利用list作为集合，同时统计每个字符出现的次数进行对比即可。
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_r = [0]*26
        count_m = [0]*26
        
        for i in ransomNote:
            count_r[ord(i)-ord('a')] += 1
        
        for i in magazine:
            count_m[ord(i)-ord('a')] += 1
        
        for i in range(26):
            if count_r[i] > count_m[i]:
                return False 
        
        return True 
# @lc code=end

