'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:07:13
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 11:09:13
FilePath: \Leetcode_Solver\821.字符的最短距离.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        res = []
        for i in range(len(s)):
            res.append(0)
        
        for i in range(len(s)):

            res[i] = (min([abs(i-j) for j in range(len(s)) if s[j] == c]))
        
        return res
# @lc code=end

