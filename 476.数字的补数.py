'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:02:33
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 22:06:54
FilePath: \Leetcode_Solver\476.数字的补数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        
        
        for i in range(0,32):
            if 2**i > num:
                return 2**i-1 - num 
            if 2**i == num:
                return 2**i-1 
        
        
        
        
# @lc code=end

