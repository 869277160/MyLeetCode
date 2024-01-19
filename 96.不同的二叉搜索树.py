'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-09 09:44:18
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-25 20:25:22
FilePath: \Leetcode_Solver\96.不同的二叉搜索树.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 : 
            return 0
        if n == 1 : 
            return 1
        if n == 2 : 
            return 2
        if n == 3 : 
            return 5
        else:
            dp = [0 for i in range(n+1)]
            dp[:6] = [1,1,2,5,14,42]
            for i in range(6,n+1):
                # (1) search all the number in the list 
                # for j in range(0,i):
                #     dp[i] += dp[j] * dp[i-1-j] 
                
                # (2) based on the dp function 
                dp[i] = 2 * (sum([dp[j] * dp[i-1-j] for j in range(0,i//2)]))
                if i % 2 == 1:
                    dp[i] += dp[i//2] * dp[i//2]
                    
                
                
            return dp[n]
        
        
# @lc code=end

