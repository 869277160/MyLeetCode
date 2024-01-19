'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-15 09:52:05
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-15 10:25:58
FilePath: \Leetcode_Solver\72.编辑距离.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int: 
        
        len1, len2 = len(word1), len(word2)
        # 快速创建有效的二维数组
        dp = [[0 for i in range(len2+1)] for j in range(len1+1)]
        
        for i in range(len1+1):
            dp[i][0] = i
        for j in range(len2+1):
            dp[0][j] = j
        
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    
        return dp[len1][len2]
        
# @lc code=end

