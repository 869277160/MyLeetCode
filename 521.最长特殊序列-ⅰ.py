'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 20:27:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:37:38
FilePath: \Leetcode_Solver\521.最长特殊序列-ⅰ.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # 动态规划求解
        dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
        
        
        # for i in range(len(a)+1):
        #     if b[0] in a[:i]:
        #         dp[i][0] = i-1 
        #     else:
        #         dp[i][0] = i
        # for j in range(len(b)+1):
        #     if a[0] in b[:j]:
        #         dp[0][j] = j-1
        #     else :
        #         dp[0][j] = j
        
        r= 0 else -1 
        
# @lc code=end

