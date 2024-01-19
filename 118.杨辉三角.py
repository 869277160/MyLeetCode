'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 10:51:17
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 10:53:28
FilePath: \Leetcode_Solver\118.杨辉三角.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0 : return []
        if numRows == 1 : return [[1]]
        if numRows == 2 : return [[1],[1,1]]
        if numRows > 2 :
            res = [[1],[1,1]]
            for i in range(2,numRows):
                res.append([1])
                for j in range(1,i):
                    res[i].append(res[i-1][j-1]+res[i-1][j])
                res[i].append(1)
                
            return res
        
# @lc code=end

