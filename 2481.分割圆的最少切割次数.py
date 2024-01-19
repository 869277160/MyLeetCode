'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 19:20:53
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 19:25:10
FilePath: \Leetcode_Solver\2481.分割圆的最少切割次数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2481 lang=python3
#
# [2481] 分割圆的最少切割次数
#

# @lc code=start
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return n //2 
        elif n%2  ==1 :
            return n           
# @lc code=end

