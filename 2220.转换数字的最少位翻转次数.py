'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 00:13:12
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 00:34:41
FilePath: \Leetcode_Solver\2220.转换数字的最少位翻转次数.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2220 lang=python3
#
# [2220] 转换数字的最少位翻转次数
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        tmp = start ^ goal
        while tmp:
            res += tmp & 1
            tmp >>= 1
        return res
       
        # start_str = str(bin(start))[2:]
        # goal_str = str(bin(goal))[2:]
        # print(start_str,goal_str)
        
        # # max_len = max(len(start_str), len(goal_str))
        # # min_len = ,
        # # goal_str.ljust(len(start_str) - len(goal_str) ,'0')
        # # start_str.ljust(len(goal_str) - len(start_str) ,'0')
        # # print(start_str,goal_str)
        
        # if start < goal:
        #     res = 0
        #     i = 0
        #     for i in range(len(goal_str) - len(start_str)):
        #         if goal_str[i] == "1":
        #             res += 1
        #     i = len(goal_str) - len(start_str)
        #     for j in range(len(start_str)):
        #         print(start_str[j], goal_str[i])
        #         if start_str[j] == goal_str[i]:
        #             res += 1
        #         i +=1 
        #     print(res)
        # else :
        #     res = 0
        #     i = 0
        #     for i in range(len(start_str) - len(goal_str)):
        #         if start_str[i] == "1":
        #             res += 1
        #     i = len(start_str) - len(goal_str)
        #     for j in range(len(goal_str)):
        #         if goal_str[j] == start_str[i]:
        #             res += 1
        #         i +=1 
        #     print(res)
        
        # return res 
    
        
# @lc code=end

