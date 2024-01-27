'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-23 13:24:38
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-23 15:43:14
FilePath: \Leetcode_Solver\1011.在-d-天内送达包裹的能力.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#
from typing import List
# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        min_cap = max(weights)
        max_cap = sum(weights)
        
        
        while min_cap < max_cap:
            
            current_cap = min_cap + (max_cap - min_cap) //2 
            print(min_cap, current_cap, max_cap)
            print(self.f(weights, current_cap))
            if self.f(weights, current_cap) < days:
                # 说明运力足够，继续在 [min_cap , current_cap)中搜索
                max_cap = current_cap
            elif self.f(weights, current_cap) > days:
                # 说明运力不够，继续在 (current_cap , max_cap]中搜索
                min_cap = current_cap + 1
            elif self.f(weights, current_cap) == days:
                # 说明运力足够， 但是无法保证是最优的运力
                # 继续在 [min_cap , current_cap) 中搜索
                max_cap = current_cap
            print(min_cap, max_cap)
        return min_cap 
    
    def f(self, weights, current_cap: int) -> int:
        # [10,50,100,100,50,100,100,100]
        days = 0
        current_loan = current_cap
        for i in range(len(weights)):
            weight = weights[i]
            current_loan = current_loan - weight
            
            if i != len(weights) - 1:
                if current_loan > 0:
                    pass 
                if current_loan == 0:
                    days += 1 
                    current_loan = current_cap
                if current_loan < 0:
                    days += 1
                    current_loan = current_cap - weight
                    
            if i == len(weights) - 1:
                if current_loan > 0:
                    days += 1
                if current_loan == 0:
                    days += 1 
                if current_loan < 0:
                    days += 2
        
            # print(days, current_loan)
            
        return days 
    
# @lc code=end

if __name__ == "__main__":
    
    s = Solution()
    print(s.f([10,50,100,100,50,100,100,100],155))
    print(s.f([1,2,3,4,5,6,7,8,9,10],15))