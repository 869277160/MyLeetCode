'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 17:34:16
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-18 13:34:53
FilePath: \Leetcode_Solver\121.买卖股票的最佳时机.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        length = len(prices)
        dp = [[0 for i in range(2)] for j in range(length)]
        for i in range(length):
            # print(dp)
            if i - 1 == -1:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])

        # for i in range(length):
        #     print(dp[i])
        return dp[-1][0]
        
        
        
        # res = 0
        # min_price = min(prices)
        # pos = prices.index(min_price)
        # if prices.count(min_price) == 1:
        #     if pos != len(prices)-1:
        #         return max(prices[pos:]) - min_price
        # else :
        #     for i in range(pos,len(prices)):
        #         if prices[i] == min_price :
        #             if max(prices[i:]) - min_price > res:
                        
        #                 res = max(prices[i:]) - min_price                     # res = prices[j] - prices[i]
        
        
  
        #     res = 0
        #     max_price = max(prices)
        #     for i in range(0,len(prices)):
        #         if prices[i] != max_price:
        #             for j in range(i+1,len(prices)):
        #                 if prices[j] > prices[i] and prices[j] - prices[i] > res:
        #                     res = prices[j] - prices[i]
            
        # return res
# @lc code=end

