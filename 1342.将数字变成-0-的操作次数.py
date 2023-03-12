'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-06 09:28:58
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-06 09:29:39
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1342.将数字变成-0-的操作次数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        res = 0
        
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            res += 1
        
        return res 
        
        
        
# @lc code=end

