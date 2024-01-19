'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 16:19:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 16:21:46
FilePath: \Leetcode_Solver\2490.回环句.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2490 lang=python3
#
# [2490] 回环句
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        start = [word[0] for word in words]
        end = [word[-1] for word in words]
        
        end = end[-1:] + end[:-1]
        
        if start == end:
            return True
        else:
            return False
        
# @lc code=end

