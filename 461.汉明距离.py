'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-04 23:21:14
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-04 23:21:30
FilePath: \Leetcode_Solverd:\Leetcode_Solver\461.汉明距离.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        return bin(x^y).count('1')
        
        
# @lc code=end

