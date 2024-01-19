'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 21:19:34
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 21:20:23
FilePath: \Leetcode_Solver\367.有效的完全平方数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math 
        return int(math.sqrt(num))**2 == num
            
        
# @lc code=end

