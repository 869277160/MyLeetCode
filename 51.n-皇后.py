'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-12 23:12:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-12 23:19:26
FilePath: \Leetcode_Solver\51.n-皇后.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 生成矩阵
        if n == 1 :
            return [["Q"]]
        elif n == 2 or n == 3:
            return []
        else:
            self.res = []
            self.s = "." * n
            self.n = n
            self.solveNQueensHelper(0,[],set(),set(),set())  
            return self.res 

    def solveNQueensHelper(self,i, tmp,col,z_diagonal,f_diagonal):
        if i == self.n:
            self.res.append(tmp)
            return 
        for j in range(self.n):
            if j not in col and i + j not in  z_diagonal and i - j not in f_diagonal:
                self.solveNQueensHelper(i+1,tmp + [self.s[:j] + "Q" + self.s[j+1:]], col | {j}, z_diagonal |{i + j} , f_diagonal |{i - j}  ) 
            


# @lc code=end

