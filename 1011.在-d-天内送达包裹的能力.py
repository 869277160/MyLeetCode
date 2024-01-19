'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-07 09:55:34
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-12 15:09:00
FilePath: \Leetcode_Solver\1011.在-d-天内送达包裹的能力.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
    #     # 线性搜索各个位置对应载重量是否符合条件
    #     # ship = 0
    #     # for ship in range(max(weights), sum(weights)+1):
    #     #     if self.FinishWithinDays(weights, ship, days):
    #     #         return ship 
        
        # 二分搜索各个位置对应载重量是否符合条件
        min_ship, max_ship = max(weights), sum(weights)
        while(min_ship < max_ship):
            mid = (min_ship + max_ship) // 2
            if self.FinishWithinDays(weights, mid, days):
                max_ship = mid
            else :
                min_ship = mid + 1
            
        return min_ship

    #     # return sum(weights)

    def FinishWithinDays(self, weights, ship,days):
        current_day = 0
        pos = 0
        while(pos < len(weights)):
            cap = ship
            while(pos< len(weights)):
                if cap < weights[pos]:
                    break
                else:
                    cap -= weights[pos]
                    pos += 1
            current_day += 1
        
        return current_day <= days
            
        # day = 0
        # i = 0
        # while i < len(weights):
        #     # 尽可能多装货物
        #     cap = ship
        #     while i < len(weights):
        #         if cap < weights[i]:
        #             break
        #         else:
        #             cap -= weights[i]
        #             i += 1
        #     day += 1
        # return day <= days

    # def shipWithinDays(self, weights: List[int], days: int) -> int:
    #     left = max(weights)
    #     right = sum(weights)

    #     while left < right:
    #         mid = (left + right) // 2
    #         if self.f(weights, mid) <= days:
    #             right = mid
    #         else:
    #             left = mid + 1

    #     return left

    # # 定义：当运载能力为 x 时，需要 f(x) 天运完所有货物
    # # f(x) 随着 x 的增加单调递减
    # def f(self, weights, x):
    #     days = 0
    #     i = 0
    #     while i < len(weights):
    #         # 尽可能多装货物
    #         cap = x
    #         while i < len(weights):
    #             if cap < weights[i]:
    #                 break
    #             else:
    #                 cap -= weights[i]
    #                 i += 1
    #         days += 1
    #     return days
    
# @lc code=end

