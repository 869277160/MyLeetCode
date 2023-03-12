'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 17:25:36
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 18:04:58
FilePath: \Leetcode_Solver\279.完全平方数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    # def numSquares(self, n: int) -> int:
    #     import math 
        
    #     if int(math.sqrt(n)) *int(math.sqrt(n)) == n :
    #         return 1
        
    #     res = [10000000 for _ in range(n+1)]
    #     res[:10]=[0,1,2,3,1,2,3,4,2,1,2]
    #     if n > 10 :
    #         for i in range(11,n+1):
    #             if int(math.sqrt(n)) *int(math.sqrt(n)) == n :
    #                 res[i] =1
    #             else:

    #                     res[i] = min(res[i], res[i - j * j] + 1);

    #     return res[n]
            
        
        
    def numSquares(self, n: int) -> int:
        goods = []
        for i in range(1,101):
            goods.append(i * i)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for g in goods:
            for j in range(1,n+1):
                if j - g >= 0:
                    dp[j] = min(dp[j-g] + 1,dp[j])
        return dp[n]
# @lc code=end

