'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 21:01:31
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 21:03:46
FilePath: \Leetcode_Solver\292.nim-游戏.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n < 3 :
            return True 
        else :
            return n % 4 != 0
        
        
        
        
        
# @lc code=end

