'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-07 15:29:29
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-07 16:01:03
FilePath: \Leetcode_Solver\289.生命游戏.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        old_board = []
        for i in range(len(board)):
            old_board.append([board[i][j] for j in range(len(board[0]))])
            # for j in 
            #     old_board.append(board[i][j])

        for i in range(len(board)):
            for j in range(len(board[0])):
                sourround = self.get_sourrounding(old_board,i,j)
                board[i][j] = self.update_list(sourround, old_board[i][j])
        
        
    def get_sourrounding(self, old_boards, i:int, j:int) -> List:
        # print(i,j)
        # res = [0 for i in range(8)]
        res = list()
        if i - 1 > 0:
            res += [old_boards[i-1][j]]
            if j - 1 > 0:
                res += [old_boards[i-1][j-1]]
            if j + 1 < len(old_boards[0]):
                res += [old_boards[i-1][j+1]]
        
        # print(res)
        if i + 1 < len(old_boards):
            print(old_boards[i+1][j])
            res.append(old_boards[i+1][j])
            if j - 1 > 0:
                res += [old_boards[i+1][j-1]]
            if j + 1 < len(old_boards[0]):
                res += [old_boards[i+1][j+1]]
        
        if j - 1 > 0:
            res += [old_boards[i][j-1]]
        if j + 1 < len(old_boards[0]):
            res += [old_boards[i][j+1]]
            
        print(i,j, res)
        return res 

            
    def update_list(self,input_list:List, target:int) -> int:
        
        total = sum(input_list)
        
        if target == 1:
            if total < 2:
                return 0
            elif total == 2 or total == 3:
                return 1
            elif total > 3:
                return 0

        if target == 0 :
            if total == 3 :
                return 1
            else:
                return 0
# @lc code=end

