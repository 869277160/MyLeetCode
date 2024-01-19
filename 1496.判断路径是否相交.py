'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 11:36:25
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 14:38:45
FilePath: \Leetcode_Solver\1496.判断路径是否相交.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        all_points = [[0,0]]
        for i in range(len(path)):
            if path[i] == 'N':
                all_points.append([all_points[-1][0],all_points[-1][1]+1])
            if path[i] == "E":
                all_points.append([all_points[-1][0]+1,all_points[-1][1]])
            if path[i] == "S":
                all_points.append([all_points[-1][0],all_points[-1][1]-1])
            if path[i] == "W":
                all_points.append([all_points[-1][0]-1,all_points[-1][1]])
            
            if all_points[-1] in all_points[:-1]:
                return True
        
        return False 
        
        # import collections
        
        # directions = collections.Counter(path)
        
        # if directions['N'] == directions['S'] and directions['E'] != directions['W']:
        #     return True
        # elif directions['N'] != directions['S'] and directions['E'] == directions['W']:
        #     return True
        
        # else:
        #     return False
        
        
        
# @lc code=end

