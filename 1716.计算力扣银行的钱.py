'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-06 09:52:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-06 10:04:57
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1716.计算力扣银行的钱.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        
        if n < 7:
            return n*(n+1) //2
        else :
            res = 0
            round = n // 7
            res += 28*round 
            res += 7*((round)*(round-1)//2)
            res += sum([i+round for i in range(1, n%7+1)])

            return res 
        
# @lc code=end

