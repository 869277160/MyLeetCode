'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-07 17:55:03
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-07 17:58:17
FilePath: \Leetcode_Solver\2399.检查相同字母间的距离.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2399 lang=python3
#
# [2399] 检查相同字母间的距离
#

# @lc code=start
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        start = ord('a')
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i-1 != distance[ord(s[i])-start]:
                        return False 
        
        return True 
# @lc code=end

