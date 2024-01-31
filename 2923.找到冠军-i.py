'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 14:43:41
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 14:45:41
FilePath: \Leetcode_Solver\2923.找到冠军-i.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2923 lang=python3
#
# [2923] 找到冠军 I
#

# @lc code=start
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        for j, col in enumerate(zip(*grid)):
            if 1 not in col:  # 没有队伍可以击败 j
                return j


        
# @lc code=end

