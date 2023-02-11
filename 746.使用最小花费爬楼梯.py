'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 09:40:06
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-10 09:51:56
FilePath: \Leetcode_Solver\746.使用最小花费爬楼梯.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # 最初子问题
        if len(cost) == 0 : return 0
        if len(cost) <= 2 : return min(cost)
        
        # 迭代求解剩下的部分。
        return min(self.minCostClimbingStairs(cost[1:]) + cost[0], self.minCostClimbingStairs(cost[2:]) + cost[1])
        
# @lc code=end

