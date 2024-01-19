'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:29:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-10 22:20:53
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

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        import math 

        if int(math.sqrt(c)) **2 == c:
            return True 
        else:
            end = int(math.sqrt(c))
            # print(end)
        
            for i in range(end,-1,-1):
                rest = c - i*i 
                if int(math.sqrt(rest)) **2 == rest:
                    return True 

            return False
# @lc code=end

