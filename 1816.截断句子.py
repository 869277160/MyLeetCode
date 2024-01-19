'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 16:15:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 16:16:49
FilePath: \Leetcode_Solver\1816.截断句子.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1816 lang=python3
#
# [1816] 截断句子
#

# @lc code=start
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return (" ".join(s.split(" ")[:k]))
        
# @lc code=end

