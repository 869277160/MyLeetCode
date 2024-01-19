'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-10 09:40:06
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 10:41:47
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
    def minCostClimbingStairs(self, cost: List[int]) :
        
        # def helper(cost,memo):
        #     res = 0
        #     step = 0
        #     while(step<len(cost)):
        #         if 
                
        #         if self.minCostClimbingStairs(cost[step:]) + cost[step] < self.minCostClimbingStairs(cost[step+1:]) + cost[step+1]:
        #             res += self.minCostClimbingStairs(cost[step:]) + cost[step]
        #             step +=1 
        #         else :
        #             res += self.minCostClimbingStairs(cost[step+1:]) + cost[step+1]
        #             step +=2 

        #     return res 
        
        # 将上楼梯改为下楼梯
        # 最初子问题
        if len(cost) == 0 : return 0
        if len(cost) <= 2 : return min(cost)
        
        res = [0 for i in cost]
        res[-2:] = cost[-2:]
        for i in range(len(cost)-3,-1,-1):
            res[i] += min(res[i+1] + cost[i], res[i+2] + cost[i]) 
            
        ouptut = min(res[0],res[1])
        # return ouptut
        return ouptut 
        
        # memo = [-1 for i in cost]
        # res = helper(cost,memo)
        
        
        # return res 
        
        # # 迭代求解剩下的部分。
        # return min(self.minCostClimbingStairs(cost[1:]) + cost[0], self.minCostClimbingStairs(cost[2:]) + cost[1])
        
# @lc code=end

