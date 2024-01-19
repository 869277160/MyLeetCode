'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 09:51:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 09:59:51
FilePath: \Leetcode_Solver\2437.有效时间的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2437 lang=python3
#
# [2437] 有效时间的数目
#

# @lc code=start
class Solution:
    def countTime(self, time: str) -> int:
        
        count_hour = 1
        if time[0] == "?":
            if time[1] == "?":
                count_hour = 24 
            elif time[1] <= "3":
                count_hour = 3 
            elif time[1] > "3":
                count_hour = 2 
        else :
            if time[1] == "?":
                count_hour = 10 if time[0] == "0" or time[0] == "1" else 4
            else:
                count_hour = 1 
        
        
        count_min = 1
        if time[3] == "?":
            if time[4] == "?":
                count_min = 60
                return count_hour * count_min
            else :
                count_min = 6
                return count_hour * count_min
        else:
            if time[4] == "?":
                count_min = 10
                return count_hour * count_min
            else:
                return count_hour * count_min
            
        
# @lc code=end

