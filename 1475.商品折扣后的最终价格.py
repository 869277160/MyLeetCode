'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-23 13:04:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-23 13:13:07
FilePath: \Leetcode_Solver\1475.商品折扣后的最终价格.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        res =[]
        for i in range(len(prices)-1):
            if min(prices[i+1:]) > prices[i]:
                res.append(prices[i])
            else:
                for j in range(i+1,len(prices)):
                    if prices[j] <= prices[i]:
                        res.append(prices[i] - prices[j])
                        break
                        
        res.append(prices[-1])
        
        return res 
        
# @lc code=end

