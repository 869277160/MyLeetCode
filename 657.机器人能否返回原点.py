'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 11:18:31
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 11:19:54
FilePath: \Leetcode_Solver\657.机器人能否返回原点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        import collections
        
        freq = collections.Counter(moves)

        if freq["U"] == freq["D"] and freq["L"] == freq["R"]:
            return True
        else:
            return False 

        
        
        
        
# @lc code=end

