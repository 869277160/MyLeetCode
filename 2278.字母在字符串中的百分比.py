'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:33:45
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:34:26
FilePath: \Leetcode_Solver\2278.字母在字符串中的百分比.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2278 lang=python3
#
# [2278] 字母在字符串中的百分比
#

# @lc code=start
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        count = 0
        for i in s:
            if i == letter:
                count += 1
        
        return int(count / len(s) * 100)
        
        
# @lc code=end

