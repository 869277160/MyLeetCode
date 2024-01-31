'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 19:33:28
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 19:34:50
FilePath: \Leetcode_Solver\2706.购买两块巧克力.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2706 lang=python3
#
# [2706] 购买两块巧克力
#

# @lc code=start
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        rest = money - prices[0] -prices[1]
        
        return rest if rest >=0 else money
        
        
# @lc code=end

