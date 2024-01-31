'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 19:29:33
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 19:30:24
FilePath: \Leetcode_Solver\2833.距离原点最远的点.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2833 lang=python3
#
# [2833] 距离原点最远的点
#

# @lc code=start
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count("L")- moves.count("R")) + moves.count("_")

# @lc code=end

