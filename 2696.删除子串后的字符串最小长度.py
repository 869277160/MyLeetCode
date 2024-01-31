'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 21:18:33
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 21:19:39
FilePath: \Leetcode_Solver\2696.删除子串后的字符串最小长度.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2696 lang=python3
#
# [2696] 删除子串后的字符串最小长度
#

# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = s.replace("AB", "")
            if "CD" in s:
                s = s.replace("CD", "")
        
        return len(s)
# @lc code=end

