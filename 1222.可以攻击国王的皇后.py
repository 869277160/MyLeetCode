'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 16:33:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 16:57:01
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1222.可以攻击国王的皇后.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1222 lang=python3
#
# [1222] 可以攻击国王的皇后
#

# @lc code=start
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        # 上下左右以及对角线搜索和K 距离最近的皇后就行了
        
        # 可以从K的角度进行广度搜索，现在是从queen的角度进行搜索，会慢一些
        

        res = []
        # 上下搜索
        up_queen = [[queen[0],king[1]] for queen in queens if queen[1] == king[1] and queen[0]< king[0]]
        if up_queen != []:
            res += self.QueenSearch(up_queen,king)
        
        down_queen = [[queen[0],king[1]] for queen in queens if queen[1] == king[1] and queen[0]> king[0]]
        if down_queen != []:
            res += self.QueenSearch(down_queen,king)
        
        # 左右搜索
        left_queen = [[king[0],queen[1]] for queen in queens if queen[0] == king[0] and queen[1]< king[1]]
        if left_queen != []:
            res += self.QueenSearch(left_queen,king)
        
        right_queen = [[king[0],queen[1]] for queen in queens if queen[0] == king[0] and queen[1]> king[1]]
        if right_queen != []:
            res += self.QueenSearch(right_queen,king)
        
        # 正对角线搜索
        up_left_queen = [[king[0]-i,king[1]-i] for i in range(1,8) if [king[0]-i,king[1]-i] in queens]
        if up_left_queen != []:
            res += self.QueenSearch(up_left_queen,king)
        
        down_right_queen = [[king[0]+i,king[1]+i] for i in range(1,8) if [king[0]+i,king[1]+i] in queens]
        if down_right_queen != []:
            res += self.QueenSearch(down_right_queen,king)
                    
        # 负对角线搜索
        up_right_queen = [[king[0]-i,king[1]+i] for i in range(1,8) if [king[0]-i,king[1]+i] in queens]
        if up_right_queen != []:
            res += self.QueenSearch(up_right_queen,king)
        
        down_left_queen = [[king[0]+i,king[1]-i] for i in range(1,8) if [king[0]+i,king[1]-i] in queens]
        if down_left_queen != []:
            res += self.QueenSearch(down_left_queen,king)
                
        return res 
        
    def QueenSearch(self,queens,kings):
        
        if len(queens) == 1 :
            return [queens[0]]
        else :
            all_dis = [(queen[0]-kings[0])**2+(queen[1]-kings[1])**2 for queen in queens]
            for i in range(len(all_dis)):
                if all_dis[i] == min(all_dis):
                    return [queens[i]]
            
        
        
# @lc code=end

