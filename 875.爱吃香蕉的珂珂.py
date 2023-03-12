'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-12 12:30:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-12 13:08:37
FilePath: \Leetcode_Solver\875.爱吃香蕉的珂珂.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
    #     # 线性搜索各个位置对应速度是否符合条件
    #     speed = 0
    #     for speed in range(1,max(piles)):
    #         if self.FinishWithinTime(piles,speed,h):
    #            return speed
    #     return max(piles)
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 线性搜索各个位置对应速度是否符合条件
        # speed = 0
        min_speed, max_speed = 1, 1000000000 + 1
        while(min_speed < max_speed):
            mid = min_speed + (max_speed - min_speed) //2
            if self.FinishWithinTime(piles,mid,h):
                max_speed = mid
            else :
                min_speed = mid + 1 
        
        return min_speed
        
    def FinishWithinTime(self,piles,speed,h):
        total_time = 0
        for pile in piles:
            temp_time = pile//speed + (1 if pile%speed else 0)
            total_time += temp_time
        
        return total_time <= h

# @lc code=end

