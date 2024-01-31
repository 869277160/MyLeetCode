'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 22:09:47
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 22:18:03
FilePath: \Leetcode_Solver\2432.处理用时最长的那个任务的员工.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2432 lang=python3
#
# [2432] 处理用时最长的那个任务的员工
#

# @lc code=start
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        time = [0 for i in range(n)]
        start = 0
        for i in range(len(logs)):
            time[logs[i][0]] = max(time[logs[i][0]], logs[i][1]-start)
            start = logs[i][1]
        
        return time.index(max(time))
        
        
# @lc code=end

