'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 20:37:34
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 20:38:35
FilePath: \Leetcode_Solver\2651.计算列车到站时间.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2651 lang=python3
#
# [2651] 计算列车到站时间
#

# @lc code=start
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        
        return (arrivalTime + delayedTime) % 24
        
        
        
        
# @lc code=end

