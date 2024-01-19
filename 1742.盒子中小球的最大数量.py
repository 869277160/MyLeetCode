'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 09:39:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 09:42:47
FilePath: \Leetcode_Solver\1742.盒子中小球的最大数量.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#

# @lc code=start
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        # 1-10 11-20 21-30 31-40 41-50 51-60
        # 
        # 
        res =  [0] * 46
        for i in range(lowLimit,highLimit+1):
            res[sum([int(j) for j in str(i)])] += 1
        return max(res)
        
        
        
# @lc code=end

