'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 12:40:06
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 13:16:09
FilePath: \Leetcode_Solver\812.最大三角形面积.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

# @lc code=start
import math 

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        
        
        res = 0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                
                    a = math.sqrt(pow(abs(points[j][0] - points[i][0]),2)+pow(abs(points[j][1] - points[i][1]),2))
                    b = math.sqrt(pow(abs(points[k][0] - points[j][0]),2)+pow(abs(points[k][1] - points[j][1]),2))
                    c = math.sqrt(pow(abs(points[i][0] - points[k][0]),2)+pow(abs(points[i][1] - points[k][1]),2))
                    l = (a+b+c)*0.5;
                    total = abs(l*(l-a)*(l-b)*(l-c))
                    res = max(res,math.sqrt(total))

        return res;

    # def distance(self, a, b):
    #     x = (a[0] - b[0]) **2 
    #     y = (a[1] - b[1]) **2
        
    #     return math.sqrt(,2)+pow(abs(a[1] - b[1]),2))

# @lc code=end

