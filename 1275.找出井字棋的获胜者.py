#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [" " for _ in range(10)]
        for i in range(len(moves)):
            if i % 2 == 0:
                board[3*moves[i][0] + moves[i][1]] = "A"
            if i % 2 == 1:
                board[3*moves[i][0] + moves[i][1]] = "B"
        # print(board)
        length = len(moves)
        board = "".join(board)
        return self.is_win(board, length)
            
    
    
    def is_win(self, board, length):
        win_1 = [[0,4,8],[2,4,6]]
        win_2 = [[0,1,2],[3,4,5],[6,7,8]]
        win_3 = [[0,3,6],[1,4,7],[2,5,8]]
        for win in win_1:
            # print(board[win[0]], board[win[1]], board[win[2]])
            if board[win[0]] == board[win[1]] and board[win[2]] == board[win[1]] and board[win[0]] != " ":
                return board[win[0]]
            
        for win in win_2:
            # print(board[win[0]], board[win[1]], board[win[2]])
            if board[win[0]] == board[win[1]] and board[win[2]] == board[win[1]] and board[win[0]] != " ":
                return board[win[0]]
        for win in win_3:
            # print(board[win[0]], board[win[1]], board[win[2]])
            if board[win[0]] == board[win[1]] and board[win[2]] == board[win[1]] and board[win[0]] != " ":
                return board[win[0]]

        
        if length == 9:
            return "Draw"
        else :
            return "Pending"
# @lc code=end

