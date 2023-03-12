'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-06 14:51:53
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-06 14:57:11
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1154.一年中的第几天.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        
        year,month,day = date.split('-')
        year,month,day = int(year),int(month),int(day)
        
        month_add = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if ((year) % 4 == 0 and (year) % 100 != 0) or ((year) % 400 == 0):
            month_add[1] = 29

        if month > 1 :
            return sum(month_add[:month-1])+day
        else :
            return day
# @lc code=end

