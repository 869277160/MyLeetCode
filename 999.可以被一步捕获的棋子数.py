#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
       
        Rook_row, Rook_col = 0,0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== "R":
                    Rook_row,Rook_col = i,j
        
        counter = 0
        # (1) 向上遍历
        for i in range(Rook_row-1,-1,-1):
            if board[i][Rook_col] == "B":
                break
            elif board[i][Rook_col] == "p":
                counter +=1 
                break
        
        # (2) down travel 
        for i in range(Rook_row+1,len(board)):
            if board[i][Rook_col] == "B":
                break
            elif board[i][Rook_col] == "p":
                counter +=1 
                break
        
        # Left
        for j in range(Rook_col-1,-1,-1):
            if board[Rook_row][j] == "B":
                break
            elif board[Rook_row][j] == "p":
                counter +=1 
                break
        
        # right
        for j in range(Rook_col+1,len(board[0])):
            if board[Rook_row][j] == "B":
                break
            elif board[Rook_row][j] == "p":
                counter +=1 
                break
        
        
        return counter
# @lc code=end

