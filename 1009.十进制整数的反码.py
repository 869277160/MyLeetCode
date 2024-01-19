'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:44:25
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 11:44:58
FilePath: \Leetcode_Solver\1009.十进制整数的反码.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0:
            return 1 
        
        for i in range(32):
            if n < 2 ** i:
                return 2 ** i - 1 - n
        
# @lc code=end

