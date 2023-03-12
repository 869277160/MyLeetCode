'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:29:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 22:30:38
FilePath: \Leetcode_Solver\633.平方数之和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math 
        
        if int(math.sqrt(c))**2 == c:
            return True

        for i in range(1,int(math.sqrt(c))+1):
            for j in range(0,int(math.sqrt(c))+1):
                if i**2 + j**2 == c:
                    return True
        
        return False
# @lc code=end

