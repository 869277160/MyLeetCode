'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 11:11:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 11:13:04
FilePath: \Leetcode_Solver\509.斐波那契数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1 
        if n==2: return 1
        if n==3: return 2
        if n==4: return 3
        if n > 4:
            return self.fib(n-1)+self.fib(n-2)
        
        
# @lc code=end

