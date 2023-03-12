'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 23:09:07
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 23:11:07
FilePath: \Leetcode_Solver\1137.第-n-个泰波那契数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        
        res =[0] * (n+1)
        res[:5] = [0,1,1,2,4]
        
        if n < 5 :
            return res[n]
        else :
            for i in range(5, n+1):
                res[i] = res[i-1] + res[i-2] + res[i-3]
                
            return res[n]
        
# @lc code=end

