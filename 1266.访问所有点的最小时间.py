'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 12:10:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 12:10:37
FilePath: \Leetcode_Solver\1266.访问所有点的最小时间.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])) for i in range(1, len(points)))
# @lc code=end

