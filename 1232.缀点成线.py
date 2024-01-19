'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-22 10:10:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-22 10:16:36
FilePath: \Leetcode_Solver\1232.缀点成线.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if (len(coordinates) == 2) or (len(coordinates) == 1):
            return True
        else :
            k,b = self.get_k_b(coordinates[0],coordinates[1])
            
            if k != None :
                for i in range(2,len(coordinates)):
                    if coordinates[i][1] != k*coordinates[i][0] + b:
                        return False
            
                return True
            else :
                for i in range(2,len(coordinates)):
                    if coordinates[i][0] != coordinates[0][0]:
                        return False
                return True

    def get_k_b(self, point1, point2):
        k=0
        b=0
        
        if point2[0] == point1[0]:
            return None, point1[0]
        else:
            k = (point2[1]-point1[1])/(point2[0]-point1[0])
            b = point1[1] - k*point1[0]
            
            return k,b
# @lc code=end

