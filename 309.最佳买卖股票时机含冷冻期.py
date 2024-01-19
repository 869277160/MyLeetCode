'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-18 14:03:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-18 14:03:25
FilePath: \Leetcode_Solver\309.最佳买卖股票时机含冷冻期.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total_len = len(prices)
        dp = [[0,0] * 2 for _ in range(total_len)]
        
        for i in range(total_len):
            if i - 1 == -1:
                # base case 1
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            if i - 2 == -1:
                # base case 2
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                # 当 i = 1 时，dp[i-2] 不合法，所以只能从 dp[i-1][1] 转移过来
                dp[i][1] = max(dp[i-1][1], -prices[i])
                # 解释如上
                continue
            
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            
        return dp[-1][0]
        
        
# @lc code=end

