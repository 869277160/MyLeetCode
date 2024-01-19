'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 12:24:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 12:26:19
FilePath: \Leetcode_Solver\744.寻找比目标字母大的最小字母.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        
        temp_min = 99999999
        for i in letters:
            if ord(i) > ord(target):
                temp_min = min(temp_min, ord(i))
                res = i
                break
        
        return res 
# @lc code=end

