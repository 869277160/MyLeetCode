'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-09 09:20:44
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-09 09:21:24
FilePath: \Leetcode_Solver\1689.十-二进制数的最少数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1689 lang=python3
#
# [1689] 十-二进制数的最少数目
#

# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max([i for i in str(n)]))
# @lc code=end

