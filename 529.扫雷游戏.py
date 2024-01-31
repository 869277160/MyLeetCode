#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row = len(board)
        col = len(board[0])
        
        # print(click)
        # print(board)
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        if board[click[0]][click[1]] == 'E':
            near_mines = self.count_mines(board,click[0],click[1])
            if  near_mines > 0:
                board[click[0]][click[1]] = str(near_mines)
                return board
            else :
                board[click[0]][click[1]] = 'B'
                new_clicks = []
                for i in range(-1,2):
                    for j in range(-1,2):
                        current_row = click[0] + i 
                        current_col = click[1] + j
                        if current_col >= 0 and current_row >= 0 and current_col < col and current_row < row:
                            if board[current_row][current_col] == 'E':
                                next_click = [current_row, current_col]
                                new_clicks.append(next_click)
                for new_click in new_clicks:
                    board = self.updateBoard(board, new_click)
                return board
        if board[click[0]][click[1]].isdigit() or board[click[0]][click[1]] == 'B':
            return board
        
    def count_mines(self, board, input_row, input_col):
        row = len(board)
        col = len(board[0])
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                current_row = input_row + i 
                current_col = input_col + j
                if current_col >= 0 and current_row >= 0 and current_col < col and current_row < row:
                    if board[current_row][current_col] == "M":
                        count +=1
        return count 
        
# @lc code=end

