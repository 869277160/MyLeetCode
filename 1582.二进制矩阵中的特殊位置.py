'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:32:51
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:34:38
FilePath: \Leetcode_Solver\1582.二进制矩阵中的特殊位置.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        res = 0
        for i  in range (len(mat)):
            if sum(mat[i]) == 1:
                for j in range(len(mat[0])):
                    if mat[i][j] == 1:
                        if sum([mat[k][j] for k in range(len(mat))]) == 1:
                            res +=1
        
        return res
        
        
# @lc code=end

