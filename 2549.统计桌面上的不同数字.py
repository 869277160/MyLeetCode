'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-06 14:58:08
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-06 14:59:36
FilePath: \Leetcode_Solverd:\Leetcode_Solver\2549.统计桌面上的不同数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2549 lang=python3
#
# [2549] 统计桌面上的不同数字
#

# @lc code=start
class Solution:
    def distinctIntegers(self, n: int) -> int:
        
        return n - 1 if n > 1 else 1

        # res = [n]
        # for i in range(n):
        #     if n % i == 0:
        #         res.append(i)
        # return len(res)
        
        
        
# @lc code=end

