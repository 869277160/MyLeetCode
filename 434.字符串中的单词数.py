'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 18:15:10
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 18:15:27
FilePath: \Leetcode_Solver\434.字符串中的单词数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        # 单次遍历，计算空格数，返回空格数+1
        return len(s.split())
# @lc code=end

