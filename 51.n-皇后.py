'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-12 23:12:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-08-25 17:08:27
FilePath: \Leetcode_Solver\51.n-皇后.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List 
# @lc code=start

# 注意：python 代码由 chatGPT🤖 根据我的 cpp 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码还未经过力扣测试，仅供参考，如有疑惑，可以参照我写的 cpp 代码对比查看。
class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        # 生成矩阵
        if n == 1 :
            return [["Q"]]
        elif n == 2 or n == 3:
            return []
        else:
            self.res = []
            board = [["."] * n for _ in range(n)]
            self.backtrack(board, 0)
            return self.res


    def backtrack(self, input_table: List[List[str]], row: int) -> None:
        if row == len(input_table):
            output_table = ["".join(row) for row in input_table]
            self.res.append(output_table)
            return


        n = len(input_table[row])
        for col in range(n):
            # print(input_table)
            # 首先判断位置是否合法，如果合法则进行下一步
            if self.isValid(input_table, row, col):
                # 这个位置合法则进入下一行进行搜索
                input_table[row][col] = "Q"
                self.backtrack(input_table, row + 1)
                input_table[row][col] = "."
            else:
                pass 
    
        
    # 检查是否和现有位置产生冲突，
    # 由于是基于行进行搜索的，
    # 因此不需要检测行
    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        n = len(board)
        # 检查列是否有皇后冲突
        for i in range(n):
            if board[i][col] == "Q":
                return False
        
        # 检查右上方是否有皇后冲突
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
    
        # 检查左上方是否有皇后冲突
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        return True
    
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     # 生成矩阵
    #     if n == 1 :
    #         return [["Q"]]
    #     elif n == 2 or n == 3:
    #         return []
    #     else:
    #         self.res = []
    #         self.s = "." * n
    #         self.n = n
    #         self.solveNQueensHelper(0,[],set(),set(),set())  
    #         return self.res 

    # def solveNQueensHelper(self,i, tmp,col,z_diagonal,f_diagonal):
    #     if i == self.n:
    #         self.res.append(tmp)
    #         return 
    #     for j in range(self.n):
    #         if j not in col and i + j not in  z_diagonal and i - j not in f_diagonal:
    #             self.solveNQueensHelper(i+1,tmp + [self.s[:j] + "Q" + self.s[j+1:]], col | {j}, z_diagonal |{i + j} , f_diagonal |{i - j}  ) 
            
# @lc code=end


if __name__ == "__main__":
    s = Solution()

    print((s.solveNQueens(4)))