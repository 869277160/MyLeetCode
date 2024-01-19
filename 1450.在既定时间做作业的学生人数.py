'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-23 12:56:07
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-23 13:00:47
FilePath: \Leetcode_Solver\1450.在既定时间做作业的学生人数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#

# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        
        return count
        
# @lc code=end

