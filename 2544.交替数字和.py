'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 11:09:56
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 11:11:27
FilePath: \Leetcode_Solver\2544.交替数字和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2544 lang=python3
#
# [2544] 交替数字和
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        #  计算各个位数的和
        str_n = str(n)
        total = 0
        for i in range(len(str_n)):
            if i % 2 == 0:
                total += int(str_n[i])
            else:
                total += int(str_n[i]) * -1
        return total
        
        
        
        
# @lc code=end

