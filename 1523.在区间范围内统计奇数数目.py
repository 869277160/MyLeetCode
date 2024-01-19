'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 14:43:54
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 14:45:11
FilePath: \Leetcode_Solver\1523.在区间范围内统计奇数数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low % 2 == 0 and high %2 == 0:
            return (high - low) // 2
        elif low%2 ==1 and high%2 == 1:
            return (high - low) // 2 + 1
        elif low%2 == 0 and high%2 == 1:
            return (high - low) // 2 + 1
        elif low%2 == 1 and high%2 == 0:
            return (high - low) // 2 + 1
        
        
        
        
# @lc code=end

