'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 14:35:08
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 14:37:43
FilePath: \Leetcode_Solver\1175.质数排列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
        prime_count = 0
        non_prime_count = 0
        for i in range(1, n+1):
            if self.is_prime(i):
                prime_count += 1
            else:
                non_prime_count += 1

        res = 1 
        for i in range(1, prime_count+1):
            res = (res * i) % (10**9 + 7)
        
        for i in range(1,non_prime_count+1):
            res = (res * i) % (10**9 + 7)
        
        return res
        

    def is_prime(self, n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

# @lc code=end

