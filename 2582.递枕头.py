'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-09-26 10:08:02
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-09-26 10:18:05
FilePath: \Leetcode_Solver\2582.递枕头.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2582 lang=python3
#
# [2582] 递枕头
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n :
            return time + 1 
        elif time == n :
            return n - 1
        elif time > n :
            rest = time - n 
            idx = rest % (2*n -2) 
            loop = [i for i in range(n-1,1,-1)] + [i for i in range(1,n+1)]
            return loop[idx]
        
# @lc code=end

