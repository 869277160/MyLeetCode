'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-08 13:22:16
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 12:23:01
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
            return mat[0]
        
        n = len(mat) -1
        m = len(mat[0]) -1 
        
        level = m + n + 1
        res = []
        # i,j = 0,0

        for x in range(level+1):    # 每层的横纵索引之和相等，刚好等于 层数值+1
            if x % 2 == 0:      # 索引和为{偶}数，向上遍历，{横}索引值递减，遍历值依次是(x,0),(x-1,1),(x-2,2),...,(0,x)，不要索引出界的，即可
                for i in range(x,-1,-1):
                    j = x - i
                    print(i,j)
                    if i <= n and j <= m:
                        res.append(mat[i][j])
                    elif j > m:
                        break
                    else:
                        continue
            else:                # 索引和为{奇}数，向下遍历，{纵}索引值递减，遍历值依次是(0,y),(1,y-1),(2,y-2),...,(y,0)，不要索引出界的，即可
                for j in range(x, -1, -1):
                    i = x - j
                    # print(i,j)
                    if i <= n and j <= m:
                        res.append(mat[i][j])
                    elif i > n :
                        break
                    else:
                        continue

        return res
            
