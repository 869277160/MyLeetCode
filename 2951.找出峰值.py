'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:58:33
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 16:00:03
FilePath: \Leetcode_Solver\2951.找出峰值.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2951 lang=python3
#
# [2951] 找出峰值
#

# @lc code=start
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        
        res = []
        for i in range(1,len(mountain)-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                res.append(i)
        return res 
# @lc code=end

