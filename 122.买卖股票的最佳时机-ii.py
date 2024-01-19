'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-18 13:35:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-18 14:01:58
FilePath: \Leetcode_Solver\122.买卖股票的最佳时机-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_len = len(prices)
        dp = [[0,0] for i in range(total_len)]
        
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        
        for i in range(0,total_len):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        
        return dp[-1][0]
        
        
# @lc code=end

