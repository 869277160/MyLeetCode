#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#

# @lc code=start
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        alphbet_dict = dict()
        for i in range(len(board)):
            for j in range(len(board[i])):
                alphbet_dict[board[i][j]] = (i, j)
        
        res = ""
        current_letter = "a"
        for next_letter in target:
            # 相同
            if current_letter == next_letter:
                res += "!"
            # 不同
            else:
                # 不同，但是有一个字母为Z
                if current_letter == "z" and next_letter != "z":
                    res += "U"
                    current_pos = alphbet_dict["u"]
                    next_pos = alphbet_dict[next_letter]
                    for i in range(current_pos[0] - next_pos[0]):
                        res += "U"
                    
                    for i in range(next_pos[1] - current_pos[1]):
                        res += "R"
                    res+="!"
                
                elif current_letter != "z" and next_letter == "z":
                    next_pos = alphbet_dict["u"]
                    current_pos = alphbet_dict[current_letter]
                    for i in range(next_pos[0] - current_pos[0]):
                        res += "D"
                    
                    for i in range(current_pos[1]- next_pos[1]):
                        res += "L"
                    res += "D"
                    res+="!"
                # 不同，但是没有Z
                else:
                    current_pos = alphbet_dict[current_letter]
                    next_pos = alphbet_dict[next_letter]
                    
                    if next_pos[0] <= current_pos[0]:
                        for i in range(current_pos[0] - next_pos[0]):
                            res += "U"
                    elif next_pos[0] > current_pos[0]:
                        for i in range(next_pos[0] - current_pos[0]):
                            res += "D"
                    
                    if next_pos[1] <= current_pos[1]:
                        for i in range(current_pos[1] - next_pos[1]):
                            res += "L"
                    elif next_pos[1] > current_pos[1]:
                        for i in range(next_pos[1] - current_pos[1]):
                            res += "R"
                         
                    # for i in range(next_pos[1] - current_pos[1]):
                    #     res += "R"   
                    res+="!"
                
                    
            
            current_letter = next_letter
        
        return res
        
        
        
        
# @lc code=end

