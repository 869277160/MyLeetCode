'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-19 15:39:58
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-19 15:40:22
FilePath: \Leetcode_Solver\1812.判断国际象棋棋盘中一个格子的颜色.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1812 lang=python3
#
# [1812] 判断国际象棋棋盘中一个格子的颜色
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        return (ord(coordinates[0]) + int(coordinates[1])) % 2 == 1
        
# @lc code=end

