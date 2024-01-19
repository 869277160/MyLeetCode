'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 11:53:10
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 11:54:36
FilePath: \Leetcode_Solver\2520.统计能整除数字的位数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2520 lang=python3
#
# [2520] 统计能整除数字的位数
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        
        count = 0 
        for diver in [int(i) for i in str(num)]:
            if num % diver == 0:
                count +=1 
        
        return count
        
        
        
# @lc code=end

