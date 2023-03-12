'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-22 09:27:03
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-22 09:40:26
FilePath: \Leetcode_Solver\6.n-字形变换.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]
        else:
                 
            res, n = [''] * numRows, 2 * numRows - 2

            for i, c in enumerate(s):
                res[min(idx := i % n, n - idx)] += c
            
            return ''.join(res)
        
        # for i in range(0,len(s),numRows):
        #     str1 += s[i]
        
        
# @lc code=end

