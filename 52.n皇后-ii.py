'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-12 23:19:27
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-12 23:27:17
FilePath: \Leetcode_Solver\52.n皇后-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def backtrack(i,col,z_diagonal,f_diagonal):
            if i == n:return  True
            for j in range(n):
                if j not in col and i + j not in  z_diagonal and i - j not in f_diagonal:
                    if backtrack(i+1, col | {j}, z_diagonal |{i + j} , f_diagonal |{i - j}  ) :
                        self.res += 1
            return False
        backtrack(0,set(),set(),set())    
        return self.res

# @lc code=end

