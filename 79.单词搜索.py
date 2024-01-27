'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-25 15:59:09
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-25 16:49:55
FilePath: \Leetcode_Solver\79.单词搜索.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution: 
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n_row, n_col = len(board), len(board[0])
        if len(word) > n_row *n_col:
                return False
        visited = []
        for i in range(n_row):
            visited.append([])
            for j in range(n_col):
                visited[i].append(False)
        
       
        else:
            for i in range(n_row):
                for j in range(n_col):
                    if word[0] == board[i][j]:
                        visited[i][j] = True
                        out_1 = self.dfs(board, visited, i + 1, j, word[1:])
                        out_2 = self.dfs(board, visited, i, j + 1, word[1:])
                        out_3 = self.dfs(board, visited, i - 1, j, word[1:])
                        out_4 = self.dfs(board, visited, i, j-1, word[1:])
                        if out_1 or out_2 or out_3 or out_4:
                            return True
                        visited[i][j] = False
            return False  
    
    def dfs(self, board: List[List[str]], visited: List[List[str]], current_row:int, current_col:int, word: str):
        n_row, n_col = len(board), len(board[0])
        # print(current_row, current_col, word)
        if word == "":
            return True
        if current_col >= n_col or current_col < 0:
            return False
        if current_row >= n_row or current_row < 0:
            return False
        if board[current_row][current_col] != word[0]:
            return False
        else:
            # print(board[current_row][current_col] ,word)
            if word[1:] == "":
                return True
            
            visited[current_row][current_col] = True
            out_1 = False 
            out_2 = False 
            out_3 = False 
            out_4 = False 
            if current_row + 1 >= n_row:
                out_1 = False
            else:
                if not visited[current_row + 1][current_col]:
                    out_1 = self.dfs(board, visited, current_row + 1, current_col, word[1:])
            
            if current_col + 1 >= n_col:
                out_2 = False
            else:
                if not visited[current_row][current_col + 1]:
                    out_2 = self.dfs(board, visited, current_row, current_col + 1, word[1:])
            

            if current_row - 1 < 0:
                out_3 = False
            else:
                if not visited[current_row - 1][current_col]:
                    out_3 = self.dfs(board, visited, current_row - 1, current_col, word[1:])
            
            if current_col - 1 < 0:
                out_4 = False
            else:
                if not visited[current_row][current_col - 1]:
                    out_4 = self.dfs(board, visited, current_row, current_col - 1, word[1:])

            if out_1 or out_2 or out_3 or out_4:
                return True
            else:
                visited[current_row][current_col] = False
                return False
# @lc code=end

