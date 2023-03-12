'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:35:21
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:49:24
FilePath: \Leetcode_Solver\1779.找到最近的有相同-x-或-y-坐标的点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        
        min_len = 999999
        for point in points :
            if point[0] == x or point[1] == y:
                length = abs(point[1]-y) + abs(point[0]-x) 
                if min_len > length:
                    min_len = length
        
        if min_len == 999999:
            return -1
        else:
            for i in range(len(points)):
                point = points[i]
                if point[0] == x or point[1] == y:
                    length = abs(point[1]-y) + abs(point[0]-x) 
                    if min_len == length:
                        return i

                
                
                

        
# @lc code=end

