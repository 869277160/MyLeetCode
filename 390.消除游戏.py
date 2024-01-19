'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-19 22:22:34
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-19 22:28:02
FilePath: \Leetcode_Solver\390.消除游戏.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=390 lang=python3
#
# [390] 消除游戏
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        
        return 1 if n == 1 else  2 * (n // 2 + 1 - self.lastRemaining(n // 2))
        
        
# @lc code=end

