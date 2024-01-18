'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 15:19:48
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-08-27 23:30:38
FilePath: \Leetcode_Solver\62.不同路径.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
from functools import cache
# @lc code=start
class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 1 or n == 1:
    #         return 1
    #     if m == 2:
    #         return n
    #     if n == 2:
    #         return m
        
    #     res = []
    #     for i in range(m):
    #         if i == 0:
    #             res.append([1 for _ in range(n)])
    #         elif i == 1:
    #             res.append([k+1 for k in range(n)])
    #         else:
    #             res.append([0 for _ in range(n)])
    #             if n > 1:
    #                 res[i][0] = 1
    #                 res[i][1] = i+1
                
        
    #     for i in range(2,m):
    #         for j in range(2,n):
    #             res[i][j] = res[i-1][j]+res[i][j-1]
    
    #     return res[m-1][n-1]
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if m == 2:
            return n
        if n == 2:
            return m
        
        @ cache
        def dfs(i,j):
            if i == 0 or j ==0 :
                return 1 
            else :
                return dfs(i-1,j)+dfs(i,j-1)

        return dfs(m-1,n-1)
    
        
# @lc code=end

