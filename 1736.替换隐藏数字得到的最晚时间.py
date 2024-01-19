'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 09:29:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 09:35:40
FilePath: \Leetcode_Solver\1736.替换隐藏数字得到的最晚时间.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0] == "?":
            if time[1] == "?" or time[1] <= "3":
                time = "2" + time[1:]
            elif time[1] > "3":
                time = "1" + time[1:]
        # print(time)
        if time[1] == "?":
            if time[0] == "2":
                time = time[0] + "3" + time[2:]
            if time[0] == "1" or time[0] == "0":
                time = time[0] + "9" + time[2:]
        if time[3] == "?":
            time = time[:3] + "5" + time[4:]
        if time[-1] == "?":
            time = time[:-1] + "9"
            
    
        return time 
# @lc code=end

