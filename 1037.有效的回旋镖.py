'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-10 16:33:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-11 17:40:46
FilePath: \Leetcode_Solver\1037.有效的回旋镖.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # same point
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        # same x 
        if points[1][0] == points[0][0] and points[0][0] == points[2][0]:
            return False
        # same y 
        if points[1][1] == points[0][1] and points[0][1] == points[2][1]:
            return False
        # same slope 
        
        v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        v2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
        return v1[0] * v2[1] - v1[1] * v2[0] != 0


        # return True 
        


# @lc code=end

