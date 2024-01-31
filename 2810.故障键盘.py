'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 22:49:20
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 22:51:05
FilePath: \Leetcode_Solver\2810.故障键盘.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2810 lang=python3
#
# [2810] 故障键盘
#

# @lc code=start
class Solution:
    def finalString(self, s: str) -> str:
        s = s.replace("ii","")
        res = ""
        for c in ((s)):
            if c == "i":
                res = res[::-1]
            else:
                res += (c)
                
        return res 
        
# @lc code=end

