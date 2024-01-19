'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 09:26:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 09:26:48
FilePath: \Leetcode_Solver\1732.找到最高海拔.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        res = [0]
        for i in range(len(gain)):
            res.append(res[-1] + gain[i])
        return max(res)
        
        
        
        
# @lc code=end

