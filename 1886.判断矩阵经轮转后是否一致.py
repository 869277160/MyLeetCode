'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 23:17:27
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 23:33:10
FilePath: \Leetcode_Solver\1886.判断矩阵经轮转后是否一致.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1886 lang=python3
#
# [1886] 判断矩阵经轮转后是否一致
#

# @lc code=start
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
    
        # 一定要画图!!!
        
        if self.SRotation(mat) == target or self.SRotation2(mat) == target or self.SRotation3(mat) == target or mat == target:
            return True 
        else :
            return False
        
    
    # 顺时针
    def SRotation(self,mat):
        res = []
        for i in range(len(mat)):
            res.append([mat[j][i] for j in range(len(mat)-1,-1,-1)])
        return res 

    
    # 顺时针2， 逆序遍历
    def SRotation2(self,mat):
        res = []
        for i in range(len(mat)-1,-1,-1):
            res.append([mat[i][j] for j in range(len(mat)-1,-1,-1)])
        return res 
        
    
    # 逆时针
    def SRotation3(self,mat):
        res = []
        for i in range(len(mat)-1,-1,-1):
            res.append([mat[j][i] for j in range(len(mat))])
        return res 

# @lc code=end

