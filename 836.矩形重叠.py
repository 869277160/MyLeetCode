'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:52:56
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 23:04:47
FilePath: \Leetcode_Solver\836.矩形重叠.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec2[0] and rec1[2] == rec2[2] and rec1[1] == rec2[1] and rec1[3] == rec2[3]:
            return True 
        if rec1[0] == rec2[2] and rec1[2] == rec2[0] and rec1[1] == rec2[3] and rec1[3] == rec2[1]:
            return True 

        if self.check(rec1,rec2[0],rec2[1]) or \
            self.check(rec1,rec2[2],rec2[1]) or \
            self.check(rec1,rec2[0],rec2[3]) or \
            self.check(rec1,rec2[2],rec2[3]) :
                return True
        else :
            return False
        
    def check(self,rec,x,y):
        max_x = max(rec[0],rec[2])
        min_x = min(rec[0],rec[2])
        max_y = max(rec[1],rec[3])
        min_y = min(rec[1],rec[3])
        if x > min_x and x < max_x and y > min_y and y < max_y:
            return True
        if (x == min_x or x == max_x ) and (y == min_y or y == max_y):
            
            return False
        
        
        
        
# @lc code=end

