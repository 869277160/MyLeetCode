'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-08 13:22:16
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-08 13:57:26
FilePath: \Leetcode_Solver\498.对角线遍历.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if mat == None :
            return []
        if len(mat) == 1:
            return mat[1]
        
        m = len(mat)
        n = len(mat[0])
        
        res = []
        i,j = -1,-1
        while(i<m and j<n):
            res,i,j = self.upOrder(mat,res,i,j,m,n)
            res,i,j = self.downOrder(mat,res,i,j,m,n)
        return res 
        
        
        
    def upOrder(self, mat, res, i, j,m,n):
        # 左上角
        if i == 0:
            res.append(mat[i][j])
            j += 1
            return res,i,j
        # 右下角
        if j == n-1:
            res.append(mat[i][j])
            i -= 1
            return res,i,j
        else :
            # 直接开始遍历
            while(i>=0 and j>=0):
                res.append(mat[i][j])
                i -= 1
                j += 1
            # 两种转向条件
            if i == 0 and j < len(mat[0])-1:
                j += 1
            if j == len(mat[0])-1:
                i += 1
        
        return res,i,j
    
    def downOrder(self,mat, res,i,j,m,n):
        # 向下搜索
        while(i > 0 and j < n):
            res.append(mat[i][j])
            i -= 1
            j += 1
        
        # 转向条件
        if i == 0 and j < n:
            j -= 1 
        if j == n-1:
            i +=1 
    
        return res,i,j

