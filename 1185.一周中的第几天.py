'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 09:22:55
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 09:23:09
FilePath: \Leetcode_Solver\1185.一周中的第几天.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] 一周中的第几天
#

# @lc code=start
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        import datetime
        return datetime.date(year,month,day).strftime("%A")
        
        
# @lc code=end

