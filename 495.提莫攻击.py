'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 11:21:13
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 11:36:38
FilePath: \Leetcode_Solver\495.提莫攻击.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        # 暴力遍历
        # res = 0
        # temp_duration = 0
        # for i in range(min(timeSeries),max(timeSeries)+1+duration):
        #     if i in timeSeries:
        #         temp_duration = duration

        #     if temp_duration > 0:
        #         res += 1
        #         temp_duration -= 1
           
        # return res 
        
        
        # 优化
        res = 0
        current_end = 0
        pos = 0
        while(pos < len(timeSeries)):
            if timeSeries[pos] >= current_end:
                res += duration
                current_end = timeSeries[pos] + duration
            else:
                res += timeSeries[pos] + duration - current_end
                current_end = timeSeries[pos] + duration
            pos += 1
        
        return res 
# @lc code=end

